import logging
from PyQt5.QtCore import QMetaObject, Qt, Q_ARG


class QTextEditLogger(logging.Handler):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit

    def emit(self, record):
        msg = self.format(record)
        QMetaObject.invokeMethod(
            self.text_edit,
            "append",
            Qt.QueuedConnection,
            Q_ARG(str, msg)
        )


if __name__ == '__main__':
    pass
