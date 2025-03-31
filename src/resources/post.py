# src/resources/post.py
from src.server import mcp
from src.reddit_client import reddit
from src.utils.formatting import format_post, format_comment

@mcp.resource("post://{post_id}")
def get_post(post_id: str) -> str:
    """Get a specific Reddit post by ID"""
    post = reddit.submission(id=post_id)
    return format_post(post)

@mcp.resource("post://{post_id}/comments")
def get_post_comments(post_id: str) -> str:
    """Get comments from a specific Reddit post"""
    post = reddit.submission(id=post_id)
    post.comments.replace_more(limit=0)
    
    comments = []
    for comment in post.comments:
        comments.append(format_comment(comment))
    
    return "\n".join(comments)