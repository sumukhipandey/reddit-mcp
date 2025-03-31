# In src/server.py
import logging
import importlib
from mcp.server.fastmcp import FastMCP
from src.config import SERVER_NAME

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create and configure MCP server
mcp = FastMCP(
    SERVER_NAME,
    resources=[
        "src.resources.post",
        "src.resources.user",
        "src.resources.subreddit"
    ]
)
logger.debug(f"MCP Server '{SERVER_NAME}' initialized")

