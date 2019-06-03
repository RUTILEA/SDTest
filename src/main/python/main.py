from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QStyleFactory
from view.startup import StartupWidget
from model.camera_model import CameraModel
from model.fbs import AppInfo

import sys
import multiprocessing


class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                             # 2. Implement run()
        """ start QtApplication """

        # TODO:カメラ選択画面から使うカメラを選択できるようにする
        self.window = StartupWidget()
        self.window.setWindowTitle(AppInfo().app_name() + ' Version ' + AppInfo().version())
        self.window.show()

        # スタイルをwindows共用に(for develop)
        self.app.setStyle(QStyleFactory.create('Fusion'))

        return self.app.exec_()

if __name__ == "__main__":
    multiprocessing.freeze_support()

    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)
