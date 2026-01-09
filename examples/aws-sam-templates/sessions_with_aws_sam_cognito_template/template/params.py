"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppName(Parameter):
    """Name of the application"""

    type = STRING
    description = 'Name of the application'


class ClientDomains(Parameter):
    """Array of domains allowed to use this UserPool"""

    type = COMMA_DELIMITED_LIST
    description = 'Array of domains allowed to use this UserPool'


class AdminEmail(Parameter):
    """Email address for administrator"""

    type = STRING
    description = 'Email address for administrator'


class AddGroupsToScopes(Parameter):
    type = STRING
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class ScopeGroupsCondition(TemplateCondition):
    logical_id = 'ScopeGroups'
    expression = Equals(AddGroupsToScopes, 'true')
