# SAM (Serverless Application Model) Guide

wetwire-aws fully supports AWS SAM (Serverless Application Model) resources, allowing you to define serverless applications using the same declarative Python syntax as CloudFormation resources.

## Overview

SAM is an extension of CloudFormation that simplifies building serverless applications. wetwire-aws supports all 9 SAM resource types:

| Resource | Description |
|----------|-------------|
| `serverless.Function` | Lambda functions with SAM-specific features |
| `serverless.Api` | API Gateway REST APIs |
| `serverless.HttpApi` | API Gateway HTTP APIs (v2) |
| `serverless.SimpleTable` | DynamoDB tables (simplified) |
| `serverless.LayerVersion` | Lambda layers |
| `serverless.StateMachine` | Step Functions state machines |
| `serverless.Application` | Nested SAM applications |
| `serverless.Connector` | Resource permission connectors |
| `serverless.GraphQLApi` | AppSync GraphQL APIs |

## Quick Start

```python
from . import *

class HelloFunction(serverless.Function):
    handler = "bootstrap"
    runtime = serverless.Runtime.PROVIDED_AL2
    code_uri = "./hello/"
    memory_size = 128
    timeout = 30
```

Generate the template:

```bash
wetwire-aws build --module myapp --format yaml > template.yaml
```

The output automatically includes the SAM Transform header:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  HelloFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: bootstrap
      Runtime: provided.al2
      CodeUri: ./hello/
      MemorySize: 128
      Timeout: 30
```

---

## SAM Function

The `serverless.Function` resource is the most commonly used SAM resource. It extends Lambda with simplified event source configuration.

### Basic Function

```python
from . import *

class MyFunction(serverless.Function):
    handler = "index.handler"
    runtime = serverless.Runtime.PYTHON3_12
    code_uri = "./src/"
    memory_size = 256
    timeout = 30
    description = "My serverless function"
```

### Function with Environment Variables

```python
from . import *

class ProcessorVariables:
    TABLE_NAME = DataTable
    BUCKET_NAME = DataBucket
    LOG_LEVEL = "INFO"

class ProcessorEnv(serverless.Function.Environment):
    variables = ProcessorVariables

class ProcessorFunction(serverless.Function):
    handler = "bootstrap"
    runtime = serverless.Runtime.PROVIDED_AL2
    code_uri = "./processor/"
    environment = ProcessorEnv
```

### Function with VPC Configuration

```python
from . import *

class VpcConfig(serverless.Function.VpcConfig):
    security_group_ids = ["sg-12345678"]
    subnet_ids = ["subnet-abc123", "subnet-def456"]

class VpcFunction(serverless.Function):
    handler = "bootstrap"
    runtime = serverless.Runtime.PROVIDED_AL2
    code_uri = "./handler/"
    vpc_config = VpcConfig
```

### Function with Inline Code

For simple functions, you can embed code directly:

```python
from . import *

class DateTimeFunction(serverless.Function):
    handler = "index.handler"
    runtime = serverless.Runtime.PYTHON3_12
    inline_code = '''
import json
from datetime import datetime

def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'timestamp': datetime.now().isoformat()})
    }
'''
```

### Function Properties Reference

| Property | Type | Description |
|----------|------|-------------|
| `handler` | str | Function entry point |
| `runtime` | str | Runtime environment (use `serverless.Runtime.*` constants) |
| `code_uri` | str | Path to function code |
| `inline_code` | str | Inline function code (alternative to code_uri) |
| `function_name` | str | Function name (optional) |
| `description` | str | Function description |
| `memory_size` | int | Memory in MB (128-10240) |
| `timeout` | int | Timeout in seconds (1-900) |
| `environment` | any | Environment variables |
| `vpc_config` | any | VPC configuration |
| `role` | any | IAM role ARN (auto-created if omitted) |
| `policies` | any | SAM policy templates or managed policy ARNs |
| `events` | dict | Event sources (API, S3, SQS, etc.) |
| `layers` | list | Lambda layer ARNs |
| `architectures` | list | CPU architecture (`x86_64` or `arm64`) |
| `tracing` | any | X-Ray tracing mode |
| `tags` | list | Resource tags |

---

## SAM Api

Create REST APIs with API Gateway:

```python
from . import *

class MyApi(serverless.Api):
    stage_name = "prod"
    description = "My REST API"
```

### API with CORS

```python
from . import *

class CorsConfig(serverless.Api.CorsConfiguration):
    allow_origin = "'*'"
    allow_methods = "'GET,POST,PUT,DELETE'"
    allow_headers = "'Content-Type,Authorization'"

class MyApi(serverless.Api):
    stage_name = "v1"
    cors = CorsConfig
```

---

## SAM HttpApi

HTTP APIs are simpler and cheaper than REST APIs:

```python
from . import *

class MyHttpApi(serverless.HttpApi):
    stage_name = "v1"
```

---

## SAM SimpleTable

Simplified DynamoDB table definition:

```python
from . import *

class UsersPrimaryKey(serverless.SimpleTable.PrimaryKey):
    name = "id"
    type_ = "String"

class UsersTable(serverless.SimpleTable):
    table_name = "users"
    primary_key = UsersPrimaryKey
```

---

## SAM LayerVersion

Create Lambda layers:

```python
from . import *

class CommonLayer(serverless.LayerVersion):
    layer_name = "common-dependencies"
    content_uri = "./layers/common/"
    compatible_runtimes = ["python3.11", "python3.12"]
    description = "Common Python dependencies"

# Reference in a function
class MyFunction(serverless.Function):
    handler = "index.handler"
    runtime = serverless.Runtime.PYTHON3_12
    code_uri = "./src/"
    layers = [CommonLayer.Arn]
```

---

## SAM StateMachine

Define Step Functions state machines:

```python
from . import *

class OrderWorkflow(serverless.StateMachine):
    name = "order-processing"
    type_ = "STANDARD"
    definition_uri = "./statemachine/order.asl.json"
```

---

## SAM Application

Deploy nested SAM applications:

```python
from . import *

class SharedInfra(serverless.Application):
    location = "arn:aws:serverlessrepo:us-east-1:123456789:applications/SharedInfra"
```

---

## SAM Connector

Simplify resource permissions:

```python
from . import *

class FunctionToTableConnector(serverless.Connector):
    source = {"Id": MyFunction}
    destination = {"Id": DataTable}
    permissions = ["Read", "Write"]
```

---

## Mixing SAM and CloudFormation

You can freely mix SAM resources with standard CloudFormation resources:

```python
from . import *

# Standard CloudFormation S3 bucket
class DataBucket(s3.Bucket):
    bucket_name = "my-data-bucket"

# Standard CloudFormation DynamoDB table
class DataTable(dynamodb.Table):
    table_name = "my-data-table"
    # ... full DynamoDB configuration

# SAM Function environment referencing CloudFormation resources
class ProcessorVariables:
    BUCKET_NAME = DataBucket
    TABLE_NAME = DataTable

class ProcessorEnv(serverless.Function.Environment):
    variables = ProcessorVariables

# SAM Function referencing CloudFormation resources
class ProcessorFunction(serverless.Function):
    handler = "bootstrap"
    runtime = serverless.Runtime.PROVIDED_AL2
    code_uri = "./processor/"
    environment = ProcessorEnv
```

The generated template will include the SAM Transform header because SAM resources are detected:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  DataBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-data-bucket
  DataTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: my-data-table
  ProcessorFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: bootstrap
      Runtime: provided.al2
      CodeUri: ./processor/
      Environment:
        Variables:
          BUCKET_NAME: !Ref DataBucket
          TABLE_NAME: !Ref DataTable
```

---

## Importing SAM Templates

You can import existing SAM templates into Python code:

```bash
wetwire-aws import template.yaml -o ./myapp
```

This generates Python code using the `serverless` module for SAM resources.

---

## Deploying SAM Applications

SAM templates require the SAM CLI or CloudFormation with package/deploy:

### Using SAM CLI

```bash
# Build (packages Lambda code)
sam build

# Deploy
sam deploy --guided
```

### Using AWS CLI

```bash
# Package (upload Lambda code to S3)
aws cloudformation package \
  --template-file template.yaml \
  --s3-bucket my-deployment-bucket \
  --output-template-file packaged.yaml

# Deploy
aws cloudformation deploy \
  --template-file packaged.yaml \
  --stack-name my-app \
  --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND
```

---

## SAM Enums

Use type-safe constants for SAM properties:

```python
# Lambda runtimes
serverless.Runtime.PYTHON3_12
serverless.Runtime.NODEJS20_X
serverless.Runtime.PROVIDED_AL2

# Architectures
serverless.Architecture.ARM64
serverless.Architecture.X86_64

# Package types
serverless.PackageType.ZIP
serverless.PackageType.IMAGE
```

---

## See Also

- [Quick Start](QUICK_START.md) - Getting started with wetwire-aws
- [CLI Reference](CLI.md) - Command reference
- [Import Workflow](IMPORT_WORKFLOW.md) - Testing against AWS sample templates
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)
