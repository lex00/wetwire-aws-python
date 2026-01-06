# wetwire-aws

[![CI](https://github.com/lex00/wetwire-aws-python/actions/workflows/ci.yml/badge.svg)](https://github.com/lex00/wetwire-aws-python/actions/workflows/ci.yml)
[![PyPI Version](https://img.shields.io/pypi/v/wetwire-aws.svg)](https://pypi.org/project/wetwire-aws/)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AWS CloudFormation synthesis using Python dataclasses.

## Installation

```bash
uv add wetwire-aws
```

## Quick Example

```python
from wetwire_aws.loader import setup_resources
setup_resources(__file__, __name__, globals())
```

```python
# infra.py
from . import *

class MyBucket(s3.Bucket):
    bucket_name = "my-data"

class MyFunction(lambda_.Function):
    function_name = "processor"
    runtime = lambda_.Runtime.PYTHON3_12
    role = MyRole.Arn  # Type-safe reference with IDE autocomplete
```

```bash
wetwire-aws build --module myapp > template.json
```

## Serverless (SAM) Support

Build serverless applications with type-safe SAM resources:

```python
from . import *

class ProcessorFunction(serverless.Function):
    function_name = "processor"
    runtime = serverless.Runtime.PYTHON3_12
    handler = "app.handler"
    code_uri = "./src"
```

All 9 SAM resource types supported: `Function`, `Api`, `HttpApi`, `SimpleTable`, `LayerVersion`, `StateMachine`, `Application`, `Connector`, `GraphQLApi`.

## AI-Assisted Design

Create infrastructure interactively with AI:

```bash
# Interactive design session
wetwire-aws design "Create an encrypted S3 bucket"

# Automated testing with personas
wetwire-aws test --persona beginner "Create a Lambda function"
```

Requires `wetwire-core` and `ANTHROPIC_API_KEY`. See [CLI Reference](docs/CLI.md#design) for details.

## Documentation

- [Quick Start](docs/QUICK_START.md) - Full tutorial
- [CLI Reference](docs/CLI.md) - All commands
- [Comparison](docs/COMPARISON.md) - vs CDK, Terraform

## Development

```bash
git clone https://github.com/lex00/wetwire-aws-python.git
cd wetwire-aws-python
uv sync
./scripts/dev-setup.sh    # First-time setup (generate resources)
./scripts/regenerate.sh   # Re-generate resources (after spec updates)
uv run pytest             # Run tests
```

See [Developer Guide](docs/DEVELOPERS.md) for details.

## License

MIT - See [LICENSE](LICENSE) for details. Third-party attributions in [NOTICE](NOTICE).
