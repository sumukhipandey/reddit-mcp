# reddit-mcp: Model Context Protocol for Reddit

A Model Context Protocol (MCP) server for accessing Reddit data and functionality through Large Language Models like Claude.

## Phase 1: Core Functionality

The current phase implements:

- Basic project structure and configuration
- Reddit API client integration
- Subreddit browsing capabilities

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

4. Copy the example environment file and update it with your Reddit API credentials:

```bash
cp .env.example .env
# Edit .env file with your credentials
```

### Running the Server

To run the MCP server:

```bash
python main.py
```

For development mode with the MCP Inspector:

```bash
mcp dev main.py
```

To install the server in Claude Desktop:

```bash
mcp install main.py
```

## Available Resources

### Subreddit Information

- `subreddit://{subreddit_name}` - Get information about a subreddit
- `subreddit://{subreddit_name}/hot` - Get hot posts from a subreddit

## Project Structure

```
reddit-mcp/
├── README.md              # This file
├── requirements.txt       # Project dependencies
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore file
├── main.py                # Main entry point
└── src/                   # Source code
    ├── __init__.py
    ├── config.py          # Configuration management
    ├── reddit_client.py   # Reddit API client wrapper
    ├── server.py          # MCP server initialization
    ├── resources/         # MCP resources
    │   ├── __init__.py
    │   └── subreddit.py   # Subreddit resources
    └── utils/             # Utility functions
        ├── __init__.py
        └── formatting.py  # Output formatting helpers
```

## Upcoming Features

The following features are planned for future phases:

- Post and comment viewing
- Search functionality
- User profile exploration
- Trend analysis
- Response caching
- Advanced prompts for content analysis

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
