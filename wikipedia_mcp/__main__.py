"""
Main entry point for the Wikipedia MCP server.
"""

import argparse
import logging
import os
from dotenv import load_dotenv

from wikipedia_mcp.server import create_server

# Load environment variables from .env file if it exists
load_dotenv()

def main():
    """Run the Wikipedia MCP server."""
    parser = argparse.ArgumentParser(description="Wikipedia MCP Server")
    parser.add_argument(
        "--host", 
        type=str, 
        default="127.0.0.1", 
        help="Host to bind the server to"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=0, 
        help="Port to bind the server to (0 for auto-selection)"
    )
    parser.add_argument(
        "--log-level", 
        type=str, 
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level"
    )
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create and start the server
    server = create_server()
    server.run()

if __name__ == "__main__":
    main() 