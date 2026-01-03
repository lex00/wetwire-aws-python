"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class SSMKey:
    """Name of parameter store which contains the json configuration of CWAgent."""

    resource: Parameter
    type = STRING
    description = 'Name of parameter store which contains the json configuration of CWAgent.'
    default = 'AmazonCloudWatch-DefaultWindowsConfigCloudFormation'


class KeyName:
    """Name of an existing EC2 KeyPair to enable SSH access to the instance"""

    resource: Parameter
    type = KEY_PAIR
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the instance'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


class InstanceType:
    """EC2 instance type"""

    resource: Parameter
    type = STRING
    description = 'EC2 instance type'
    default = 't3.medium'
    constraint_description = 'must be a valid EC2 instance type.'


class InstanceAMI:
    """Managed AMI ID for EC2 Instance"""

    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    description = 'Managed AMI ID for EC2 Instance'
    default = '/aws/service/ami-windows-latest/Windows_Server-2022-English-Full-SQL_2022_Web'


class IAMRole:
    """EC2 attached IAM role"""

    resource: Parameter
    type = STRING
    description = 'EC2 attached IAM role'
    default = 'CloudWatchAgentAdminRole'
    constraint_description = 'must be an existing IAM role which will be attached to EC2 instance.'


class SubnetId:
    resource: Parameter
    type = SUBNET_ID
