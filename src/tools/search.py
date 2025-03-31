# src/tools/search.py
from typing import Optional
from src.server import mcp
from src.reddit_client import reddit
from src.utils.formatting import format_post_summary

@mcp.tool()
def search_reddit(query: str, subreddit: Optional[str] = None, sort: str = "relevance", time_filter: str = "all", limit: int = 10) -> str:
    """
    Search Reddit posts.
    
    Args:
        query: Search query
        subreddit: Optional subreddit to search within (None for all Reddit)
        sort: Sort method ('relevance', 'hot', 'top', 'new', 'comments')
        time_filter: Time filter ('all', 'day', 'hour', 'month', 'week', 'year')
        limit: Maximum number of results to return
    """
    if subreddit:
        results = reddit.subreddit(subreddit).search(query, sort=sort, time_filter=time_filter, limit=limit)
    else:
        results = reddit.subreddit("all").search(query, sort=sort, time_filter=time_filter, limit=limit)
    
    posts = []
    for post in results:
        posts.append(format_post_summary(post))
    
    if not posts:
        return "No results found."
    
    return "\n".join(posts)