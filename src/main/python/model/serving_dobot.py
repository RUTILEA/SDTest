from PyQt5.QtCore import pyqtSignal, QObject, QThread
import zmq
import threading


class ServingDobot(QObject):
    __default_instance = None
    dobot_req = pyqtSignal()

    @classmethod
    def default(cls):
        """returns default instance of LearningModel class."""
        if cls.__default_instance is None:
            cls.__default_instance = ServingDobot()
        return cls.__default_instance

    def __init__(self):
        QObject.__init__(self)
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:19111")
        self.is_waiting_req = True
        self.__waiting_dobot_req_thread = threading.Thread(target=self.waiting_dobot_req)
        self.__waiting_dobot_req_thread.start()

    def waiting_dobot_req(self):
        self.is_waiting_req = True
        while self.is_waiting_req:
            message = self.socket.recv_string()
            if message:
                self.dobot_req.emit()
                self.is_waiting_req = False

    def sending_inspection_result(self, result):
        if not self.is_waiting_req:
            if result:
                self.socket.send(b'OK')
            else:
                self.socket.send(b'NG')
            self.__waiting_dobot_req_thread = threading.Thread(target=self.waiting_dobot_req)
            self.__waiting_dobot_req_thread.start()




