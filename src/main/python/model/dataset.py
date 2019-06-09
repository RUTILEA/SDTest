from datetime import datetime
from enum import Enum, auto
from pathlib import Path
from model.project import Project
import os, cv2


class Dataset:

    class Category(Enum):
        TRAINING_OK = auto()
        TEST_OK = auto()
        TEST_NG = auto()

    @classmethod
    def _root_path(cls) -> str:
        return Project.project_path() + "/dataset"

    @classmethod
    def images_path(cls, category: Category) -> Path:
        if category is cls.Category.TRAINING_OK:
            return Path(cls._root_path() + '/train/OK')
        elif category is cls.Category.TEST_OK:
            return Path(cls._root_path() + '/test/OK')
        elif category is cls.Category.TEST_NG:
            return Path(cls._root_path() + '/test/NG')
        else:
            assert False

    @classmethod
    def trimed_path(cls, category: Category) -> Path:
        if category is cls.Category.TRAINING_OK:
            return Path(cls._root_path() + '/train/trim')
        elif category is cls.Category.TEST_OK:
            return Path(cls._root_path() + '/test/OKtrim')
        elif category is cls.Category.TEST_NG:
            return Path(cls._root_path() + '/test/NGtrim')
        else:
            assert False

    @classmethod
    def generate_image_path(cls, category: Category, cam_number: int, file_extension: str) -> Path:
        timestamp = str(datetime.now().isoformat()).replace(':', '-')
        file_name = f'camera_{cam_number}_{timestamp}{file_extension}'
        return cls.images_path(category).joinpath(file_name)

    @classmethod
    def trim_image(cls, path: Path, category: Category, data: tuple):
        img = cv2.imread(path)
        position = data[0]
        size = data[1]
        rect = img[int(position[1]):int(position[1])+size[1], int(position[0]):int(position[0])+size[0]]
        file_name = os.path.basename(path)
        cv2.imwrite(str(cls.trimed_path(category).joinpath(file_name)), rect)
