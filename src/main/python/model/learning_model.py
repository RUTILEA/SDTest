from PyQt5.QtCore import pyqtSignal, QObject, QThread
from module.novelty_detector import NoveltyDetector
from model.dataset import Dataset
from model.project import Project
import numpy as np


class TestResults(object):
    def __init__(self):
        self.__distances_of_ok_images = np.empty(shape=0)
        self.__distances_of_ng_images = np.empty(shape=0)
        self.min_distance = 0
        self.max_distance = 0

    @property
    def distances_of_ok_images(self) -> np.ndarray:
        return self.__distances_of_ok_images

    @property
    def distances_of_ng_images(self) -> np.ndarray:
        return self.__distances_of_ng_images

    def reload(self, distances_of_ok_images: np.ndarray, distances_of_ng_images: np.ndarray):
        assert(len(distances_of_ok_images.shape) == 1 and len(distances_of_ng_images.shape) == 1)
        self.__distances_of_ok_images = distances_of_ok_images
        self.__distances_of_ng_images = distances_of_ng_images

        # update min/max distances
        all_distances = np.hstack([self.distances_of_ok_images, self.distances_of_ng_images])
        if all_distances.size != 0:
            self.min_distance = min(all_distances)
            self.max_distance = max(all_distances)
        else:
            self.min_distance = 0
            self.max_distance = 0

    @property
    def true_positive(self) -> int:
        return len([ok for ok in self.distances_of_ok_images if ok > LearningModel.default().threshold])

    @property
    def true_negative(self) -> int:
        return len([ng for ng in self.distances_of_ng_images if ng <= LearningModel.default().threshold])

    @property
    def false_positive(self) -> int:
        return len(self.distances_of_ok_images) - self.true_positive

    @property
    def false_negative(self) -> int:
        return len(self.distances_of_ng_images) - self.true_negative

    @property
    def correct_rate(self) -> float:
        if self.__number_of_distances == 0:
            return 0
        return float(self.true_positive + self.true_negative) / self.__number_of_distances

    @property
    def false_positive_rate(self) -> float:
        if self.__number_of_distances == 0:
            return 0
        return float(self.false_positive) / self.__number_of_distances

    @property
    def false_negative_rate(self) -> float:
        if self.__number_of_distances == 0:
            return 0
        return float(self.false_negative) / self.__number_of_distances

    @property
    def __number_of_distances(self) -> int:
        return len(self.distances_of_ok_images) + len(self.distances_of_ng_images)


class LearningModel(QObject):
    __default_instance = None
    training_finished = pyqtSignal()
    training_start = pyqtSignal()
    predicting_finished = pyqtSignal(dict)
    predicting_start = pyqtSignal()
    test_finished = pyqtSignal()

    @classmethod
    def default(cls):
        """returns default instance of LearningModel class."""
        if cls.__default_instance is None:
            cls.__default_instance = LearningModel()
        return cls.__default_instance

    def __init__(self):
        super().__init__()
        self.__model = NoveltyDetector(nth_layer=24, nn_name='ResNet', detector_name='LocalOutlierFactor')
        self.__threshold = Project.latest_threshold()
        self.__should_test = True  # TODO: assign True on dataset change
        self.test_results = TestResults()

        self.__predicting_thread = PredictingThread(self.__model)
        self.__predicting_thread.finished.connect(self.predicting_finished)
        self.__training_thread = TrainingThread(self.__model)
        self.__training_thread.finished.connect(self.on_training_finished)
        self.__test_thread = TestThread(self.__model, self)
        self.__test_thread.finished.connect(self.on_test_finished)

    @property
    def threshold(self) -> float:
        return self.__threshold

    @threshold.setter
    def threshold(self, new_value: float):
        self.__threshold = new_value
        Project.save_latest_threshold(new_value)

    def start_training(self):
        self.training_start.emit()
        self.__training_thread.start()

    def on_training_finished(self):
        self.__model.save_ocsvm(LearningModel.__weight_file_path(cam_index=0))
        Project.save_latest_training_date()
        self.__should_test = True
        self.training_finished.emit()

    def cancel_training(self):
        self.__training_thread.exit()

    def load_weights(self):
        self.__model.load_ocsvm(LearningModel.__weight_file_path(cam_index=0))

    def predict(self, image_paths):
        self.predicting_start.emit()
        self.__predicting_thread.set_image_paths(image_paths)
        self.__predicting_thread.start()

    def on_predicting_finished(self, result):
        self.predicting_finished.emit(result)

    def test_if_needed(self):
        if not self.__should_test:
            self.test_finished.emit()
            return

        # TODO: check if test images exist

        self.__test_thread.start()

    def on_test_finished(self):
        if self.test_results.distances_of_ng_images.size != 0:
            self.threshold = max(self.test_results.distances_of_ng_images)  # default threshold FIXME: logic
            self.__should_test = False
        self.test_finished.emit()

    @classmethod
    def __weight_file_path(cls, cam_index: int) -> str:
        return Project.project_path() + f'/models/camera_{cam_index}.joblib'


class PredictingThread(QThread):
    finished = pyqtSignal(dict)

    def __init__(self, model):
        super().__init__()
        self.__image_paths = None
        self.__model = model

    def set_image_paths(self, image_paths):
        self.__image_paths = image_paths

    def run(self):
        scores = self.__model.predict_paths(self.__image_paths)
        self.finished.emit({'scores': list(scores), 'image_paths': self.__image_paths})


class TrainingThread(QThread):
    def __init__(self, model):
        super().__init__()
        self.__image_paths = None
        self.__model = model

    def set_image_path(self, image_path):
        self.__image_paths = image_path

    def run(self):
        try:
            self.__model.fit_in_dir(str(Dataset.images_path(Dataset.Category.TRAINING_OK)))
        except OSError:
            print('TODO: repair directory for training images')


class TestThread(QThread):
    finished = pyqtSignal()

    def __init__(self, model, learning_model):
        super().__init__()
        self.__image_paths = None
        self.__model = model
        self.__learning_model = learning_model

    def run(self):
        try:
            _, pred_of_ok_images = self.__model.predict_in_dir(str(Dataset.images_path(Dataset.Category.TEST_OK)))
            _, pred_of_ng_images = self.__model.predict_in_dir(str(Dataset.images_path(Dataset.Category.TEST_NG)))
            self.__learning_model.test_results.reload(distances_of_ok_images=pred_of_ok_images,
                                                      distances_of_ng_images=pred_of_ng_images)
            self.finished.emit()
        except IndexError:  # TODO: handle as UndoneTrainingError
            print('TODO: tell the user to train')
            self.finished.emit()
        except OSError:
            print('TODO: repair directory for test images')
