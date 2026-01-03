"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppName:
    resource: Parameter
    type = STRING


class UserPoolArn:
    resource: Parameter
    type = STRING
