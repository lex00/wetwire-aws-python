"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Date(Parameter):
    """Date for this test (ISO 8601 format)"""

    type = STRING
    description = 'Date for this test (ISO 8601 format)'
    default = ''
    allowed_pattern = '^$|^\\d{4}(-\\d\\d(-\\d\\d(T\\d\\d:\\d\\d(:\\d\\d)?(\\.\\d+)?(([+-]\\d\\d:\\d\\d)|Z)?)?)?)?$'


class Date2(Parameter):
    """Second date for test to use (ISO 8601 format)"""

    type = STRING
    description = 'Second date for test to use (ISO 8601 format)'
    default = ''
    allowed_pattern = '^$|^\\d{4}(-\\d\\d(-\\d\\d(T\\d\\d:\\d\\d(:\\d\\d)?(\\.\\d+)?(([+-]\\d\\d:\\d\\d)|Z)?)?)?)?$'


class Days(Parameter):
    """Days"""

    type = NUMBER
    description = 'Days'
    default = 1
