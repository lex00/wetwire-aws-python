"""Infra resources: Transform."""

from . import *  # noqa: F403


class Transform(cloudformation.Macro):
    resource: cloudformation.Macro
    name = 'String'
    description = 'Provides various string processing functions'
    function_name = TransformFunction.Arn
