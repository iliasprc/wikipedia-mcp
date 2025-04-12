# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2024-04-12

### Added
- GitHub Actions workflows for automated testing and releases
- Comprehensive release documentation in docs/RELEASE_PROCESS.md
- Testing documentation in docs/TESTING.md
- Example script for MCP client interaction

### Fixed
- Fixed MCP transport issues in server implementation
- Corrected documentation for MCP protocol usage
- Updated README with accurate MCP protocol information

### Changed
- Improved error handling in Wikipedia client
- Enhanced documentation on using the MCP server with Claude Desktop
- Updated project metadata in setup.py

## [1.0.1] - 2024-03-15

### Added
- Added support for related topics functionality
- Implemented section extraction for Wikipedia articles
- Added logging for better debugging

### Fixed
- Fixed article retrieval for titles with special characters
- Improved error handling for API calls

## [1.0.0] - 2024-02-20

### Added
- Initial release
- Core MCP server implementation
- Wikipedia API client integration
- Basic search, summary, and article retrieval functionality
- Configuration for Claude Desktop integration 