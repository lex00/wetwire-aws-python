"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Name(Parameter):
    type = STRING


class DomainName(Parameter):
    type = STRING


class Port(Parameter):
    type = STRING
    default = 80
