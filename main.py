# main.py
from src.server import mcp

# Import all resources, tools, and prompts
from src.resources import subreddit

if __name__ == "__main__":
    print("Starting Reddit MCP server...")
    mcp.run()