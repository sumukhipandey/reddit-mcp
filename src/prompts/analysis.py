# src/prompts/analysis.py
from src.server import mcp
from mcp.server.fastmcp.prompts import base

@mcp.prompt()
def analyze_post(post_id: str) -> list[base.Message]:
    """Analyze a Reddit post with comments"""
    return [
        base.UserMessage(f"Can you analyze this Reddit post (ID: {post_id}) for me?"),
        base.UserMessage("Please summarize the main points, the community's reaction in the comments, and any interesting insights or controversies that stand out."),
        base.AssistantMessage("I'll analyze that Reddit post for you. Let me gather the post content and comments...")
    ]