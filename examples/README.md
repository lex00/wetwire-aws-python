# Examples

This directory contains AWS CloudFormation and SAM templates that have been imported and converted to wetwire-aws Python syntax. These examples are used for round-trip testing to ensure the importer generates valid, buildable code.

## Imported Templates

| Directory | Source | Template Count | License |
|-----------|--------|----------------|---------|
| `aws-cloudformation-templates/` | [aws-cloudformation/aws-cloudformation-templates](https://github.com/aws-cloudformation/aws-cloudformation-templates) | 159 | Apache 2.0 |
| `aws-sam-templates/` | Multiple SAM repositories (see below) | 42 | Apache 2.0 |

### SAM Template Sources

The `aws-sam-templates/` directory contains templates imported from:

- [aws/aws-sam-cli-app-templates](https://github.com/aws/aws-sam-cli-app-templates) - Official SAM CLI init templates
- [aws-samples/sessions-with-aws-sam](https://github.com/aws-samples/sessions-with-aws-sam) - Real-world SAM examples from Twitch series
- [aws-samples/sam-python-crud-sample](https://github.com/aws-samples/sam-python-crud-sample) - Python CRUD SAM sample

## License

The original templates are licensed under the Apache License 2.0. See the respective source repositories for full license details.

## Import Process

Templates are imported using the scripts in `scripts/`:

```bash
# Import CloudFormation templates
python scripts/import_aws_samples.py

# Import SAM templates
python scripts/import_sam_samples.py
```

## Purpose

These imported examples serve to:

1. Validate the importer generates syntactically correct Python code
2. Ensure imported packages can be built back to CloudFormation JSON
3. Provide reference implementations for common AWS patterns
4. Test round-trip consistency (YAML -> Python -> JSON)
