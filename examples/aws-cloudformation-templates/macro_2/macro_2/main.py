"""Stack resources."""

from . import *  # noqa: F403


class Function(serverless.Function):
    runtime = lambda_.Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'index.handler'
