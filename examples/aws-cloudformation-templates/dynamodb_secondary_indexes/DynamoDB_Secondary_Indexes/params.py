"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class ReadCapacityUnits(Parameter):
    """Provisioned read throughput"""

    type = NUMBER
    description = 'Provisioned read throughput'
    default = '5'
    min_value = 5
    max_value = 10000
    constraint_description = 'must be between 5 and 10000'


class WriteCapacityUnits(Parameter):
    """Provisioned write throughput"""

    type = NUMBER
    description = 'Provisioned write throughput'
    default = '10'
    min_value = 5
    max_value = 10000
    constraint_description = 'must be between 5 and 10000'
