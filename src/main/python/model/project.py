import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional
from model.supporting_model import TrimmingData


class Project:
    __settings_dict = dict()
    __project_path_key = "project_path"
    __project_name_key = "project_name"
    __project_file_extension = ".sdt"
    __number_of_angles_key = "number_of_angles"
    __latest_threshold_key = "latest_threshold"
    __latest_trimming_data_key = "latest_trimming_data"
    __latest_training_date_key = "latest_training_date"
    __latest_dataset_image_path_key = "latest_dataset_image_path"
    __latest_inspection_image_path_key = "latest_inspection_image_path"

    @classmethod
    def project_path(cls) -> str:
        return cls.__settings_dict[cls.__project_path_key]

    @classmethod
    def save_project_path(cls, input_data: str):
        cls.__settings_dict[cls.__project_path_key] = input_data
        cls.__save_settings()

    @classmethod
    def number_of_angles(cls) -> int:
        return cls.__settings_dict[cls.__number_of_angles_key]

    @classmethod
    def save_number_of_angles(cls, input_data: int):
        cls.__settings_dict[cls.__number_of_angles_key] = input_data
        cls.__save_settings()

    @classmethod
    def latest_threshold(cls) -> float:
        return cls.__settings_dict[cls.__latest_threshold_key]

    @classmethod
    def save_latest_threshold(cls, input_data: float):
        cls.__settings_dict[cls.__latest_threshold_key] = input_data
        cls.__save_settings()

    @classmethod
    def latest_training_date(cls) -> Optional[datetime]:
        training_date_str = cls.__settings_dict[cls.__latest_training_date_key]
        if training_date_str is None:
            return None
        else:
            # datetime.fromisoformat is available in python 3.7 and later
            return datetime.strptime(training_date_str, "%Y-%m-%dT%H:%M:%S.%f")

    @classmethod
    def save_latest_training_date(cls, training_date: datetime = datetime.now()):
        cls.__settings_dict[cls.__latest_training_date_key] = training_date.isoformat()
        cls.__save_settings()

    @classmethod
    def latest_dataset_image_path(cls) -> str:
        return cls.__settings_dict[cls.__latest_dataset_image_path_key]

    @classmethod
    def save_latest_dataset_image_path(cls, image_path: str):
        cls.__settings_dict[cls.__latest_dataset_image_path_key] = image_path
        cls.__save_settings()

    @classmethod
    def latest_inspection_image_path(cls) -> str:
        return cls.__settings_dict[cls.__latest_inspection_image_path_key]

    @classmethod
    def save_latest_inspection_image_path(cls, image_path: str):
        cls.__settings_dict[cls.__latest_inspection_image_path_key] = image_path
        cls.__save_settings()

    @classmethod
    def latest_trimming_data(cls) -> TrimmingData:
        trimming_data_dict = cls.__settings_dict[cls.__latest_trimming_data_key]
        return TrimmingData(position=trimming_data_dict['position'],
                            size=trimming_data_dict['size'],
                            needs_trimming=trimming_data_dict['needs_trimming'])

    @classmethod
    def save_latest_trimming_data(cls, data: TrimmingData):
        cls.__settings_dict[cls.__latest_trimming_data_key] = {"position": data.position,
                                                               "size": data.size,
                                                               "needs_trimming": data.needs_trimming}
        cls.__save_settings()

    @classmethod
    def project_name(cls) -> str:
        return cls.__settings_dict[cls.__project_name_key]

    @classmethod
    def load_settings_file(cls, project_file_path: str):
        f = open(project_file_path, 'r')
        cls.__settings_dict = json.load(f)
        project_path = Path(project_file_path).parent
        cls.save_project_path(str(project_path))

    @classmethod
    def __save_settings(cls):
        # json書き込み中にsetting_dictが書き換えられた場合に関するエラー回避
        settings_dict = cls.__settings_dict.copy()
        fw = open(os.path.join(cls.project_path(), cls.project_name() + cls.__project_file_extension), 'w')
        json.dump(settings_dict, fw, indent=4)

    @classmethod
    def generate_project_file(cls, project_path: str, project_name: str):
        cls.__settings_dict = {
            cls.__project_path_key: project_path,
            cls.__project_name_key: project_name,
            cls.__latest_threshold_key: 0,
            cls.__number_of_angles_key: 1,
            cls.__latest_training_date_key: None,
            cls.__latest_dataset_image_path_key: None,
            cls.__latest_inspection_image_path_key: None,
            cls.__latest_trimming_data_key: {"position": None,
                                             "size": None,
                                             "needs_trimming": False}
        }
        cls.__project_file_name = project_name
        cls.__save_settings()

