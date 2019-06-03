from fbs_runtime.application_context import ApplicationContext
from fbs import path
from os.path import exists, abspath, dirname
from pathlib import Path


class AppInfo(ApplicationContext):
    def app_name(self):
        return self.build_settings['app_name']

    def version(self):
        version = self.build_settings['version']
        version_path = dirname(__file__) + '/../../../freeze/base/version'

        if exists(version_path):
            version += ' Build ' + Path(version_path).read_text()

        return version

    def author(self):
        return self.build_settings['author']
