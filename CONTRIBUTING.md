# Contributing to wetwire-aws

Thank you for your interest in contributing to wetwire-aws! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- **Python 3.11+** (required)
- **uv** (recommended package manager)
- **git** (version control)

### Getting Started

```bash
# Clone the repository
git clone https://github.com/lex00/wetwire-aws-python.git
cd wetwire-aws-python

# Install dependencies
uv sync

# First-time setup (generates resource types)
./scripts/dev-setup.sh

# Run tests to verify setup
uv run pytest
```

### Optional Dependencies

```bash
# Install codegen dependencies (for regenerating resources)
uv sync --extra codegen

# Install agent dependencies (for AI features)
uv sync --extra agent
```

## Code Style

### Formatting and Linting

We use [ruff](https://docs.astral.sh/ruff/) for formatting and linting:

```bash
# Format code
uv run ruff format src/ tests/

# Check for linting issues
uv run ruff check src/ tests/

# Auto-fix linting issues
uv run ruff check --fix src/ tests/
```

### Type Checking

Type hints are required for all public APIs:

```bash
uv run ty check src/wetwire_aws/
```

### Guidelines

- Follow PEP 8 style conventions
- Use type hints for all public functions and methods
- Keep lines under 88 characters (enforced by ruff)
- Write docstrings for public APIs

## Pull Request Process

### 1. Create a Branch

```bash
git checkout -b feature/my-feature
# or
git checkout -b fix/my-bugfix
```

### 2. Make Changes

- Write or update tests for your changes
- Ensure all tests pass: `uv run pytest`
- Run linting: `uv run ruff check`
- Run type checking: `uv run ty check src/wetwire_aws/`

### 3. Commit Your Changes

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: Add support for new resource type
fix: Correct template serialization bug
docs: Update installation instructions
test: Add tests for intrinsic functions
refactor: Simplify loader logic
chore: Update dependencies
```

### 4. Push and Create PR

```bash
git push origin feature/my-feature
```

Then open a Pull Request on GitHub. Include:
- A clear description of the changes
- Any related issue numbers (e.g., "Fixes #123")
- Screenshots if applicable (for CLI changes)

### 5. Address Review Feedback

- Respond to review comments
- Push additional commits as needed
- Keep commits focused and atomic

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage report
uv run pytest --cov=wetwire_aws --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_template.py -v

# Run specific test
uv run pytest tests/test_template.py::test_from_registry -v
```

## Code Generation

If you need to regenerate resource types:

```bash
# Full regeneration
./scripts/regenerate.sh

# Individual stages
uv run python -m codegen.fetch
uv run python -m codegen.parse
uv run python -m codegen.generate
```

See [docs/CODEGEN.md](docs/CODEGEN.md) for details.

## Questions?

- Check the [Developer Guide](docs/DEVELOPERS.md) for architecture details
- Open an issue for questions or discussions
- See [FAQ](docs/FAQ.md) for common questions
