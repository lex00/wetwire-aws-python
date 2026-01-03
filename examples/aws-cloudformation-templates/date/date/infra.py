"""Infra resources: Transform."""

from . import *  # noqa: F403


class Transform:
    resource: cloudformation.Macro
    name = 'Date'
    description = 'Provides date processing functions'
    function_name = TransformFunction.Arn
