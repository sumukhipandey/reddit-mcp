#!/usr/bin/env python
import os
import sys
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("reddit-mcp")

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)
logger.info(f"Added {project_dir} to Python path")

# Load environment variables from .env file
load_dotenv()

try:
    logger.info(f"Python executable: {sys.executable}")
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Current directory: {os.getcwd()}")
    
    # Import required modules
    logger.info("Importing modules...")
    from src.server import mcp
    from src.resources import subreddit, post, user
    from src.tools import search, trending
    
    # Run the MCP server
    logger.info("Starting Reddit MCP server...")
    mcp.run()
except Exception as e:
    logger.error(f"Error starting MCP server: {str(e)}", exc_info=True)
    sys.exit(1)