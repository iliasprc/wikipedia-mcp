FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Install the package in development mode
RUN pip install -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# MCP server uses stdio or SSE for communication
# Default to stdio transport (can be overridden with --transport option)
ENTRYPOINT ["wikipedia-mcp"]
CMD ["--log-level", "INFO"]

# Label for metadata
LABEL org.opencontainers.image.title="Wikipedia MCP Server"
LABEL org.opencontainers.image.description="Model Context Protocol server for Wikipedia integration"
LABEL org.opencontainers.image.url="https://github.com/rudra-ravi/wikipedia-mcp"
LABEL org.opencontainers.image.source="https://github.com/rudra-ravi/wikipedia-mcp"
LABEL org.opencontainers.image.version="1.0.2"
LABEL org.opencontainers.image.authors="Ravi Kumar <ravikumar@ravikumar-dev.me>"
LABEL org.opencontainers.image.licenses="MIT"
