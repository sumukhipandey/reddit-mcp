# src/resources/subreddit.py
from src.server import mcp
from src.reddit_client import reddit
from src.utils.formatting import format_subreddit

@mcp.resource("subreddit://{subreddit_name}")
def get_subreddit_info(subreddit_name: str) -> str:
    """Get information about a subreddit"""
    subreddit = reddit.subreddit(subreddit_name)
    return format_subreddit(subreddit)

@mcp.resource("subreddit://{subreddit_name}/hot")
def get_hot_posts(subreddit_name: str) -> str:
    """Get hot posts from a subreddit"""
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.hot(limit=10):
        posts.append(format_post_summary(post))
    return "\n".join(posts)