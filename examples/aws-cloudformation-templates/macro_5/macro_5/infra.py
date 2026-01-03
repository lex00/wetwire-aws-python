"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro:
    resource: cloudformation.Macro
    name = 'StackMetrics'
    function_name = MacroFunction.Arn
