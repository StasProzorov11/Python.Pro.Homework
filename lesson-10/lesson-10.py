import datetime
from abc import ABC, abstractmethod
from typing import List


class SocialChannel(ABC):
    def __init__(self, channel_type: str, followers: int):
        self.channel_type = channel_type
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str, timestamp: int) -> None:
        pass


class YouTubeChannel(SocialChannel):
    def post_message(self, message: str, timestamp: int) -> None:
        current_time_str = datetime.datetime.fromtimestamp(timestamp).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        print(
            f"Posted on YouTube ({self.followers} followers): {message} (posted at: {current_time_str})"
        )


class FacebookChannel(SocialChannel):
    def post_message(self, message: str, timestamp: int) -> None:
        current_time_str = datetime.datetime.fromtimestamp(timestamp).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        print(
            f"Posted on Facebook ({self.followers} followers): {message} (posted at: {current_time_str})"
        )


class TwitterChannel(SocialChannel):
    def post_message(self, message: str, timestamp: int) -> None:
        current_time_str = datetime.datetime.fromtimestamp(timestamp).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        print(
            f"Posted on Twitter ({self.followers} followers): {message} (posted at: {current_time_str})"
        )


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


def post_a_message(channel: SocialChannel, message: str, timestamp: int) -> None:
    channel.post_message(message, timestamp)


def process_schedule(posts: List[Post], channels: List[SocialChannel]) -> None:
    current_time = datetime.datetime.now().timestamp()
    for post in posts:
        if post.timestamp <= current_time:
            for channel in channels:
                post_a_message(channel, post.message, post.timestamp)


messages = [
    Post("Hello, YouTube!", 1633112400),
    Post("Hello, Facebook!", 1633123200),
    Post("Hello, Twitter!", 1633126800),
]

channels = [
    YouTubeChannel("YouTube", 10000),
    FacebookChannel("Facebook", 5000),
    TwitterChannel("Twitter", 2000),
]

process_schedule(messages, channels)
