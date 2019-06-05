from fbs_runtime.application_context import ApplicationContext
from fbs import path
from os.path import exists, abspath, dirname
from pathlib import Path


class AppInfo(ApplicationContext):
    def app_name(self):
        return self.build_settings['app_name']

    def version(self):
        version = self.build_settings['version']

        # Add the latest commit hash as build number
        if exists(dirname(__file__) + '/../../../freeze/base/version'):
            version += ' Build ' + Path(dirname(__file__) + '/../../../freeze/base/version').read_text()
        elif exists(dirname(__file__) + '/../version'):
            version += ' Build ' + Path(dirname(__file__) + '/../version').read_text()

        return version

    def author(self):
        return self.build_settings['author']
