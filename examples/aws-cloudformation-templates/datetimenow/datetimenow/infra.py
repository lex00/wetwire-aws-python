"""Infra resources: Transform."""

from . import *  # noqa: F403


class Transform:
    resource: cloudformation.Macro
    name = 'DatetimeNow'
    description = 'Provides the current datetime as string in the format requested.'
    function_name = TransformFunction.Arn
