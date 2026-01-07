"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class HashKeyElementName(Parameter):
    """HashType PrimaryKey Name"""

    type = STRING
    description = 'HashType PrimaryKey Name'
    allowed_pattern = '[a-zA-Z0-9]*'
    min_length = 1
    max_length = 2048
    constraint_description = 'must contain only alphanumberic characters'


class HashKeyElementType(Parameter):
    """HashType PrimaryKey Type"""

    type = STRING
    description = 'HashType PrimaryKey Type'
    default = 'S'
    allowed_pattern = '[S|N]'
    min_length = 1
    max_length = 1
    constraint_description = 'must be either S or N'


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
