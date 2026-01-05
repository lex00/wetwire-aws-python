"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro(cloudformation.Macro):
    name = 'StackMetrics'
    function_name = MacroFunction.Arn
