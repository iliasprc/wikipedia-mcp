# Wikipedia MCP Server

A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs. Built by [Ravikumar E](https://github.com/Rudra-ravi), a Cybersecurity Analyst and Full-stack Developer specializing in Python development and AI integration.

## Project Status

🚧 **Under Development** 🚧

This project is currently in active development. The core functionality is being implemented, and we welcome contributions from the community.

### Implementation Roadmap

- [ ] Core MCP Server Setup
  - [ ] Basic server configuration
  - [ ] Request handling
  - [ ] Error handling and logging

- [ ] Wikipedia API Integration
  - [ ] Article search functionality
  - [ ] Content retrieval
  - [ ] Summary generation
  - [ ] Section extraction

- [ ] Advanced Features
  - [ ] Content caching
  - [ ] Rate limiting
  - [ ] Error recovery
  - [ ] API documentation

- [ ] Testing and Documentation
  - [ ] Unit tests
  - [ ] Integration tests
  - [ ] API documentation
  - [ ] Usage examples

## About the Author

I'm a Cybersecurity Analyst and Mobile Developer with expertise in:
- 🔒 SOC Analysis and Python Scripting
- 📱 Mobile Development (Flutter, Angular, Ionic)
- 🤖 AI Integration and Cloud Security
- 🛠️ IoT and Home Automation

## Planned Features

- Search Wikipedia articles
  - Full-text search
  - Category-based search
  - Language support
- Retrieve article summaries
  - Configurable length
  - Multiple formats (plain text, markdown)
- Get full article content
  - Section-wise retrieval
  - Format preservation
  - Image handling
- Extract article sections
  - Hierarchical section extraction
  - Custom section filtering
- Find links within articles
  - Internal links
  - External references
  - Category links
- Secure API implementation
  - Rate limiting
  - Authentication (optional)
  - HTTPS support
- Efficient data retrieval and caching
  - Local caching
  - Cache invalidation
  - Memory optimization

## Project Structure

```
wikipedia-mcp/
├── wikipedia_mcp/
│   ├── __init__.py
│   ├── cli.py
│   ├── server.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── handlers.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── wikipedia.py
│   │   └── cache.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_core.py
├── docs/
│   ├── API.md
│   └── DEVELOPMENT.md
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── setup.py
├── requirements.txt
└── .gitignore
```

## Installation

### Using pipx (Recommended)

```bash
# Install pipx if you don't have it
sudo apt install pipx
pipx ensurepath

# Install the Wikipedia MCP server
pipx install git+https://github.com/rudra-ravi/wikipedia-mcp.git
```

### Using a virtual environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the package
pip install git+https://github.com/rudra-ravi/wikipedia-mcp.git
```

## Usage

### Running the server

```bash
# If installed with pipx
wikipedia-mcp

# If installed in a virtual environment
source venv/bin/activate
wikipedia-mcp
```

### Configuration for Claude Desktop

Add the following to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "wikipedia": {
      "command": "wikipedia-mcp"
    }
  }
}
```

Location of the configuration file:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

### Example Prompts

Once the server is running and configured with Claude Desktop, you can use prompts like:

- "Tell me about quantum computing using the Wikipedia information."
- "Summarize the history of artificial intelligence based on Wikipedia."
- "What does Wikipedia say about climate change?"

## Development

The server is built using the Model Context Protocol (MCP) Python SDK and the Wikipedia API. It provides several resources and tools for interacting with Wikipedia content.

### Local Development

```bash
# Clone the repository
git clone https://github.com/rudra-ravi/wikipedia-mcp.git
cd wikipedia-mcp

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the package in development mode
pip install -e .

# Run the server
wikipedia-mcp
```

### Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

### Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=wikipedia_mcp tests/
```

## Connect with Me

- 🌐 Portfolio: [ravikumar-dev.me](https://ravikumar-dev.me)
- 📝 Blog: [Medium](https://medium.com/@Ravikumar-e)
- 💼 LinkedIn: [in/ravi-kumar-e](https://linkedin.com/in/ravi-kumar-e)
- 🐦 Twitter: [@Ravikumar_d3v](https://twitter.com/Ravikumar_d3v)

## License

MIT

## Acknowledgments

- [Model Context Protocol (MCP)](https://github.com/anthropics/anthropic-sdk-python)
- [Wikipedia API](https://wikipedia.readthedocs.io/en/latest/)
- [Claude Desktop](https://github.com/anthropics/claude-desktop)