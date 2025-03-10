# Bonsai Search MCP Server

A Model Context Protocol ([MCP](https://modelcontextprotocol.io/introduction)) server that provides search capabilities through Bonsai's Search cluster. This server enables Large Language Models (LLMs) like Claude to perform search queries on your indexed data.

## Features

- `search`: Execute search queries against your Bonsai elasticsearch cluster

## Prerequisites

- Python 3.10 or higher
- MCP SDK 1.2.0 or higher
- Bonsai cluster credentials
- Pre-existing indexed data .See [product_indexer](https://github.com/lutzcc1/products_indexer])

## Installation

1. Clone repository

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in your project root with the following:
```env
INDEX_NAME=your_index_name
BONSAI_URL=your_bonsai_cluster_url
```

## Usage

### Running the Server

```bash
python server.py
```

### Integrating with Claude for Desktop

1. Install the latest version of Claude for Desktop
2. Create or edit the Claude Desktop configuration file:
   - MacOS/Linux: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. Add the server configuration:
```json
{
  "mcpServers": {
    "bonsai-mcp": {
      "env": {
        "BONSAI_URL": "https://user:pass@your-cluster.bonsai.io",
        "INDEX_NAME": "index_name"
      },
      "command": "python", // use absolute path to the executable
      "args": [
        "/absolute/path/to/server.py"
      ]
    }
  }
}
```

4. Restart Claude for Desktop

### Available Tool

1. Search
   - Function: `search(query: str)`
   - Parameter: Search query string
   - Returns: Formatted JSON response from Bonsai elasticsearch cluster containing search results

## Testing the server
You can test the server functionality without running the full MCP server using the included test script:
```bash
python test_server.py "your search query here"
```

## Troubleshooting

### Logs Location
- Claude Desktop MCP logs: `~/Library/Logs/Claude/mcp.log`
- Server-specific logs: `~/Library/Logs/Claude/mcp-server-server.log`

### Common Issues

1. Server not showing up in Claude:
   - Verify `claude_desktop_config.json` syntax
   - Ensure paths are absolute
   - Restart Claude for Desktop

2. Search API Issues:
   - Verify environment variables are properly set
   - Check Bonsai cluster status
   - Verify index name exists
   - Check network connectivity to Bonsai cluster

## Environment Variables

| Variable | Description |
|----------|-------------|
| INDEX_NAME | The name of your Bonsai elasticsearch index |
| BONSAI_URL | The URL of your Bonsai elasticsearch cluster |
