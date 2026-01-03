"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Name:
    resource: Parameter
    type = STRING


class DomainName:
    resource: Parameter
    type = STRING


class Port:
    resource: Parameter
    type = STRING
    default = 80
