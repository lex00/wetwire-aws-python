"""Infra resources: Macro."""

from . import *  # noqa: F403


class Macro(cloudformation.Macro):
    name = 'ExecutionRoleBuilder'
    function_name = Function.Arn
