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

def format_post(post):
    """Format detailed post information"""
    return f"""Title: {post.title}
ID: {post.id}
Author: u/{post.author.name if post.author else '[deleted]'}
Score: {post.score:,}
Comments: {post.num_comments:,}
URL: {post.url}
Content: {post.selftext if post.selftext else '[No text content]'}
Created: {post.created_utc}
Upvote Ratio: {post.upvote_ratio:.2f}
NSFW: {post.over_18}
"""

def format_comment(comment):
    """Format comment information"""
    return f"""Author: u/{comment.author.name if comment.author else '[deleted]'}
Score: {comment.score:,}
Content: {comment.body}
Created: {comment.created_utc}
ID: {comment.id}
---------"""

def format_user_profile(user):
    """Format user profile information"""
    try:
        return f"""Username: u/{user.name}
Comment Karma: {user.comment_karma:,}
Post Karma: {user.link_karma:,}
Created: {user.created_utc}
Is Mod: {user.is_mod if hasattr(user, 'is_mod') else 'Unknown'}
Is Gold: {user.is_gold if hasattr(user, 'is_gold') else 'Unknown'}
"""
    except Exception as e:
        return f"Error retrieving user profile: {str(e)}"