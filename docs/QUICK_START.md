# Quick Start

Get started with `wetwire-aws` in 5 minutes.

## Installation

```bash
uv add wetwire-aws
```

## Your First Project

Create a package for your infrastructure:

```
myapp/
├── __init__.py
└── infra.py
```

**myapp/__init__.py:**
```python
from wetwire_aws.loader import setup_resources
setup_resources(__file__, __name__, globals())
```

**myapp/infra.py:**
```python
from . import *

class DataBucket(s3.Bucket):
    bucket_name = "my-data-bucket"
```

**Generate template:**
```bash
wetwire-aws build --module myapp > template.json
```

That's it. Resources auto-register when the module is loaded.

---

## Adding References

Reference other resources using the no-parens style:

**myapp/infra.py:**
```python
from . import *

class DataBucket(s3.Bucket):
    bucket_name = "data"

# Policy statement as wrapper class (flattened)
class LambdaAssumeRoleStatement(iam.PolicyStatement):
    effect = "Allow"
    principal = {"Service": "lambda.amazonaws.com"}
    action = "sts:AssumeRole"

class LambdaAssumeRolePolicy(iam.PolicyDocument):
    version = "2012-10-17"
    statement = [LambdaAssumeRoleStatement]

class ProcessorRole(iam.Role):
    role_name = "processor"
    assume_role_policy_document = LambdaAssumeRolePolicy

class ProcessorFunction(lambda_.Function):
    function_name = "processor"
    runtime = lambda_.Runtime.PYTHON3_12
    handler = "index.handler"
    role = ProcessorRole.Arn  # Reference to role's Arn attribute
```

---

## Type-Safe References

For introspectable references, use type annotations:

```python
from . import *  # Includes Attr, Ref from dataclass-dsl (Annotated is from typing)

class ProcessorRole(iam.Role):
    role_name = "processor"

class ProcessorFunction(lambda_.Function):
    function_name = "processor"
    runtime = lambda_.Runtime.PYTHON3_12
    # Type annotation enables dependency introspection
    role: Annotated[str, Attr(ProcessorRole, "Arn")] = None
```

The annotation `Annotated[str, Attr(ProcessorRole, "Arn")]` tells dataclass-dsl this resource depends on `ProcessorRole` and uses its `Arn` attribute. This enables:

- Static dependency analysis
- Topological sorting in templates
- Validation of reference targets

---

## Using the CLI

```bash
# Generate template from a module
wetwire-aws build --module myapp > template.json

# Generate YAML
wetwire-aws build --module myapp --format yaml

# List registered resources
wetwire-aws list --module myapp

# Validate references
wetwire-aws validate --module myapp
```

---

## Multi-File Organization

Split resources across files:

```
myapp/
├── __init__.py      # Uses setup_resources() for auto-discovery
├── __init__.pyi     # Auto-generated for IDE support
├── storage.py       # S3, EFS
├── compute.py       # Lambda, EC2
├── network.py       # VPC, Subnets
└── database.py      # DynamoDB, RDS
```

**__init__.py** (the key file):
```python
from wetwire_aws.loader import setup_resources
setup_resources(__file__, __name__, globals())
```

`setup_resources()` automatically:
- Discovers all `.py` files in the package
- Parses them to find class definitions and references
- Loads modules in dependency order (dependencies first)
- Makes cross-file references work via namespace injection
- Generates `.pyi` stubs for IDE autocomplete

**storage.py:**
```python
from . import *

__all__ = ["DataBucket"]

class DataBucket(s3.Bucket):
    bucket_name = "data"
```

**compute.py:**
```python
from . import *  # Includes Annotated, Ref, all exported symbols

__all__ = ["ProcessorFunction"]

class ProcessorFunction(lambda_.Function):
    function_name = "processor"
    runtime = lambda_.Runtime.PYTHON3_12
    # Cross-file reference - DataBucket is injected by setup_resources()
    bucket: Annotated[DataBucket, Ref()] = None  # noqa: F821
```

**Generate:**
```bash
wetwire-aws build --module myapp
```

> **Note:** The `# noqa: F821` comment silences linter warnings about `DataBucket` being undefined. It's actually injected by `setup_resources()` before this module loads. The generated `.pyi` stub ensures IDE autocomplete still works.

---

## Type-Safe Constants

Use generated enum classes for type safety:

```python
from . import *

class MyFunction(lambda_.Function):
    runtime = lambda_.Runtime.PYTHON3_12    # Not "python3.12"
    architectures = [lambda_.Architecture.ARM64]

class MyTableKeySchema(dynamodb.Table.KeySchema):
    attribute_name = "pk"
    key_type = dynamodb.KeyType.HASH

class MyTableAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = "pk"
    attribute_type = dynamodb.ScalarAttributeType.S

class MyTable(dynamodb.Table):
    key_schema = [MyTableKeySchema]
    attribute_definitions = [MyTableAttributeDefinition]
```

---

## Template Building

`CloudFormationTemplate.from_registry()` collects all registered resources:

```python
from myapp import CloudFormationTemplate

template = CloudFormationTemplate.from_registry(
    description="My Application Stack",
)

# Add parameters
template.add_parameter(
    "Environment",
    type="String",
    default="dev",
    allowed_values=["dev", "staging", "prod"],
)

# Add outputs (use type-safe reference)
template.add_output(
    "BucketArn",
    value=DataBucket.Arn,  # Type-safe attribute reference
    description="Data bucket ARN",
)

print(template.to_json())
```

---

## Deploy

```bash
# Generate template
wetwire-aws build --module myapp > template.json

# Deploy with AWS CLI
aws cloudformation deploy \
  --template-file template.json \
  --stack-name myapp \
  --capabilities CAPABILITY_IAM
```

---

## AWS SAM (Serverless) Support

Build serverless applications with type-safe SAM resources:

```python
from . import *

class ProcessorFunction(serverless.Function):
    function_name = "processor"
    runtime = serverless.Runtime.PYTHON3_12
    handler = "app.handler"
    code_uri = "./src"
    memory_size = 256
    timeout = 30

class ItemsApi(serverless.Api):
    stage_name = "prod"

class ItemsTable(serverless.SimpleTable):
    table_name = "items"
    primary_key = serverless.SimpleTable.PrimaryKey(
        name="id",
        type_="String",
    )
```

**Generate SAM template:**
```bash
wetwire-aws build --module myapp --format yaml > template.yaml
```

The output automatically includes the SAM Transform header:
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
```

### Supported SAM Resources

| Resource | Description |
|----------|-------------|
| `serverless.Function` | Lambda function with events, policies, auto-role |
| `serverless.Api` | REST API Gateway |
| `serverless.HttpApi` | HTTP API Gateway v2 |
| `serverless.SimpleTable` | DynamoDB table wrapper |
| `serverless.LayerVersion` | Lambda layer |
| `serverless.StateMachine` | Step Functions state machine |
| `serverless.Application` | Nested SAM applications |
| `serverless.Connector` | Resource permission connectors |
| `serverless.GraphQLApi` | AppSync GraphQL API |

### SAM Enums

```python
# Lambda runtimes
serverless.Runtime.PYTHON3_12
serverless.Runtime.NODEJS20_X

# Architectures
serverless.Architecture.ARM64
serverless.Architecture.X86_64

# Package types
serverless.PackageType.ZIP
serverless.PackageType.IMAGE
```

---

## Next Steps

- See the full [CLI Reference](CLI.md)
- Learn about [migration strategies](ADOPTION.md)
- Understand [how it compares](COMPARISON.md) to CDK and Terraform
- Explore [internals](INTERNALS.md) for how auto-registration works
