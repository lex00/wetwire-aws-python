"""Lambda function that references role from another file."""

from . import *  # noqa: F401, F403, F405

__all__ = ["AppFunction"]


class AppFunction(lambda_.Function):  # noqa: F405
    """Lambda function that uses the AppRole."""

    function_name = "app-function"
    runtime = "python3.12"
    handler = "index.handler"
    # Cross-file reference using no-parens pattern
    # AppRole is injected by setup_resources() before this module executes
    role = AppRole.Arn  # noqa: F405, F821
