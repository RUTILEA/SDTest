from PyQt5.QtCore import pyqtSignal, QObject, QThread
from module.novelty_detector import NoveltyDetector
from model.dataset import Dataset
from model.project import Project
import numpy as np
import threading, os


class TestResults(object):
    def __init__(self):
        self.__distances_of_train_images = np.empty(shape=0)
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

    @property
    def distances_of_train_images(self) -> np.ndarray:
        return self.__distances_of_train_images

    def reload(self, distances_of_ok_images: np.ndarray, distances_of_ng_images: np.ndarray, distances_of_train_images: np.ndarray=None):
        assert(len(distances_of_ok_images.shape) == 1 and len(distances_of_ng_images.shape) == 1)
        self.__distances_of_ok_images = distances_of_ok_images
        self.__distances_of_ng_images = distances_of_ng_images
        if distances_of_train_images is not None:
            self.__distances_of_train_images = distances_of_train_images

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
        """Number of NG images judged to be NG"""
        return len([ng for ng in self.distances_of_ng_images if ng <= LearningModel.default().threshold])

    @property
    def true_negative(self) -> int:
        """Number of OK images judged to be OK"""
        return len([ok for ok in self.distances_of_ok_images if ok > LearningModel.default().threshold])

    @property
    def false_positive(self) -> int:
        """Number of OK images judged to be NG"""
        return len(self.distances_of_ok_images) - self.true_negative

    @property
    def false_negative(self) -> int:
        """Number of NG images judged to be OK"""
        return len(self.distances_of_ng_images) - self.true_positive

    @property
    def accuracy(self) -> float:
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
    def recall(self) -> float:
        if self.distances_of_ng_images.size == 0:
            return 0
        return float(self.true_positive) / float(self.distances_of_ng_images.size)

    @property
    def precision(self) -> float:
        TP = self.true_positive
        FP = self.false_positive
        if TP + FP == 0:
            return 0
        return float(self.true_positive) / float(TP+FP)

    @property
    def specificity(self) -> float:
        if self.distances_of_ok_images.size == 0:
            return 0
        return float(self.true_negative) / float(self.distances_of_ok_images.size)

    @property
    def __number_of_distances(self) -> int:
        return len(self.distances_of_ok_images) + len(self.distances_of_ng_images)


class LearningModel(QObject):
    __default_instance = None
    training_finished = pyqtSignal()
    training_start = pyqtSignal()
    predicting_finished = pyqtSignal(dict)
    predicting_start = pyqtSignal()
    test_finished = pyqtSignal(bool)

    @classmethod
    def default(cls):
        """returns default instance of LearningModel class."""
        if cls.__default_instance is None:
            cls.__default_instance = LearningModel()
        return cls.__default_instance

    def __init__(self):
        super().__init__()

        self.__model = NoveltyDetector(nth_layer=24, nn_name='ResNet', detector_name='ABOD')
        self.__threshold = Project.latest_threshold()
        self.__should_test = True  # TODO: assign True on dataset change
        self.test_results = TestResults()
        self.__training_thread = None

    @property
    def threshold(self) -> float:
        return self.__threshold

    @threshold.setter
    def threshold(self, new_value: float):
        self.__threshold = new_value
        Project.save_latest_threshold(new_value)

    def start_training(self):
        self.training_start.emit()
        self.__training_thread = threading.Thread(target=self.train)
        self.__training_thread.start()

    def train(self):
        self.__model.fit_in_dir(str(Dataset.trimmed_path(Dataset.Category.TRAINING_OK)))
        self.__model.save_ocsvm(LearningModel.__weight_file_path(cam_index=0))
        Project.save_latest_training_date()
        self.__should_test = True
        self.training_finished.emit()

    def load_weights(self):
        self.__model.load_ocsvm(LearningModel.__weight_file_path(cam_index=0))

    def start_predict(self, image_paths):
        image_path = image_paths[0]
        trimming_data = Project.latest_trimming_data()
        Dataset.trim_image(image_path, os.path.dirname(image_path), trimming_data)
        self.predicting_start.emit()
        predict_thread = threading.Thread(target=self.predict, args=([image_paths]))
        predict_thread.start()

    def predict(self, image_paths):
        scores = self.__model.predict_paths(image_paths)
        self.predicting_finished.emit({'scores': scores, 'image_paths': image_paths})

    def test_if_needed(self, predict_training=False):
        if not self.__should_test:
            self.test_finished.emitf(predict_training)
            return

        # TODO: check if test images exist
        test_thread = threading.Thread(target=self.test, args=(predict_training,))
        test_thread.start()

    def test(self, predict_training=False):
        try:
            _, pred_of_ok_images = self.__model.predict_in_dir(str(Dataset.trimmed_path(Dataset.Category.TEST_OK)))
            _, pred_of_ng_images = self.__model.predict_in_dir(str(Dataset.trimmed_path(Dataset.Category.TEST_NG)))
            if predict_training:
                _, pred_of_train_images = self.__model.predict_in_dir(str(Dataset.trimmed_path(Dataset.Category.TRAINING_OK)))
                self.test_results.reload(distances_of_ok_images=pred_of_ok_images, distances_of_ng_images=pred_of_ng_images, distance_of_train_images=pred_of_train_images)
            else:
                self.test_results.reload(distances_of_ok_images=pred_of_ok_images, distances_of_ng_images=pred_of_ng_images)
            if self.test_results.distances_of_ng_images.size != 0:
                self.threshold = max(self.test_results.distances_of_ng_images)  # default threshold FIXME: logic
                self.__should_test = False
        except IndexError:  # TODO: handle as UndoneTrainingError
            print('TODO: tell the user to train')
        except OSError:
            print('TODO: repair directory for test images')
        finally:
            self.test_finished.emit(predict_training)

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
