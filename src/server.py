# src/server.py
from mcp.server.fastmcp import FastMCP
from src.config import SERVER_NAME

# Create and configure MCP server
mcp = FastMCP(SERVER_NAME)