# Developer Guide

Comprehensive guide for developers working on wetwire-aws.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Code Generation](#code-generation)
- [Contributing](#contributing)

---

## Development Setup

### Prerequisites

- **Python 3.11+** (required)
- **uv** (recommended package manager)
- **git** (version control)

### Clone and Setup

```bash
# Clone repository
git clone https://github.com/lex00/wetwire.git
cd wetwire/python/packages/wetwire-aws

# Install dependencies (creates .venv automatically)
uv sync

# Install codegen dependencies
uv sync --extra codegen

# Verify installation
uv run pytest tests/ -v
```

---

## Project Structure

```
wetwire-aws/
├── src/wetwire_aws/           # Source code
│   ├── __init__.py            # Package entry point
│   ├── base.py                # CloudFormationResource base class
│   ├── decorator.py           # @wetwire_aws decorator
│   ├── template.py            # CloudFormationTemplate class
│   ├── cli.py                 # CLI commands
│   ├── intrinsics/            # Intrinsic functions
│   │   ├── functions.py       # Ref, GetAtt, Sub, Join, etc.
│   │   ├── pseudo.py          # AWS pseudo-parameters
│   │   └── refs.py            # ref(), get_att(), dataclass-dsl integration
│   └── resources/             # Generated AWS resources (263 services)
│       ├── s3/__init__.py     # S3 resources
│       ├── ec2/__init__.py    # EC2 resources
│       ├── lambda_/__init__.py # Lambda resources
│       └── ...                # All other AWS services
├── codegen/                   # Code generation tools
│   ├── config.py              # Version configuration
│   ├── fetch.py               # Download CloudFormation spec
│   ├── parse.py               # Parse spec into intermediate format
│   ├── generate.py            # Generate Python classes
│   ├── extract_enums.py       # Extract botocore enums
│   └── intermediate.py        # Intermediate representation
├── specs/                     # CloudFormation spec (committed)
├── tests/                     # Test suite
├── docs/                      # Documentation
├── scripts/                   # Automation scripts
└── pyproject.toml             # Package configuration
```

---

## Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# With coverage
uv run pytest tests/ --cov=wetwire_aws --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_template.py -v

# Run specific test
uv run pytest tests/test_template.py::test_from_registry -v
```

---

## Code Generation

See [CODEGEN.md](CODEGEN.md) for comprehensive code generation documentation.

**Quick commands:**

```bash
# Full regeneration
./scripts/regenerate.sh

# Individual stages
uv run python -m codegen.fetch
uv run python -m codegen.parse
uv run python -m codegen.generate
```

---

## Contributing

### Code Style

- **Formatting**: Use `ruff format`
- **Linting**: Use `ruff check`
- **Type Hints**: Required for all public APIs

```bash
# Format code
uv run ruff format src/ tests/

# Lint
uv run ruff check src/ tests/

# Type check
uv run ty check src/wetwire_aws/
```

### Commit Messages

Follow conventional commits:

```
feat: Add support for EC2 resources
fix: Correct S3 bucket serialization
docs: Update installation instructions
test: Add tests for dataclass-dsl integration
chore: Update dependencies
```

### Pull Request Process

1. Create feature branch: `git checkout -b feature/my-feature`
2. Make changes with tests
3. Run tests: `uv run pytest tests/`
4. Commit with clear messages
5. Push and open Pull Request
6. Address review comments

---

## See Also

- [Quick Start](QUICK_START.md) - Getting started
- [CLI Reference](CLI.md) - CLI commands
- [Internals](INTERNALS.md) - Architecture details
- [Versioning](VERSIONING.md) - Version management
