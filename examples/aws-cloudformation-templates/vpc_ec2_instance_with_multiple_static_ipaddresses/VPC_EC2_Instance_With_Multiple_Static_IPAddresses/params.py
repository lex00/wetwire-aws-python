"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class KeyName(Parameter):
    """Name of an existing EC2 KeyPair to enable SSH access to the instance"""

    type = KEY_PAIR
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the instance'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


class InstanceType(Parameter):
    """WebServer EC2 instance type"""

    type = STRING
    description = 'WebServer EC2 instance type'
    default = 't3.micro'
    constraint_description = 'must be a valid EC2 instance type.'


class VpcId(Parameter):
    """VpcId of your existing Virtual Private Cloud (VPC)"""

    type = VPC_ID
    description = 'VpcId of your existing Virtual Private Cloud (VPC)'
    constraint_description = 'must be the VPC Id of an existing Virtual Private Cloud.'


class SubnetId(Parameter):
    """SubnetId of an existing subnet (for the primary network) in your Virtual Private Cloud (VPC)"""

    type = SUBNET_ID
    description = 'SubnetId of an existing subnet (for the primary network) in your Virtual Private Cloud (VPC)'
    constraint_description = 'must be an existing subnet in the selected Virtual Private Cloud.'


class PrimaryIPAddress(Parameter):
    """Primary private IP. This must be a valid IP address for Subnet"""

    type = STRING
    description = 'Primary private IP. This must be a valid IP address for Subnet'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})'
    constraint_description = 'must be a valid IP address of the form x.x.x.x.'


class SecondaryIPAddress(Parameter):
    """Secondary private IP. This ust be a valid IP address for Subnet"""

    type = STRING
    description = 'Secondary private IP. This ust be a valid IP address for Subnet'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})'
    constraint_description = 'must be a valid IP address of the form x.x.x.x.'


class SSHLocation(Parameter):
    """The IP address range that can be used to SSH to the EC2 instances"""

    type = STRING
    description = 'The IP address range that can be used to SSH to the EC2 instances'
    default = '0.0.0.0/0'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'must be a valid IP CIDR range of the form x.x.x.x/x.'


class LatestAMI(Parameter):
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'
