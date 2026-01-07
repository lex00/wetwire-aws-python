"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class KeyName(Parameter):
    """Name of an existing EC2 KeyPair to enable SSH access to the instance"""

    type = KEY_PAIR
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the instance'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


class InstanceType(Parameter):
    """EC2 instance type"""

    type = STRING
    description = 'EC2 instance type'
    default = 't3.medium'
    constraint_description = 'must be a valid EC2 instance type.'


class InstanceAMI(Parameter):
    """Managed AMI ID for EC2 Instance"""

    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'Managed AMI ID for EC2 Instance'
    default = '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'


class IAMRole(Parameter):
    """EC2 attached IAM role"""

    type = STRING
    description = 'EC2 attached IAM role'
    default = 'CloudWatchAgentAdminRole'
    constraint_description = 'must be an existing IAM role which will be attached to EC2 instance.'


class SSHLocation(Parameter):
    """The IP address range that can be used to SSH to the EC2 instances"""

    type = STRING
    description = 'The IP address range that can be used to SSH to the EC2 instances'
    default = '0.0.0.0/0'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'must be a valid IP CIDR range of the form x.x.x.x/x.'


class SubnetId(Parameter):
    type = SUBNET_ID
