# reddit-mcp: Model Context Protocol for Reddit

A Model Context Protocol (MCP) server for accessing Reddit data and functionality through Large Language Models like Claude.

## Features

- Subreddit browsing and information
- Hot posts viewing
- Post and comment viewing
- User profile exploration
- Reddit search functionality
- Trending topics analysis

## Setup

### Prerequisites

- Python 3.9+
- Reddit API credentials (obtain from [Reddit's app preferences](https://www.reddit.com/prefs/apps))

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/reddit-mcp.git
cd reddit-mcp
```

2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the MCP Server

To run the MCP server directly:

```bash
mcp dev main.py
```

## Claude Desktop Integration

To use this MCP with Claude Desktop:

1. Create a `claude_desktop_config.json` file in `~/Library/Application Support/Claude` with the following content:

```json
{
  "mcpServers": {
    "Reddit Explorer": {
      "command": "/path/to/your/reddit-mcp/venv/bin/python",
      "args": ["/path/to/your/reddit-mcp/direct_runner.py"],
      "env": {
        "REDDIT_CLIENT_ID": "your_client_id",
        "REDDIT_CLIENT_SECRET": "your_client_secret",
        "REDDIT_USERNAME": "your_username",
        "REDDIT_PASSWORD": "your_password",
        "REDDIT_USER_AGENT": "Reddit MCP v1.0 (by /u/your_username)"
      }
    }
  }
}
```

Replace the placeholder values with your actual Reddit API credentials and correct paths.

2. Open Claude Desktop
3. The Reddit Explorer tool should now be available
4. Start a new conversation and enable the tool

## Available Resources

### Subreddit Resources

- `subreddit://{subreddit_name}` - Get information about a subreddit
- `subreddit://{subreddit_name}/hot` - Get hot posts from a subreddit

### Post Resources

- `post://{post_id}` - Get a specific post by ID
- `post://{post_id}/comments` - Get comments from a post

### User Resources

- `user://{username}` - Get a user's profile information
- `user://{username}/posts` - Get a user's recent posts

### Tools

- `search_reddit` - Search for posts across Reddit
- `get_trending_topics` - Get trending topics on Reddit
