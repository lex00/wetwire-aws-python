"""Stack resources."""

from . import *  # noqa: F403


class MacroFunction(serverless.Function):
    resource: serverless.Function
    runtime = lambda_.Runtime.PYTHON3_12
    code_uri = 'lambda'
    handler = 'index.handler'


class ResourceFunction(serverless.Function):
    resource: serverless.Function
    runtime = lambda_.Runtime.PYTHON3_12
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'CloudWatchFullAccess'
