import sys

from PySide6.QtCore import QThread, QObject, Signal, Qt
from PySide6.QtWidgets import QApplication, QPushButton


def thread_id(thread: QThread) -> str:
    return str(id(thread))[-4:]


def current_thread_id() -> str:
    return thread_id(QThread.currentThread())


class TestObject(QObject):
    bridge: "Bridge"

    test_signal = Signal()

    def __init__(self, parent, bridge: "Bridge"):
        super().__init__(parent)

        self.bridge = bridge
        self.test_signal.connect(self.receiver, Qt.ConnectionType.QueuedConnection)
        print("TestObject thread on creation", thread_id(self.thread()))

    @classmethod
    def create_in_parent_thread(cls, parent: QObject, *args, **kwargs) -> "TestObject":
        inst = cls(None, *args, **kwargs)
        inst.moveToThread(parent.thread())
        inst.setParent(parent)
        return inst

    def emit_signal(self):
        print("---- SENDER", current_thread_id())
        print("TestObject thread on test", thread_id(self.thread()))
        self.test_signal.emit()

    def receiver(self):
        print("---- RECEIVER", current_thread_id())


class LoaderThread(QThread):
    bridge: QObject

    def __init__(self, parent: QObject, bridge: QObject):
        super().__init__(parent)
        self.bridge = bridge

    def run(self):
        self.bridge.test_obj = TestObject.create_in_parent_thread(self.bridge, self.bridge)


class Bridge(QObject):
    test_obj: "TestObject"

    def __init__(self, parent):
        super().__init__(parent)

        print("MAIN THREAD", thread_id(QApplication.instance().thread()))

        thr = LoaderThread(self, self)
        print("LOADER THREAD", thread_id(thr))

        thr.start()

    def on_button(self, *args, **kwargs):
        print("!! button clicked", current_thread_id())
        self.test_obj.emit_signal()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    brigge = Bridge(app)

    button = QPushButton("test")
    button.clicked.connect(brigge.on_button)
    button.show()

    app.exec()