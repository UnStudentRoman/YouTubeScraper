import logging
from time import time
from YouTubeDriver import YTDriver
from PyQt5.QtCore import QObject, pyqtSignal


class Worker(QObject):
    log_signal = pyqtSignal(str)

    def __init__(self, video_url, api_key):
        super().__init__()
        self._video_url = video_url
        self._api_key = api_key

    def scape(self):
        start = time()

        obj = YTDriver()  # Create object
        obj.add_video_id(video=self._video_url.text())
        obj.yt_service_obj(self._api_key.text())  # Initialize YouTube Service Object
        obj.get_comments()
        obj.get_user_details()
        obj.generate_output()

        end = time()
        logging.info(f'Done - Process ran for {"{:.2f}".format((end - start) / 60)} minutes.')


if __name__ == '__main__':
    pass
