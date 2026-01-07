"""Infra resources: Transform."""

from . import *  # noqa: F403


class Transform(cloudformation.Macro):
    resource: cloudformation.Macro
    name = Sub('PyPlate')
    description = 'Processes inline python in templates'
    function_name = TransformFunction.Arn
