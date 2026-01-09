"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DbEngine(Parameter):
    """DB Engine"""

    type = STRING
    description = 'DB Engine'
    default = 'MySQL'


class DbVersion(Parameter):
    """DB Version"""

    type = STRING
    description = 'DB Version'


class DbName(Parameter):
    """Name of DB to use"""

    type = STRING
    description = 'Name of DB to use'
    no_echo = True


class DbUsername(Parameter):
    """Username for DB"""

    type = STRING
    description = 'Username for DB'
    no_echo = True


class DbPassword(Parameter):
    """Password for DB"""

    type = STRING
    description = 'Password for DB'
    no_echo = True
