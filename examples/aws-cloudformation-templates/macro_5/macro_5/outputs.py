"""Template outputs."""

from . import *  # noqa: F403


class ResourceFunctionOutput(Output):
    value = ResourceFunction.Arn
    export_name = 'StackMetricsMacroFunction'
