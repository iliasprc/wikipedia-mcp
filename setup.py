from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wikipedia-mcp",
    version="0.1.0",
    author="Ravikumar E",
    author_email="ravikumar.dev@example.com",
    description="A Model Context Protocol server for Wikipedia integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rudra-ravi/wikipedia-mcp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "mcp>=0.1.0",
        "wikipedia-api>=0.5.0",
        "requests>=2.25.0",
        "python-dotenv>=0.19.0"
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=3.9",
            "mypy>=0.910"
        ]
    },
    entry_points={
        "console_scripts": [
            "wikipedia-mcp=wikipedia_mcp.cli:main",
        ],
    },
)