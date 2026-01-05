"""Stack resources."""

from . import *  # noqa: F403


class MacroFunction(CloudFormationResource):
    # Unknown resource type: AWS::Serverless::Function
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'explode.handler'
