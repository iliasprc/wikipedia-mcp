# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.5.2] - 2025-06-13

### Added
- Added command-line argument `--language` (`-l`) to `wikipedia-mcp` to specify the Wikipedia language for the server (e.g., `wikipedia-mcp --language ja`). This enhancement allows users to easily configure the language at startup. (Related to GitHub Issue #7).

### Changed
- **Docker Improvements**: Reverted Dockerfile to use proper MCP-compatible approach with PyPI installation
- **MCP Studio Compatibility**: Restored stdio transport for proper MCP client communication
- **Package Installation**: Now uses `pip install wikipedia-mcp` (recommended approach) instead of local file copying
- **Environment Configuration**: Restored proper Python environment variables for containerized deployment
- **Dependency Cleanup**: Removed unnecessary HTTP server dependencies (uvicorn) from requirements

### Fixed
- Fixed Docker container to work properly with MCP Studio and Claude Desktop
- Restored proper MCP protocol compliance using stdio transport instead of HTTP

## [1.5.1] - 2024-06-03

### Added
- Added an optional `language` parameter to `create_server` function in `wikipedia_mcp.server` to allow configuring the `WikipediaClient` with a specific language (e.g., "ja", "es"). Defaults to "en". (Fixes GitHub Issue #7).

### Changed
- N/A

### Fixed
- Corrected assertions in CLI tests (`tests/test_cli.py`) to accurately reflect the behavior of the `stdio` transport in a non-interactive subprocess environment. Tests now expect and verify `subprocess.TimeoutExpired` and check `stderr` for startup messages, ensuring robust testing of CLI startup and logging levels.

## [1.5.0] - 2025-05-31

### Added
- New tool: `summarize_article_for_query(title: str, query: str, max_length: Optional[int] = 250)` to get a summary of a Wikipedia article tailored to a specific query.
- New resource: `/summary/{title}/query` for the `summarize_article_for_query` tool.
- New tool: `summarize_article_section(title: str, section_title: str, max_length: Optional[int] = 150)` to get a summary of a specific section of a Wikipedia article.
- New resource: `/summary/{title}/section/{section_title}` for the `summarize_article_section` tool.
- New tool: `extract_key_facts(title: str, topic_within_article: Optional[str] = None, count: int = 5)` to extract key facts from a Wikipedia article.
- New resource: `/facts/{title}` for the `extract_key_facts` tool.

### Changed
- Updated project version to 1.5.0.

### Fixed
- N/A (New feature release)

## [1.4.4] - Previous Release Date
- ... (details of previous release, if you have them) ... 