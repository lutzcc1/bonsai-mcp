from typing import Any
import requests
import json
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("server")

# Constants
USER_AGENT = "bonsai-mcp/1.0"
INDEX_NAME = os.environ.get('INDEX_NAME')
BONSAI_URL = os.environ.get('BONSAI_URL')

def make_search_request(query: str) -> Any:
    """Make a search request to Bonsai's cluster."""
    response = requests.get(
        f"{BONSAI_URL}/{INDEX_NAME}/_search?q={query}",
        headers={"User-Agent": USER_AGENT},
    )
    return response.json()

def format_response(response: Any) -> str:
    """Format the response from the Bonsai's cluster"""
    # If response is empty or None
    if not response:
        return "No response received"

    # For search results (contains hits)
    if "hits" in response:
        hits = response["hits"]["hits"]
        if not hits:
            return "No search results found"
        else:
            return json.dumps(response, indent=2)
    else:
        return str(response)

@mcp.tool()
def search(query: str) -> str:
    """Search for products in Bonsai's cluster"""
    response = make_search_request(query)
    return format_response(response)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')