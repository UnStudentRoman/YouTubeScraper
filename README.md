YouTube Video Comments Scraper
====================================

Description:
-------------
This program scrapes YouTube video comments, replies, and user information using the YouTube Data API. The outputs are written to two Excel files in the same directory as the executable.

Version Bug Fixes:
-------------
V.0.1 - Fixed GUI from freezing while scraper was running.

Prerequisites:
--------------
1. YouTube Data API Key
2. YouTube Video Link

How to Obtain a YouTube Data API Key:
-------------------------------------
1. Go to the Google Developers Console: https://console.developers.google.com/
2. Sign in with your Google account.
3. Create a new project by clicking on the "Select a project" dropdown at the top, then click "New Project."
4. Name your project and click "Create."
5. Once your project is created, select it from the project dropdown.
6. In the left-hand menu, navigate to "APIs & Services" > "Library."
7. Search for "YouTube Data API v3" and select it.
8. Click the "Enable" button.
9. Navigate to "APIs & Services" > "Credentials."
10. Click "Create Credentials" and select "API Key."
11. Your API key will be created and displayed. Copy this key, as you will need it to run the program.

Usage:
------
1. Ensure you have the YouTube Data API Key and the YouTube video link.
2. Run the executable.
3. Enter the required information when prompted:
   - YouTube Data API Key
   - YouTube Video Link
4. The program will process the video and scrape comments, replies, and user information.
5. Two Excel files will be generated in the same directory as the executable:
   - `<VIDEO_ID>_comments.xlsx`: Contains all comments and replies.
   - `<VIDEO_ID>_users_info.xlsx`: Contains information about the users who commented.

Output Files:
-------------
- `<VIDEO_ID>_comments.xlsx`: This file includes the following columns:
  - `videoId`: The ID of the video the comment is associated with.
  - `textOriginal`: The original text of the comment.
  - `authorDisplayName`: The display name of the comment's author.
  - `authorChannelUrl`: The URL of the author's YouTube channel.
  - `likeCount`: The number of likes the comment has received.
  - `publishedAt`: The date and time when the comment was originally published.
  - `updatedAt`: The date and time when the comment was last updated.
  - `id`: The unique ID of the comment.
  - `totalReplyCount`: The total number of replies to the comment.
  - `parentId`: The ID of the parent comment if this comment is a reply.

- `<VIDEO_ID>_users_info.xlsx`: This file includes the following columns:
  - `id`: The unique ID of the user's channel.
  - `channelDisplayName`: The display name of the user's channel.
  - `channelURL`: The URL of the user's YouTube channel.
  - `title`: The title of the user's YouTube channel.
  - `description`: The description of the user's YouTube channel.
  - `joinedAt`: The date and time when the user joined YouTube.
  - `viewCount`: The total number of views on the user's channel.
  - `subscriberCount`: The total number of subscribers to the user's channel.
  - `videoCount`: The total number of videos uploaded to the user's channel.

Notes:
------
- Ensure that your internet connection is stable during the scraping process.
- The program might take some time to run depending on the number of comments and replies on the video.

Future Features:
------
1. Modern & Improved UI
2. Multiple API Key handling. Once an API Key reached its daily limit, switch to next key.
3. Output file names to contain YT video title instead of video id.
4. Customisable outputs. (Chose columns and column order, create templates, etc.)

Contact:
--------
For any issues or questions, please contact me.

