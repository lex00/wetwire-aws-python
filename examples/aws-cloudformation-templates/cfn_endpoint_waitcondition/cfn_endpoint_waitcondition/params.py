"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class EnvironmentName(Parameter):
    """An environment name that will be prefixed to resource names"""

    type = STRING
    description = 'An environment name that will be prefixed to resource names'


class VpcCIDR(Parameter):
    """Please enter the IP range (CIDR notation) for this VPC"""

    type = STRING
    description = 'Please enter the IP range (CIDR notation) for this VPC'
    default = '10.192.0.0/16'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


class PublicSubnet1CIDR(Parameter):
    """Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone"""

    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the public subnet in the first Availability Zone'
    default = '10.192.10.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


class PublicSubnet2CIDR(Parameter):
    """Please enter the IP range (CIDR notation) for the public subnet in the second Availability Zone"""

    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the public subnet in the second Availability Zone'
    default = '10.192.11.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


class PrivateSubnet1CIDR(Parameter):
    """Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone"""

    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the private subnet in the first Availability Zone'
    default = '10.192.20.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


class PrivateSubnet2CIDR(Parameter):
    """Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone"""

    type = STRING
    description = 'Please enter the IP range (CIDR notation) for the private subnet in the second Availability Zone'
    default = '10.192.21.0/24'
    allowed_pattern = '((\\d{1,3})\\.){3}\\d{1,3}/\\d{1,2}'


class KeyName(Parameter):
    """Key pair for EC2 access"""

    type = KEY_PAIR
    description = 'Key pair for EC2 access'


class LinuxAMI(Parameter):
    """Managed AMI ID for Amazon Linux"""

    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'Managed AMI ID for Amazon Linux'
    default = '/aws/service/ami-amazon-linux-latest/amzn-ami-hvm-x86_64-gp2'
