import os
import argparse
from dotenv import load_dotenv
from server import search

# Load environment variables from .env file
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Test the Bonsai MCP server")
    parser.add_argument("query", help="The search query")

    args = parser.parse_args()

    # Check if BONSAI_URL is set
    if not os.environ.get("BONSAI_URL"):
        print("Error: BONSAI_URL environment variable is not set")
        print("Please set it with: export BONSAI_URL='your-bonsai-url-here'")
        print("Or create a .env file with BONSAI_URL=your-bonsai-url-here")
        return 1

    print(f"Searching for: {args.query}")
    print("Fetching results...")

    try:
        # Call the search function
        results = search(args.query)

        # Print the results
        print("\nResults:")
        print(results)

        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())