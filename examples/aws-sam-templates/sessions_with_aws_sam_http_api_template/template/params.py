"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class UserPoolId(Parameter):
    """User poolID for Cognito provider"""

    type = STRING
    description = 'User poolID for Cognito provider'


class Audience(Parameter):
    """Client id for user pool"""

    type = STRING
    description = 'Client id for user pool'
