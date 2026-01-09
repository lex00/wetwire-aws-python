"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DbEngine(Parameter):
    type = SSM_PARAMETER_STRING
    default = '/myApp/DbEngine'
