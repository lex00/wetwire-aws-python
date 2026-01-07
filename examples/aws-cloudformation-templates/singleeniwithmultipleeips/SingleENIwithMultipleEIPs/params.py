"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Subnet(Parameter):
    """ID of the Subnet the instance should be launched in, this will link the instance to the same VPC."""

    type = LIST_SUBNET_ID
    description = 'ID of the Subnet the instance should be launched in, this will link the instance to the same VPC.'
