"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class TestCount(Parameter):
    type = NUMBER
    default = 3


class TestList(Parameter):
    type = COMMA_DELIMITED_LIST
    default = 'foo,bar'
