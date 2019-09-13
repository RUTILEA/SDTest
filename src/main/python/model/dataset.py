from datetime import datetime
from enum import Enum, auto
from pathlib import Path
from model.project import Project
from model.supporting_model import TrimmingData
import os, cv2, subprocess


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
    def trimmed_path(cls, category: Category) -> Path:
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
    def trim_image(cls, path: Path, save_path: Path, data: TrimmingData):
        img = cv2.imread(path)
        check = subprocess.check_output(['convert', path, '-coalesce', 'null'], stderr=subprocess.STDOUT)
        if check:
            print('@@@ image corrupted @@@')
        position = data.position
        size = data.size
        rect = img[int(position[1]):int(position[1])+size[1], int(position[0]):int(position[0])+size[0]]
        file_name = os.path.basename(path)
        cv2.imwrite(os.path.join(save_path, file_name), rect)

