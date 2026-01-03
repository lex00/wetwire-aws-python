"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro:
    resource: cloudformation.Macro
    name = 'Count'
    function_name = CountMacroFunction.Arn
