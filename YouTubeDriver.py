import time
import pandas as pd
from googleapiclient.discovery import build
import logging


class YTDriver:
    def __init__(self):
        self.service_obj = None
        self.video_id = None
        self.title = None
        self.api_key = None
        self.comments = []
        self.users_ids = set()
        self.users = []

    def get_api_key(self, key) -> str:
        if key:
            self.api_key = key
            return 'Youtube API Key successfully retrieved.'

        # elif os.environ.get('YOUTUBEAPIKEY2'):
        #     self.api_key = os.environ.get('YOUTUBEAPIKEY2')
        #     return 'Youtube API Key successfully retrieved.'
        return 'Youtube API Key failed to retrieve. Further actions will not work.'

    def add_video_id(self, video: str) -> None:
        try:
            self.video_id = video[video.index('www.youtube.com/watch?v=') + len('www.youtube.com/watch?v='):]

        except ValueError:
            logging.warning('URL invalid. Please make sure URL format is one of the below:'
                  '\n"https://www.youtube.com/watch?v=<VIDEO_ID>"'
                  '\n"http://www.youtube.com/watch?v=<VIDEO_ID>"'
                  '\n"www.youtube.com/watch?v=<VIDEO_ID>"')
        return None

    def yt_service_obj(self, key=None) -> None:
        """
        Build the YouTube service object
        :return:
        """
        logging.info(self.get_api_key(key))  # Try to retrieve API Key

        # Build YouTube service object
        self.service_obj = build('youtube', 'v3', developerKey=self.api_key)
        return None

    def generate_output(self) -> None:
        comments = pd.DataFrame(self.comments)
        comments = comments.drop(['channelId', 'textOriginal', 'authorProfileImageUrl', 'authorChannelId', 'canRate', 'viewerRating'], axis=1)
        comments.to_excel(f'{self.title if self.title else self.video_id}_comments.xlsx', index=False)

        users = pd.DataFrame.from_dict(self.users)
        users.to_excel(f'{self.title if self.title else self.video_id}_users_info.xlsx', index=False)
        logging.info(f'Outputs {self.title if self.title else self.video_id}_comments.xlsx and {self.title if self.title else self.video_id}_users_info.xlsx generated.')
        return None

    def get_comments(self):
        next_page_token = None

        # Comment Counting
        i = 1

        while True:
            # Call the YouTube API to get comments
            response = self.service_obj.commentThreads().list(
                                                                part='snippet',
                                                                videoId=self.video_id,
                                                                pageToken=next_page_token,
                                                                maxResults=100
            ).execute()

            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comment.update({'id': item['snippet']['topLevelComment']['id']})
                comment.update({'totalReplyCount': item['snippet']['totalReplyCount']})
                user = item['snippet']['topLevelComment']['snippet']['authorChannelId']['value']

                self.comments.append(comment)
                self.users_ids.add(user)

                # Comment Counting
                logging.info(f'Comment {i}')
                i += 1

                if item['snippet']['totalReplyCount'] > 0:
                    logging.info(f"For the current comment {item['snippet']['totalReplyCount']} replies were found.")
                    self.get_replies(parent_id=comment['id'])

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        return None

    def get_replies(self, parent_id: str) -> None:
        next_page_token = None

        while True:
            response = self.service_obj.comments().list(part='snippet', parentId=parent_id,
                                                        pageToken=next_page_token, maxResults=100).execute()

            for item in response['items']:
                comment = item['snippet']
                user = item['snippet']['authorChannelId']['value']
                self.comments.append(comment)
                self.users_ids.add(user)

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        return None

    def get_user_details(self) -> None:
        step = 50
        user_ids_lists = [list(self.users_ids)[i:i + step] for i in range(0, len(list(self.users_ids)), step)]

        # User Counting
        j = 1

        for user_ids in user_ids_lists:
            # Call the YouTube API to get user details
            response = self.service_obj.channels().list(
                part='snippet,contentDetails,statistics',
                id=user_ids
            ).execute()

            for item in response['items']:
                user_detail = {
                    'id': item['id'],
                    'channelDisplayName': item['snippet']['customUrl'] if 'customUrl' in item['snippet'] else 'Unknown',
                    'channelURL': f"https://www.youtube.com/{item['snippet']['customUrl'] if 'customUrl' in item['snippet'] else 'Unknown'}",
                    'title': item['snippet']['title'],
                    'description': item['snippet']['description'],
                    'joinedAt': item['snippet']['publishedAt'],
                    'viewCount': item['statistics']['viewCount'],
                    'subscriberCount': item['statistics'].get('subscriberCount', 'hidden'),
                    'videoCount': item['statistics']['videoCount']
                }
                self.users.append(user_detail)
                # User Counting
                logging.info(f"Users {j} / {len(list(self.users_ids))}.")
                j += 1
        return None


if __name__ == '__main__':
    start = time.time()

    VIDEO_ID = 'Ey0qVzG8_vU'

    obj = YTDriver()  # Create object
    obj.add_video_id(video=VIDEO_ID)
    obj.yt_service_obj()  # Initialize YouTube Service Object
    obj.get_comments()
    obj.get_user_details()
    obj.generate_output()

    end = time.time()
    logging.info(f'Done - Process ran for {"{:.2f}".format((end-start)/60)} minutes.')
