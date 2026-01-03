"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Subnet:
    """ID of the Subnet the instance should be launched in, this will link the instance to the same VPC."""

    resource: Parameter
    type = LIST_SUBNET_ID
    description = 'ID of the Subnet the instance should be launched in, this will link the instance to the same VPC.'
