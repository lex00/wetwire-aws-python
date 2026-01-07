"""Infra resources: Transform."""

from . import *  # noqa: F403


class Transform(cloudformation.Macro):
    resource: cloudformation.Macro
    name = 'DatetimeNow'
    description = 'Provides the current datetime as string in the format requested.'
    function_name = TransformFunction.Arn
