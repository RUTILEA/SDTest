from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QStyleFactory
from view.startup import StartupWidget
from model.fbs import AppInfo
from fbs_runtime.application_context import cached_property, is_frozen
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.excepthook.sentry import SentryExceptionHandler

import os
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
        startup_window = StartupWidget()
        startup_window.setWindowTitle(AppInfo().app_name() + ' Version ' + AppInfo().version())
        if len(sys.argv) > 1 and type(sys.argv[1]) is str:
            project_file_path = sys.argv[1]
            _, ext = os.path.splitext(project_file_path)
            if ext == '.sdt':
                startup_window.move_to_main_window(project_file_path)
        else:
            # startup_window.show()
            startup_window.move_to_main_window("/Users/satoakitaka/sample_dhc/sample_dhc.sdt")
            # from view.q_camera_view_finder_with_guide import QCameraViewFinderWithGuide
            # q_camera = QCameraViewFinderWithGuide()
            # q_camera.show()

        # スタイルをwindows共用に(for develop)
        # self.app.setStyle(QStyleFactory.create('Fusion'))

        # Enable High DPI display with PyQt5
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        self.app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

        return self.app.exec_()


if __name__ == "__main__":
    multiprocessing.freeze_support()

    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)
