"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppName(Parameter):
    """Name of application (no spaces). Value must be globally unique"""

    type = STRING
    description = 'Name of application (no spaces). Value must be globally unique'
    default = 'shortener'


class UseLocalClient(Parameter):
    """Enables public client and local client for testing. (Less secure)"""

    type = STRING
    description = 'Enables public client and local client for testing. (Less secure)'
    default = 'false'


class CustomDomain(Parameter):
    """Custom domain added to client"""

    type = STRING
    description = 'Custom domain added to client'
    default = 'none'


class ClientAddress(Parameter):
    """URL for client"""

    type = STRING
    description = 'URL for client'


class IsLocalCondition(TemplateCondition):
    logical_id = 'IsLocal'
    expression = Equals(UseLocalClient, 'true')
