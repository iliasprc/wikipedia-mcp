# PyPI Publishing Guide for Wikipedia MCP

This guide will help you set up automated PyPI publishing for the Wikipedia MCP server.

## Prerequisites

1. **PyPI Account**: Create an account at [pypi.org](https://pypi.org/account/register/)
2. **TestPyPI Account**: Create an account at [test.pypi.org](https://test.pypi.org/account/register/) for testing
3. **GitHub Repository**: Your code should be in a GitHub repository

## Step 1: Generate PyPI API Tokens

### For PyPI (Production)
1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Scroll down to "API tokens"
3. Click "Add API token"
4. Give it a name like "wikipedia-mcp-github-actions"
5. Set scope to "Entire account" (you can limit this to specific projects later)
6. Copy the token (starts with `pypi-`)

### For TestPyPI (Testing)
1. Go to [TestPyPI Account Settings](https://test.pypi.org/manage/account/)
2. Follow the same steps as above
3. Copy the token (starts with `pypi-`)

## Step 2: Add GitHub Secrets

1. Go to your GitHub repository
2. Click on "Settings" tab
3. In the left sidebar, click "Secrets and variables" → "Actions"
4. Click "New repository secret"
5. Add these secrets:

   - **Name**: `PYPI_API_TOKEN`
     **Value**: Your PyPI API token (the one that starts with `pypi-`)

   - **Name**: `TEST_PYPI_API_TOKEN`
     **Value**: Your TestPyPI API token

   - **Name**: `PYPI_USERNAME` (fallback)
     **Value**: `__token__`

   - **Name**: `PYPI_PASSWORD` (fallback)
     **Value**: Your PyPI API token

## Step 3: Test Local Build

Before using GitHub Actions, test the build locally:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Check the package
twine check dist/*

# Test upload to TestPyPI (optional)
twine upload --repository testpypi dist/* --username __token__ --password YOUR_TEST_PYPI_TOKEN
```

## Step 4: Manual PyPI Upload (Alternative)

If GitHub Actions isn't working, you can upload manually:

```bash
# Build the package
python -m build

# Upload to PyPI
twine upload dist/* --username __token__ --password YOUR_PYPI_TOKEN
```

## Step 5: Using GitHub Actions

The updated workflow in `.github/workflows/release.yml` now supports:

1. **Modern PyPI token authentication**
2. **Trusted publishing** (recommended by PyPI)
3. **Fallback to username/password** if token fails
4. **Package validation** before upload

To trigger a release:

1. Go to your GitHub repository
2. Click "Actions" tab
3. Click "Release Wikipedia MCP" workflow
4. Click "Run workflow"
5. Enter the version number (e.g., "1.5.0")
6. Choose if it's a pre-release
7. Click "Run workflow"

## Step 6: Verify Publication

After successful upload:

1. Check [PyPI](https://pypi.org/project/wikipedia-mcp/) for your package
2. Test installation: `pip install wikipedia-mcp`
3. Test the uvx command: `uvx wikipedia-mcp`

## Troubleshooting Common Issues

### 1. "403 Forbidden" Error
- **Cause**: Invalid credentials or insufficient permissions
- **Solution**: Regenerate API token and update GitHub secrets

### 2. "400 Bad Request" Error
- **Cause**: Package name already exists or invalid metadata
- **Solution**: Check if package name is available, validate setup.py/pyproject.toml

### 3. "422 Unprocessable Entity" Error
- **Cause**: Version already exists on PyPI
- **Solution**: Increment version number in setup.py and pyproject.toml

### 4. "500 Internal Server Error"
- **Cause**: Temporary PyPI server issues
- **Solution**: Wait and retry, or check [PyPI status](https://status.python.org/)

### 5. Package Not Found After Upload
- **Cause**: PyPI indexing delay or upload failure
- **Solution**: Wait 5-10 minutes, check PyPI directly

## Best Practices

1. **Always test on TestPyPI first**
2. **Use semantic versioning** (e.g., 1.5.0, 1.5.1)
3. **Update CHANGELOG.md** before releases
4. **Tag releases** in Git
5. **Use API tokens** instead of passwords
6. **Keep secrets secure** and rotate them regularly

## Package Installation Commands

After publishing, users can install your package with:

```bash
# Using pip
pip install wikipedia-mcp

# Using uvx (recommended for MCP servers)
uvx wikipedia-mcp

# Using pipx
pipx install wikipedia-mcp
```

## MCP Configuration

Users can then add to their MCP configuration:

```json
{
  "wikipedia": {
    "command": "uvx",
    "args": ["wikipedia-mcp"]
  }
}
```

This addresses the original issue from [GitHub Issue #5](https://github.com/Rudra-ravi/wikipedia-mcp/issues/5). 