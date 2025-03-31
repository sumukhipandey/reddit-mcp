# main.py
import sys
import os
import logging

# Configure logging to stderr for Claude desktop to capture
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

try:
    logger.info(f"Python executable: {sys.executable}")
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Current directory: {os.getcwd()}")
    
    from src.server import mcp
    logger.info("Server module imported successfully")
    
    # Import all resources, tools, and prompts
    from src.resources import subreddit, post, user
    logger.info("Resources imported successfully")
    
    from src.tools import search, trending
    logger.info("Tools imported successfully")
    
    from src.utils import formatting, caching
    logger.info("Utils imported successfully")
    
    if __name__ == "__main__":
        logger.info("Starting Reddit MCP server...")
        print("Starting Reddit MCP server...")
        mcp.run()
except Exception as e:
    logger.error(f"Error starting server: {str(e)}", exc_info=True)
    print(f"Error starting server: {str(e)}", file=sys.stderr)
    raise