# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive PyPI publishing guide (PUBLISHING_GUIDE.md)
- Modern pyproject.toml configuration for better package management
- Package build validation script (test_build.py)
- Support for PyPI API token authentication in GitHub Actions
- Trusted publishing support for enhanced security

### Fixed
- Fixed PyPI publishing issues in GitHub Actions workflow
- Resolved authentication problems with PyPI uploads
- Fixed configuration conflicts between setup.py and pyproject.toml
- Updated GitHub Actions to use latest versions (checkout@v4, setup-python@v5)
- Added package validation step before publishing

### Changed
- Modernized GitHub Actions release workflow
- Simplified setup.py to use pyproject.toml configuration
- Enhanced error handling in release process
- Added fallback authentication method for PyPI publishing
- Improved package metadata and keywords for better discoverability

### Security
- Migrated from username/password to API token authentication for PyPI
- Added trusted publishing support for GitHub Actions

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