# Import Workflow Documentation

This document explains the CloudFormation template import workflow used by wetwire-aws (Python) to test and validate the implementation against real-world AWS templates.

## Overview

The import workflow tests wetwire-aws's ability to parse and convert CloudFormation templates from the official [aws-cloudformation-templates](https://github.com/awslabs/aws-cloudformation-templates) and [aws-sam-cli-app-templates](https://github.com/aws/aws-sam-cli-app-templates) repositories into Python code. This provides continuous validation and identifies edge cases for improvement.

## Workflow Steps

The import workflow follows these steps:

1. **Clone Repository**: Clone the template repository (or use a local copy)
2. **Filter Templates**: Remove excluded templates (see below for exclusion criteria)
3. **Discover Templates**: Find all `.yaml`, `.yml`, and `.json` files
4. **Import**: Convert each CloudFormation template to Python code using `wetwire-aws import`
5. **Lint**: Run `wetwire-aws lint --fix` on generated code
6. **Build**: Verify `wetwire-aws build` produces valid output
7. **Report**: Generate statistics on success/failure rates

## Basic Usage

### Import a single template

```bash
wetwire-aws import template.yaml -o ./myapp
```

### Import with custom package name

```bash
wetwire-aws import template.yaml -o ./myapp --name my_infrastructure
```

### Import as single file

```bash
wetwire-aws import template.yaml -o ./myapp --single-file
```

## Template Exclusion Lists

### Excluded Templates

Templates that are completely excluded from import use non-standard CloudFormation features or are not CloudFormation templates at all.

#### Rain-specific templates

Templates that use Rain preprocessor tags (`!Rain::` custom tags):

```
APIGateway/apigateway_lambda_integration.yaml
CloudFormation/CustomResources/getfromjson/src/getfromjson.yml
RainModules/*.yml
Solutions/GitLab/GitLabServer.*
Solutions/GitLabAndVSCode/GitLabAndVSCode.*
Solutions/Gitea/Gitea.*
Solutions/ManagedAD/templates/MANAGEDAD.cfn.*
Solutions/VSCode/VSCodeServer.*
ElastiCache/Elasticache-snapshot.yaml
```

**Rationale**: Rain is a CloudFormation deployment tool that extends the template syntax with custom tags. These templates require Rain preprocessing and cannot be imported directly.

#### Kubernetes manifests

```
EKS/manifest.yml
```

**Rationale**: This is a Kubernetes manifest file, not a CloudFormation template.

#### Lambda test events

```
CloudFormation/CustomResources/getfromjson/src/events/*.json
```

**Rationale**: These are Lambda test event payloads, not CloudFormation templates.

#### CloudFormation Macro definitions

```
CloudFormation/MacrosExamples/*/macro.*
```

**Rationale**: These templates only define the macro Lambda function itself. They don't contain infrastructure resources to validate.

#### CodeBuild buildspec files

```
Solutions/CodeBuildAndCodePipeline/codebuild-app-*.yml
```

**Rationale**: These are CodeBuild buildspec files, not CloudFormation templates.

#### CDK configuration files

```
CloudFormation/StackSets-CDK/cdk.json
CloudFormation/StackSets-CDK/config.json
```

**Rationale**: These are AWS CDK configuration files, not CloudFormation templates.

### Skipped Templates

Templates that import successfully but have known issues in validation:

#### example_2

**Issue**: Uses the ExecutionRoleBuilder custom CloudFormation macro with non-standard properties.

#### efs_with_automount_to_ec2

**Issue**: Complex Join-based UserData generates malformed strings with nested intrinsic functions.

## Output Structure

The import command generates:

```
myapp/
├── __init__.py      # Package entry with setup_resources()
├── params.py        # Parameters, Mappings, Conditions
├── outputs.py       # CloudFormation Outputs
├── main.py          # Main resources (or split by category)
├── storage.py       # S3, EFS resources (if split)
├── compute.py       # Lambda, EC2 resources (if split)
├── network.py       # VPC, networking resources (if split)
└── security.py      # IAM resources (if split)
```

For single-file mode (`--single-file`):

```
myapp/
├── __init__.py
└── resources.py     # All resources in one file
```

## Success Metrics

Current import success rates:

- **CloudFormation templates**: 254/254 (100%)
- **SAM templates**: 58/58 (100%)

Covers all major AWS services and CloudFormation features including:
- Intrinsic functions (Ref, GetAtt, Sub, Join, etc.)
- Pseudo-parameters (AWS::Region, AWS::StackName, etc.)
- Resource dependencies
- SAM resources and transforms

## Post-Import Workflow

After importing a template:

```bash
# 1. Import the template
wetwire-aws import template.yaml -o ./myapp

# 2. Auto-fix lint issues
wetwire-aws lint ./myapp --fix

# 3. Validate the generated code
wetwire-aws validate --module myapp

# 4. Build to verify output
wetwire-aws build --module myapp > template.json

# 5. Compare with original (optional)
diff <(yq -o json template.yaml) template.json
```

## Improvement Loop

The import workflow provides continuous feedback for improving wetwire-aws:

1. **Identify edge cases**: Failed imports reveal parsing issues
2. **Test new features**: Verify intrinsic functions work correctly
3. **Regression testing**: Ensure changes don't break existing templates
4. **Documentation**: Understand real-world CloudFormation patterns

## Cross-Implementation Consistency

Both the Go and Python implementations use the same exclusion lists to ensure consistent behavior and test coverage. When adding new exclusions:

1. Update exclusion lists in both repositories
2. Document the rationale in both locations
3. Cross-reference the related issue/PR

## See Also

- [SAM Guide](SAM.md) - SAM resource support
- [CLI Reference](CLI.md) - Import command details
- [Quick Start](QUICK_START.md) - Getting started
