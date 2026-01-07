"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro(cloudformation.Macro):
    resource: cloudformation.Macro
    name = 'StackMetrics'
    function_name = MacroFunction.Arn
