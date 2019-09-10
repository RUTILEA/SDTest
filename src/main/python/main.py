from PySide2.QtWidgets import QStyleFactory
from view.startup import StartupWindow
from model.fbs import AppInfo
from fbs_runtime.application_context import cached_property, is_frozen
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.excepthook.sentry import SentryExceptionHandler
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtCore

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

    def qt_message_handler(mode, context, message):
        if mode == QtCore.QtInfoMsg:
            mode = 'Info'
        elif mode == QtCore.QtWarningMsg:
            mode = 'Warning'
        elif mode == QtCore.QtCriticalMsg:
            mode = 'critical'
        elif mode == QtCore.QtFatalMsg:
            mode = 'fatal'
        else:
            mode = 'Debug'
        print("%s: %s (%s:%d, %s)" % (mode, message, context.file, context.line, context.file))

    def run(self):                             # 2. Implement run()
        """ start QQmlApplicationEngine """
        app_engine = QQmlApplicationEngine()
        if len(sys.argv) > 1 and type(sys.argv[1]) is str:
            project_file_path = sys.argv[1]
            _, ext = os.path.splitext(project_file_path)
            if ext == '.sdt':
                # startup_window.move_to_main_window(project_file_path)
                StartupWindow(app_engine, appctxt)

        else:
            StartupWindow(app_engine, appctxt)

        # スタイルをwindows共用に(for develop)
        # self.app.setStyle(QStyleFactory.create('Fusion'))

        # TODO: Enable High DPI display with PySide for QML
        # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"   # fix "QT"
        # self.app.setAttribute(PySide2.Qt.AA_EnableHighDpiScaling, True)

        return self.app.exec_()


if __name__ == "__main__":
    multiprocessing.freeze_support()

    appctxt = AppContext()                      # 4. Instantiate the subclass
    QtCore.qInstallMessageHandler(appctxt.qt_message_handler)
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)
