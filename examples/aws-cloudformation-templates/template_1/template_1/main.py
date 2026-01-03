"""Stack resources."""

from . import *  # noqa: F403


class CountMacroFunction:
    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    code_uri = 'src'
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_11
    timeout = 5
