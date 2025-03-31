# src/prompts/exploration.py
from src.server import mcp
from mcp.server.fastmcp.prompts import base

@mcp.prompt()
def explore_subreddit(subreddit: str) -> str:
    """Prompt to explore a specific subreddit"""
    return f"""I'd like to explore the r/{subreddit} subreddit. 
Please tell me about this community and show me some of the top posts right now.
If it's appropriate, please also suggest similar subreddits I might be interested in."""