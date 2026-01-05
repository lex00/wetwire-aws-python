"""Stack resources."""

from . import *  # noqa: F403


class MacroFunction:
    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = lambda_.Runtime.PYTHON3_12
    code_uri = 'lambda'
    handler = 'index.handler'


class ResourceFunction:
    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = lambda_.Runtime.PYTHON3_12
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'CloudWatchFullAccess'
