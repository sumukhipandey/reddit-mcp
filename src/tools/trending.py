# src/tools/trending.py
from src.server import mcp
from src.reddit_client import reddit
from src.utils.formatting import format_post_summary

@mcp.tool()
def get_trending_topics() -> str:
    """Get currently trending topics across Reddit"""
    popular = reddit.subreddit("popular")
    topics = {}
    
    for post in popular.hot(limit=50):
        for topic in post.link_flair_text.split() if post.link_flair_text else []:
            if topic not in topics:
                topics[topic] = 0
            topics[topic] += 1
    
    sorted_topics = sorted(topics.items(), key=lambda x: x[1], reverse=True)
    return "\n".join([f"{topic}: {count} mentions" for topic, count in sorted_topics[:10]])