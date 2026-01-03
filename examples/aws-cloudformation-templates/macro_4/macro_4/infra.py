"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro:
    resource: cloudformation.Macro
    name = 'S3Objects'
    function_name = MacroFunction.Arn
