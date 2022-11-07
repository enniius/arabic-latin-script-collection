# this function uses youtube api to get all videos of a channel and exports them to a csv file

import csv
import googleapiclient.discovery
import googleapiclient.errors
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = config['youtube']['API_KEY']
CHANNEL_ID = 'UCyspqvfIMfwofk2MpBK9PEg'
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)


# returns 50 channel videos ids.

def get_channel_videos(channel_id):
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        type="video",
        maxResults=50
    )

    response = request.execute()
    videos_ids = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        videos_ids.append(video_id)
    return videos_ids

# for input video_id return 100 comments from that video
# as a CommentThreads Resource, its a json file


def get_video_comments(video_id):
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=100
    ).execute()
    comments_texts = []
    for item in results['items']:  # type - comments Resource
        comment = item["snippet"]["topLevelComment"]
        comment_text = comment["snippet"]["textDisplay"]  # type - String
        comments_texts.append(comment_text)
    return comments_texts

# for a list of video_ids, return the comments of each video


def get_videos_comments(videos_ids):
    videos_comments = []
    for video_id in videos_ids:
        comments = get_video_comments(video_id)
        videos_comments.append(comments)
    return videos_comments

# write the list of comments to a csv file named after the channel id


def write_to_csv(comments):
    with open(CHANNEL_ID + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(comments)


if __name__ == "__main__":
    videos_ids = get_channel_videos(CHANNEL_ID)
    videos_comments = get_videos_comments(videos_ids)
    write_to_csv(videos_comments)
