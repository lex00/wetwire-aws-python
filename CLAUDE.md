# wetwire-aws (Python)

Generate CloudFormation templates from Python dataclass declarations.

## Syntax Principles

All resources are Python classes inheriting from generated resource types. No function calls, no registration.

### Resource Declaration

Resources are declared as classes inheriting from the generated type:

```python
from . import *

class MyBucket(s3.Bucket):
    bucket_name = "my-data"
```

### Direct References

Reference other resources directly by class name:

```python
class MyFunction(lambda_.Function):
    role = MyRole.Arn  # GetAtt via attribute access
    environment = MyEnv
```

### Nested Types

Extract nested configurations to separate classes:

```python
class MyEnv(lambda_.Environment):
    variables = MyVariables

class MyVariables:
    BUCKET = MyBucket  # Direct reference
```

### Type-Safe Constants

Use typed enum constants instead of strings:

```python
class MyFunction(lambda_.Function):
    runtime = lambda_.Runtime.PYTHON3_12  # Not "python3.12"
```

## Package Structure

```
wetwire_aws/
├── resources/         # Generated resource types (263 services)
│   ├── s3/           # S3 resources (Bucket, AccessPoint, etc.)
│   ├── lambda_/      # Lambda resources (Function, etc.)
│   ├── iam/          # IAM resources (Role, Policy, etc.)
│   └── serverless/   # SAM resources (Function, Api, etc.)
├── intrinsics/       # Ref, GetAtt, Sub, Join, etc.
├── template.py       # CloudFormation template builder
├── loader.py         # Resource discovery
├── linter/           # 20 lint rules (WAW001-WAW020)
└── importer/         # YAML to Python conversion
```

## Lint Rules (WAW001-WAW020)

Key rules enforcing declarative patterns:

- **WAW001-004**: Use typed constants (parameters, pseudo-params, enums, intrinsics)
- **WAW006**: No-parens references (use `MyRole.Arn` not `MyRole().Arn`)
- **WAW010**: Split large files (>15 resources per file)
- **WAW013**: Use wrapper classes, not inline constructors
- **WAW019-020**: Avoid explicit `Ref()` and `GetAtt()` — use direct references

## Key Principles

1. **Class inheritance** — Resources inherit from generated types
2. **Flat declarations** — Extract nested configs to named classes
3. **Direct references** — Use class names, not function calls
4. **Typed constants** — Use enums for runtime, regions, etc.

## Build

```bash
wetwire-aws build --module myapp > template.json
```

## Project Structure

```
my-stack/
├── __init__.py        # setup_resources() call
├── network.py         # VPC, subnets, security groups
├── compute.py         # EC2, Lambda, containers
├── storage.py         # S3, EFS, databases
└── security.py        # IAM roles, policies
```
