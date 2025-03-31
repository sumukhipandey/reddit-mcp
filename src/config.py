# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.environ.get("REDDIT_USER_AGENT", "Reddit MCP v1.0")
REDDIT_USERNAME = os.environ.get("REDDIT_USERNAME", None)
REDDIT_PASSWORD = os.environ.get("REDDIT_PASSWORD", None)

# MCP server configuration
SERVER_NAME = "Reddit Explorer"