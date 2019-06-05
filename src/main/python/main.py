from PyQt5.QtWidgets import QStyleFactory
from view.startup import StartupWidget
from fbs_runtime.application_context import ApplicationContext, cached_property, is_frozen
from fbs_runtime.excepthook.sentry import SentryExceptionHandler

import sys


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
        # TODO: エラー情報に紐付けるユーザ情報
        # scope.user = {'id': 41, 'email': 'john@gmail.com'}

    def run(self):                             # 2. Implement run()
        """ start QtApplication """

        # TODO:カメラ選択画面から使うカメラを選択できるようにする
        self.window = StartupWidget()
        self.window.setWindowTitle(self.build_settings['app_name'] + ' Version ' + self.build_settings['version'])
        self.window.show()

        # スタイルをwindows共用に(for develop)
        self.app.setStyle(QStyleFactory.create('Fusion'))

        return self.app.exec_()

if __name__ == "__main__":
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)
