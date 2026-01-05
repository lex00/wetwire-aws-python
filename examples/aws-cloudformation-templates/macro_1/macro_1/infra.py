"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro(cloudformation.Macro):
    name = 'Boto3'
    function_name = MacroFunction.Arn
