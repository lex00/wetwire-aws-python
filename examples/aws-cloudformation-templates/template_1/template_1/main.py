"""Stack resources."""

from . import *  # noqa: F403


class CountMacroFunction(serverless.Function):
    resource: serverless.Function
    code_uri = 'src'
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_11
    timeout = 5
