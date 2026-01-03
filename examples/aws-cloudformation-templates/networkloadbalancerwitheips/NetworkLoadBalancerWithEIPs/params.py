"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class VPC:
    resource: Parameter
    type = 'List<AWS::EC2::VPC::Id>'


class Subnet1:
    """ID of the Subnet the instance should be launched in, this will link the instance to the same VPC."""

    resource: Parameter
    type = LIST_SUBNET_ID
    description = 'ID of the Subnet the instance should be launched in, this will link the instance to the same VPC.'


class Subnet2:
    """ID of the Subnet the instance should be launched in, this will link the instance to the same VPC."""

    resource: Parameter
    type = LIST_SUBNET_ID
    description = 'ID of the Subnet the instance should be launched in, this will link the instance to the same VPC.'


class ELBType:
    resource: Parameter
    type = STRING
    default = 'network'


class ELBIpAddressType:
    resource: Parameter
    type = STRING
    default = 'ipv4'
    allowed_values = [
    'ipv4',
    'dualstack',
]
