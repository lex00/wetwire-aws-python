"""Template outputs."""

from . import *  # noqa: F403


class ResourceFunctionOutput:
    resource: Output
    value = ResourceFunction.Arn
    export_name = 'StackMetricsMacroFunction'
