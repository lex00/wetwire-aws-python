"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class NatGatewayPrivateIP(Parameter):
    """The private IP address of the NAT Gateway"""

    type = STRING
    description = 'The private IP address of the NAT Gateway'


class NatGatewayID(Parameter):
    """The ID of the NAT Gateway"""

    type = STRING
    description = 'The ID of the NAT Gateway'


class VpcCidr(Parameter):
    """The CIDR block of the VPC"""

    type = STRING
    description = 'The CIDR block of the VPC'


class LogGroupName(Parameter):
    """The ARN of the log group to query"""

    type = STRING
    description = 'The ARN of the log group to query'
