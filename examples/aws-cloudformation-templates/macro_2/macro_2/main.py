"""Stack resources."""

from . import *  # noqa: F403


class Function:
    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'index.handler'
