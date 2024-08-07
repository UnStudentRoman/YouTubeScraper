from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from YouTubeDriver import YTDriver
import sys
import logging
import logger_config  # Import the logger configuration module


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi(r'utils/gui.ui', self)
        self.show()
        self.setWindowTitle('Youtube Video Scrapper')
        self.setWindowIcon(QIcon('utils/icon.ico'))

        self.scrape_button.clicked.connect(self.scrape)

        # Setup logger to use QTextEdit widget
        logger_config.add_qt_handler(self.text_edit)

    def scrape(self):
        logging.info(f'This is api key inserted by user: {self.api_key.text()}.')
        logging.info(f'This is video url inserted by user: {self.video_url.text()}.')

        obj = YTDriver()  # Create object
        obj.add_video_id(video=self.video_url.text())
        obj.yt_service_obj(self.api_key.text())  # Initialize YouTube Service Object
        obj.get_comments()
        obj.get_user_details()
        obj.generate_output()


def gui():
    app = QApplication([])  # Start application.

    # Create Window and generate Window features.
    window = MyGUI()
    app.exec_()


if __name__ == '__main__':
    gui()

