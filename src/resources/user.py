# src/resources/user.py
from src.server import mcp
from src.reddit_client import reddit
from src.utils.formatting import format_user_profile, format_post_summary

@mcp.resource("user://{username}")
def get_user_profile(username: str) -> str:
    """Get a Reddit user's profile information"""
    user = reddit.redditor(username)
    return format_user_profile(user)

@mcp.resource("user://{username}/posts")
def get_user_posts(username: str) -> str:
    """Get a Reddit user's recent posts"""
    user = reddit.redditor(username)
    limit = 10
    posts = []
    
    for post in user.submissions.new(limit=limit):
        posts.append(format_post_summary(post))
    
    if not posts:
        return f"User u/{username} has no recent posts."
    
    return "\n".join(posts)