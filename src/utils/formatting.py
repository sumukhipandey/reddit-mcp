# src/utils/formatting.py
def format_subreddit(subreddit):
    """Format subreddit information for display"""
    return f"""Subreddit: r/{subreddit.display_name}
Description: {subreddit.description}
Subscribers: {subreddit.subscribers:,}
Created: {subreddit.created_utc}
NSFW: {subreddit.over18}
"""

def format_post_summary(post):
    """Format post summary information"""
    return f"""Title: {post.title}
ID: {post.id}
Author: u/{post.author.name if post.author else '[deleted]'}
Score: {post.score:,}
Comments: {post.num_comments:,}
URL: {post.url}
---------"""