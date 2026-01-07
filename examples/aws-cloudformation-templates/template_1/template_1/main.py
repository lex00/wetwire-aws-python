"""Stack resources."""

from . import *  # noqa: F403


class CountMacroFunction(CloudFormationResource):
    # Unknown resource type: AWS::Serverless::Function
    code_uri = 'src'
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_11
    timeout = 5
