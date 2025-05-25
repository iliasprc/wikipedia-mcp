#!/usr/bin/env python3
"""
Setup script for the Wikipedia MCP server.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wikipedia-mcp",
    version="1.0.2",
    author="Ravi Kumar",
    author_email="ravikumar@ravikumar-dev.me",
    description="A Model Context Protocol server for Wikipedia integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rudra-ravi/wikipedia-mcp",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "mcp==1.6.0",
        "wikipedia-api>=0.8.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "wikipedia-mcp=wikipedia_mcp.__main__:main",
        ],
    },
) 