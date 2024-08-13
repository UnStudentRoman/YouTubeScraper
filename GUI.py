import logging
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from time import time
from worker import Worker
from logger_config import QTextEditLogger


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        # Setup GUI from template
        uic.loadUi(r'utils/gui.ui', self)
        self.show()
        self.setWindowTitle('Youtube Video Scraper')
        self.setWindowIcon(QIcon('utils/icon.ico'))

        # Setup scrape button action
        self.scrape_button.clicked.connect(self.scrape)
        # Create a worker thread and move the logging worker to it
        self.thread = QThread()
        self.worker = Worker(video_url=self.video_url, api_key=self.api_key)

        # Setup logger
        self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Create a QTextEditLogger handler
        text_edit_handler = QTextEditLogger(self.text_edit)

        # Define the log format
        log_format = (
            "%(asctime)s - "  # Timestamp
            "%(levelname)s - "  # Log level (e.g., INFO, DEBUG, ERROR)
            "%(message)s"  # Log message
        )

        text_edit_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(text_edit_handler)  # Add handler to the logger

    def thread_start(self):
        self.worker.log_signal.connect(self.log_message)
        self.worker.moveToThread(self.thread)

        # Start the worker thread
        self.thread.started.connect(self.worker.scape)
        self.thread.start()

        self.scrape_button.setEnabled(False)  # Disable button while worker thread is functioning.

    def scrape(self):
        start = time()

        logging.info(f'This is api key inserted by user: {self.api_key.text()}.')
        logging.info(f'This is video url inserted by user: {self.video_url.text()}.')

        # Start working thread.
        self.thread_start()

        end = time()
        logging.info(f'Done - Process ran for {"{:.2f}".format((end - start) / 60)} minutes.')

    def log_message(self, message):
        logging.info(message)

    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()
        super().closeEvent(event)


def gui():
    app = QApplication([])  # Start application.

    # Create Window and generate Window features.
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    pass
