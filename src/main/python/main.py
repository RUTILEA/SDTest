from PyQt5.QtWidgets import QStyleFactory
from view.startup import StartupWidget
from model.fbs import AppInfo
from fbs_runtime.application_context import cached_property, is_frozen
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.excepthook.sentry import SentryExceptionHandler

import sys
import multiprocessing


class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext

    @cached_property
    def exception_handlers(self):
        result = super().exception_handlers
        if is_frozen():
            result.append(self.sentry_exception_handler)
        return result

    @cached_property
    def sentry_exception_handler(self):
        return SentryExceptionHandler(
            self.build_settings['sentry_dsn'],
            self.build_settings['version'],
            self.build_settings['environment'],
            callback=self._on_sentry_init
        )

    def _on_sentry_init(self):
        scope = self.sentry_exception_handler.scope
        from fbs_runtime import platform
        scope.set_extra('os', platform.name())
        scope.set_extra('build', AppInfo().version())

    def run(self):                             # 2. Implement run()
        """ start QtApplication """

        # TODO:カメラ選択画面から使うカメラを選択できるようにする
        # self.window = StartupWidget()

        # for debug
        from view.test import TestWidget
        from model.learning_model import LearningModel
        from model.project import Project
        Project.load_settings_file('/Users/satoakitaka/SampleProject/SampleProject.sdt')
        import numpy as np
        LearningModel.default().test_results.reload(distances_of_ok_images=np.array([0.1, 1, -1.2, 1.2, 1.3]),
                                                    distances_of_ng_images=np.array([-1, -1.2, 1.1, 0.8, -0.2, -1.0]))
        LearningModel.default().threshold = -0.8
        self.window = TestWidget()
        self.window.reload_test_results()


        self.window.setWindowTitle(AppInfo().app_name() + ' Version ' + AppInfo().version())
        self.window.show()

        # スタイルをwindows共用に(for develop)
        # self.app.setStyle(QStyleFactory.create('Fusion'))

        return self.app.exec_()


if __name__ == "__main__":
    multiprocessing.freeze_support()

    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)
