"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro(cloudformation.Macro):
    name = 'Explode'
    function_name = MacroFunction.Arn
