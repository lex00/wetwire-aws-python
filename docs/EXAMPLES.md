# Examples Reference

The `examples/` directory contains imported AWS templates converted to wetwire-aws Python code. These serve as:

1. **Test artifacts** - Validate the import workflow
2. **Reference implementations** - Real-world CloudFormation patterns
3. **Learning resources** - See how complex templates translate to Python

## Directory Structure

```
examples/
├── aws-cloudformation-templates/   # 161 imported templates
│   ├── amazon_linux/
│   │   └── amazon_linux/           # Python package
│   │       ├── __init__.py
│   │       ├── __init__.pyi        # Generated stubs
│   │       ├── params.py           # Parameters
│   │       ├── compute.py          # EC2 resources
│   │       └── network.py          # VPC resources
│   └── ...
│
└── aws-sam-templates/              # 44 imported SAM templates
    ├── governance_1_initial_setup_template/
    └── ...
```

## CloudFormation Templates (161)

Imported from [aws-cloudformation-templates](https://github.com/awslabs/aws-cloudformation-templates).

### By AWS Service

| Category | Count | Examples |
|----------|-------|----------|
| EC2/Compute | ~50 | `amazon_linux`, `ubuntu`, `windows`, `autoscaling*` |
| VPC/Network | ~30 | `public_vpc`, `private_vpc`, `vpcpeering*` |
| ECS/Containers | ~15 | `ecs_*`, `fargate_*` |
| Lambda | ~10 | `lambda_*`, `apigateway_lambda*` |
| CloudFormation | ~15 | `macro_*`, `stackset_*`, `nested_*` |
| Other | ~40 | Various services |

### Notable Examples

| Example | Description |
|---------|-------------|
| `amazon_linux` | Basic EC2 instance with VPC |
| `autoscalingmultiazwithnotifications` | Auto Scaling with SNS notifications |
| `vpcpeering_requester_setup` | Cross-account VPC peering |
| `ecs_cluster_with_alb` | ECS with Application Load Balancer |
| `rds_with_dbparametergroup` | RDS with custom parameter groups |

## SAM Templates (44)

Imported from [aws-sam-cli-app-templates](https://github.com/aws/aws-sam-cli-app-templates) and [sessions-with-aws-sam](https://github.com/aws-samples/sessions-with-aws-sam).

### By Pattern

| Pattern | Count | Examples |
|---------|-------|----------|
| Governance | 5 | `governance_1_*` through `governance_5_*` |
| Custom Domains | 5 | `custom_domains_*` |
| Event Sources | 10+ | `eventbridge_*`, `sqs_*`, `kinesis_*` |
| API Patterns | 10+ | `appsync_*`, `graphql_*`, `rest_*` |

### Notable Examples

| Example | Description |
|---------|-------------|
| `governance_5_reusable_setup_full_template` | Complete governance setup with Config rules |
| `sessions_with_aws_sam_eventbridge_template` | EventBridge event patterns |
| `appsync_singletable_sam_template` | AppSync with DynamoDB single-table design |

## Package Structure

Each imported template becomes a Python package:

```
example_name/
├── __init__.py      # setup_resources() entry point
├── __init__.pyi     # Generated type stubs for IDE support
├── params.py        # Parameters, Mappings, Conditions
├── outputs.py       # CloudFormation Outputs (if any)
├── main.py          # Resources (small templates)
│
# Or split by category (large templates):
├── compute.py       # EC2, Lambda, ECS
├── network.py       # VPC, subnets, security groups
├── storage.py       # S3, EFS, EBS
├── security.py      # IAM roles, policies
└── database.py      # RDS, DynamoDB
```

## Using Examples

### Build a template

```bash
wetwire-aws build --module examples.aws-cloudformation-templates.amazon_linux.amazon_linux
```

### View resources

```bash
wetwire-aws list --module examples.aws-cloudformation-templates.amazon_linux.amazon_linux
```

### Copy as starting point

```bash
cp -r examples/aws-cloudformation-templates/amazon_linux/amazon_linux ./my_ec2_stack
```

## Import Success Rates

| Repository | Success | Total |
|------------|---------|-------|
| aws-cloudformation-templates | 254/254 | 100% |
| aws-sam-templates | 58/58 | 100% |

See [IMPORT_WORKFLOW.md](IMPORT_WORKFLOW.md) for details on exclusions and the testing process.

## Refreshing Examples

To re-import all examples (after updating the importer):

```bash
# CloudFormation templates
./scripts/import_aws_samples.sh

# SAM templates
./scripts/import_sam_samples.sh
```

## See Also

- [IMPORT_WORKFLOW.md](IMPORT_WORKFLOW.md) - Import testing documentation
- [SAM.md](SAM.md) - SAM resource guide
- [Quick Start](QUICK_START.md) - Getting started
