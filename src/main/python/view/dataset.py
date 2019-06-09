import os
import shutil
from distutils.dir_util import copy_tree
from typing import Optional, Set
from pathlib import Path
from PyQt5.QtCore import Qt, QObject, QFileSystemWatcher, pyqtSignal, QRect, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel, QMenu, QMessageBox, QDesktopWidget
from view.ui.dataset import Ui_Dataset
from view.image_capture_dialog import ImageCaptureDialog
from view.select_area_dialog import SelectAreaDialog
from model.project import Project
from model.learning_model import LearningModel
from model.dataset import Dataset


class Thumbnail(QObject):
    def __init__(self, path: Path):
        super().__init__()
        self.path = path
        self.pixmap = QPixmap(str(path))


class DatasetWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dataset()
        self.ui.setupUi(self)

        self.all_thumbnails = []
        self.selected_thumbnails: Set[Thumbnail] = set()

        self.ui.image_list_widget.itemSelectionChanged.connect(self.on_changed_image_list_selection)
        self.ui.delete_images_button.clicked.connect(self.on_clicked_delete_images_button)
        self.ui.train_button.clicked.connect(self.on_clicked_train_button)

        self.ui.camera_and_images_menu = QMenu()
        self.ui.camera_and_images_menu.addAction(self.ui.select_images_action)
        self.ui.camera_and_images_menu.addAction(self.ui.camera_action)
        self.ui.camera_and_images_button.setMenu(self.ui.camera_and_images_menu)

        self.ui.select_images_action.triggered.connect(self.on_clicked_select_images_button)
        self.ui.camera_action.triggered.connect(self.on_clicked_camera_button)

        self.ui.image_list_widget.setCurrentItem(self.ui.image_list_widget.topLevelItem(0).child(0))  # FIXME: refactor
        self.ui.image_list_widget.expandAll()

        self._reload_images(Dataset.Category.TRAINING_OK)
        self.__reload_recent_training_date()

        self.capture_dialog: Optional[ImageCaptureDialog] = None

        self.preview_window = PreviewWindow()

        self.watcher = QFileSystemWatcher(self)
        self.watcher.addPaths([str(Dataset.images_path(Dataset.Category.TRAINING_OK)),
                               str(Dataset.images_path(Dataset.Category.TEST_OK)),
                               str(Dataset.images_path(Dataset.Category.TEST_NG))])
        self.watcher.directoryChanged.connect(self.on_dataset_directory_changed)

        self.select_area_dialog = SelectAreaDialog()
        self.select_area_dialog.finish_selecting_area.connect(self.on_finished_selecting_area)

        LearningModel.default().training_finished.connect(self.on_finished_training)

    def _reload_images(self, category: Dataset.Category):
        # reset selection
        self.selected_thumbnails.clear()
        self.ui.delete_images_button.setEnabled(False)

        # reset grid area contents
        current_images_count = self.ui.images_grid_area.count()
        if current_images_count > 0:
            for i in reversed(range(current_images_count)):
                self.ui.images_grid_area.itemAt(i).widget().setParent(None)

        image_paths = sorted(Dataset.images_path(category).iterdir())
        nullable_thumbnails = [Thumbnail(path=image_path) for image_path in image_paths]
        self.all_thumbnails = [thumbnail for thumbnail in nullable_thumbnails if not thumbnail.pixmap.isNull()]
        self.ui.number_of_images_label.setText(f'{len(self.all_thumbnails)}枚')

        row = 0
        column = 0
        for thumbnail in self.all_thumbnails:
            thumbnail_cell = ThumbnailCell(thumbnail=thumbnail)
            thumbnail_cell.selection_changed.connect(self.on_changed_thumbnail_selection)
            thumbnail_cell.double_clicked.connect(self.on_double_clicked_thumbnail)
            self.ui.images_grid_area.addWidget(thumbnail_cell, row, column)

            if column == 4:
                row += 1
                column = 0
            else:
                column += 1

    def on_changed_image_list_selection(self):
        selected_category = self.__selected_dataset_category()
        if selected_category is not None:
            self._reload_images(selected_category)

    def on_changed_thumbnail_selection(self, selected: bool, thumbnail: Thumbnail):
        if selected:
            self.selected_thumbnails.add(thumbnail)
        else:
            self.selected_thumbnails.remove(thumbnail)

        if self.selected_thumbnails:
            number_of_images_description = f'{len(self.all_thumbnails)}枚 - {len(self.selected_thumbnails)}枚選択中'
            self.ui.delete_images_button.setEnabled(True)
        else:
            number_of_images_description = f'{len(self.all_thumbnails)}枚'
            self.ui.delete_images_button.setEnabled(False)
        self.ui.number_of_images_label.setText(number_of_images_description)

    def on_double_clicked_thumbnail(self, thumbnail: Thumbnail):
        self.preview_window.set_thumbnail(thumbnail)
        self.preview_window.show()
        self.preview_window.activateWindow()
        self.preview_window.raise_()

        # move preview to center
        preview_geometry: QRect = self.preview_window.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        preview_geometry.moveCenter(screen_center)
        self.preview_window.move(preview_geometry.topLeft())

    def on_clicked_camera_button(self):
        selected_category = self.__selected_dataset_category()
        if selected_category is None:
            print('TODO: disable to select other items')
            return

        del self.capture_dialog
        self.capture_dialog = ImageCaptureDialog(image_save_location=str(Dataset.images_path(selected_category)))
        self.capture_dialog.show()

    def on_clicked_select_images_button(self):
        selected_category = self.__selected_dataset_category()
        if selected_category is None:
            print('TODO: disable to select other items')
            return

        ext_filter = '画像ファイル(*.jpg *.jpeg *.png *.gif *.bmp)'
        source_image_names = QFileDialog.getOpenFileNames(caption='データセットに取り込む', filter=ext_filter)[0]
        if source_image_names:
            for source_image_name in source_image_names:
                try:
                    # TODO: specify correct camera number
                    destination = Dataset.generate_image_path(category=selected_category,
                                                              cam_number=0,
                                                              file_extension=Path(source_image_name).suffix)
                    shutil.copyfile(source_image_name, destination)
                except shutil.SameFileError:
                    print("TODO: fix destination")

    def on_clicked_delete_images_button(self):
        assert self.selected_thumbnails

        message = f'{len(self.selected_thumbnails)}枚の画像を削除してよろしいですか?\nこの操作は取り消せません'
        selected_action = QMessageBox.warning(None, '', message, QMessageBox.Cancel, QMessageBox.Yes)
        if selected_action == QMessageBox.Yes:
            for selected_thumbnail in self.selected_thumbnails:
                os.remove(path=str(selected_thumbnail.path))
            self._reload_images(self.__selected_dataset_category())

    def on_clicked_train_button(self):
        self.select_area_dialog.show()
        self.__reload_recent_training_date()

    def on_finished_selecting_area(self, data: tuple):
        categories = [Dataset.Category.TRAINING_OK, Dataset.Category.TEST_OK, Dataset.Category.TEST_NG]
        for category in categories:
            dir_path = Dataset.images_path(category)
            save_path = Dataset.trimed_path(category)
            if os.path.exists(save_path):
                shutil.rmtree(save_path)
            os.mkdir(save_path)
            if not data[2]:
                copy_tree(str(dir_path), str(save_path))
            else:
                file_list = os.listdir(dir_path)
                file_list = [img for img in file_list if
                                  Path(img).suffix in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']]
                for file_name in file_list:
                    Dataset.trim_image(os.path.join(dir_path, file_name), category, data)
        LearningModel.default().start_training()

    def on_dataset_directory_changed(self, directory: str):
        selected_category = self.__selected_dataset_category()
        if str(Dataset.images_path(selected_category)) == directory:
            self._reload_images(selected_category)

    def on_finished_training(self):
        self.__reload_recent_training_date()

    def __selected_dataset_category(self) -> Optional[Dataset.Category]:
        current_item = self.ui.image_list_widget.currentItem()
        current_item_text = current_item.text(0)
        # FIXME: refactor
        if current_item_text == 'トレーニング用画像' or current_item_text == '性能評価用画像':
            return None
        elif current_item.parent().text(0) == 'トレーニング用画像':
            if current_item_text == '良品':  # train_OK
                return Dataset.Category.TRAINING_OK
        elif current_item.parent().text(0) == '性能評価用画像':
            if current_item_text == '良品':  # test_OK
                return Dataset.Category.TEST_OK
            elif current_item_text == '不良品':  # test_NG
                return Dataset.Category.TEST_NG
        else:
            assert False

    def __reload_recent_training_date(self):
        latest_training_date = Project.latest_training_date()
        if latest_training_date is None:
            self.ui.latest_training_date_label.setText('トレーニング未実行')
        else:
            date_description = latest_training_date.strftime('%Y/%m/%d')
            self.ui.latest_training_date_label.setText(f'前回のトレーニング：{date_description}')


class ThumbnailCell(QWidget):
    selection_changed = pyqtSignal(bool, Thumbnail)
    double_clicked = pyqtSignal(Thumbnail)

    def __init__(self, thumbnail: Thumbnail):
        super().__init__()

        THUMBNAIL_LENGTH = 80
        CELL_LENGTH = 88
        MIN_MARGIN = (CELL_LENGTH - THUMBNAIL_LENGTH) / 2

        self.setFixedSize(CELL_LENGTH, CELL_LENGTH)

        self.thumbnail = thumbnail

        self.thumbnail_label = QLabel(self)
        self.thumbnail_label.setAlignment(Qt.AlignCenter)
        if thumbnail.pixmap.width() < thumbnail.pixmap.height():
            scaled_thumbnail = thumbnail.pixmap.scaledToHeight(THUMBNAIL_LENGTH)
            horizontal_margin = (CELL_LENGTH - scaled_thumbnail.width()) / 2
            thumbnail_style_sheet = f'margin: {MIN_MARGIN}px {horizontal_margin}px'
        else:
            scaled_thumbnail = thumbnail.pixmap.scaledToWidth(THUMBNAIL_LENGTH)
            vertical_margin = (CELL_LENGTH - scaled_thumbnail.height()) / 2
            thumbnail_style_sheet = f'margin: {vertical_margin}px {MIN_MARGIN}px'
        self.thumbnail_label.setPixmap(scaled_thumbnail)
        self.thumbnail_label.setStyleSheet(thumbnail_style_sheet)

        self.__selection_overlay = ThumbnailSelectionOverlay(parent=self)
        self.__selection_overlay.setFixedSize(CELL_LENGTH, CELL_LENGTH)
        self.__selection_overlay.selection_changed.connect(self.__on_changed_selection)
        self.__selection_overlay.double_clicked.connect(self.__on_double_clicked)

        # NOTE: https://stackoverflow.com/questions/31178695/qt-stylesheet-not-working
        self.__selection_overlay.setAttribute(Qt.WA_StyledBackground)

    def __on_changed_selection(self, selected: bool):
        self.selection_changed.emit(selected, self.thumbnail)

    def __on_double_clicked(self):
        self.double_clicked.emit(self.thumbnail)


class ThumbnailSelectionOverlay(QWidget):
    selection_changed = pyqtSignal(bool)
    double_clicked = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.selected = False

    def mousePressEvent(self, QMouseEvent):
        self.selected = not self.selected
        if self.selected:
            style_sheet = 'background-color: rgba(66, 152, 249, 0.2);' \
                          'border: solid #4298f9;' \
                          'border-width: 2px;' \
                          'border-radius: 5px'
            self.setStyleSheet(style_sheet)
        else:
            self.setStyleSheet('')
        self.selection_changed.emit(self.selected)

    def mouseDoubleClickEvent(self, mouse_event):
        self.double_clicked.emit()


class PreviewWindow(QLabel):
    def set_thumbnail(self, thumbnail: Thumbnail):
        self.setWindowTitle(thumbnail.path.name)

        desktop_size: QSize = QDesktopWidget().availableGeometry().size()
        max_size = QSize(desktop_size.width() - 50, desktop_size.height() - 50)
        image_size: QSize = thumbnail.pixmap.size()
        scaled_size = image_size.scaled(max_size, Qt.KeepAspectRatio)
        if image_size.width() < scaled_size.width():
            preview_size = image_size
        else:
            preview_size = scaled_size

        self.setFixedSize(preview_size)
        self.setPixmap(thumbnail.pixmap.scaled(preview_size))
