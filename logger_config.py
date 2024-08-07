import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Function to add handler to the logger
def add_qt_handler(text_edit):
    text_edit_handler = QTextEditLogger(text_edit)
    text_edit_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(text_edit_handler)


class QTextEditLogger(logging.Handler):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit

    def emit(self, record):
        msg = self.format(record)
        self.text_edit.append(msg)
