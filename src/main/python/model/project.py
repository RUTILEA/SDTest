import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional


class Project:
    __settings_dict = dict()
    __project_path_key = "project_path"
    __project_name_key = "project_name"
    __project_file_extension = ".sdt"
    __number_of_angles_key = "number_of_angles"
    __latest_threshold_key = "latest_threshold"
    __latest_training_date_key = "latest_training_date"

    @classmethod
    def project_path(cls):
        return cls.__settings_dict[cls.__project_path_key]

    @classmethod
    def save_project_path(cls, input_data):
        cls.__settings_dict[cls.__project_path_key] = input_data
        cls.__save_settings()

    @classmethod
    def number_of_angles(cls):
        return cls.__settings_dict[cls.__number_of_angles_key]

    @classmethod
    def save_number_of_angles(cls, input_data):
        cls.__settings_dict[cls.__number_of_angles_key] = input_data
        cls.__save_settings()

    @classmethod
    def latest_threshold(cls):
        return cls.__settings_dict[cls.__latest_threshold_key]

    @classmethod
    def save_latest_threshold(cls, input_data):
        cls.__settings_dict[cls.__latest_threshold_key] = input_data
        cls.__save_settings()

    @classmethod
    def latest_training_date(cls) -> Optional[datetime]:
        training_date_str = cls.__settings_dict[cls.__latest_training_date_key]
        if training_date_str is None:
            return None
        else:
            return datetime.fromisoformat(training_date_str)

    @classmethod
    def save_latest_training_date(cls, training_date: datetime = datetime.now()):
        cls.__settings_dict[cls.__latest_training_date_key] = training_date.isoformat()
        cls.__save_settings()

    @classmethod
    def project_name(cls):
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
    def generate_project_file(cls, project_path, project_name):
        cls.__settings_dict = {
            cls.__project_path_key: project_path,
            cls.__project_name_key: project_name,
            cls.__latest_threshold_key: 0,
            cls.__number_of_angles_key: 1,
            cls.__latest_training_date_key: None
        }
        cls.__project_file_name = project_name
        cls.__save_settings()

