"""Stack resources."""

from . import *  # noqa: F403


class MacroFunction(CloudFormationResource):
    # Unknown resource type: AWS::Serverless::Function
    runtime = lambda_.Runtime.PYTHON3_12
    code_uri = 'lambda'
    handler = 'index.handler'


class ResourceFunction(CloudFormationResource):
    # Unknown resource type: AWS::Serverless::Function
    runtime = lambda_.Runtime.PYTHON3_12
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'CloudWatchFullAccess'
