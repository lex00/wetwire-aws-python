"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class InstanceType(Parameter):
    """WebServer EC2 instance type"""

    type = STRING
    description = 'WebServer EC2 instance type'
    default = 't4g.micro'


class OperatorEMail(Parameter):
    """Email address to notify if there are any scaling operations"""

    type = STRING
    description = 'Email address to notify if there are any scaling operations'


class KeyName(Parameter):
    """The EC2 Key Pair to allow SSH access to the instances"""

    type = KEY_PAIR
    description = 'The EC2 Key Pair to allow SSH access to the instances'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


class SSHLocation(Parameter):
    """The IP address range that can be used to SSH to the EC2 instances"""

    type = STRING
    description = 'The IP address range that can be used to SSH to the EC2 instances'
    default = '192.168.1.0/24'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'must be a valid IP CIDR range of the form x.x.x.x/x.'


class LatestAmiId(Parameter):
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64'


class KmsKeyArn(Parameter):
    """KMS Key ARN to encrypt data"""

    type = STRING
    description = 'KMS Key ARN to encrypt data'


class CertificateArn(Parameter):
    """Certificate ARN for HTTPS"""

    type = STRING
    description = 'Certificate ARN for HTTPS'


class SecurityGroups(Parameter):
    """Security Groups to be used"""

    type = LIST_SECURITY_GROUP_ID
    description = 'Security Groups to be used'


class Subnets(Parameter):
    """Subnets to be used"""

    type = LIST_SUBNET_ID
    description = 'Subnets to be used'


class AZs(Parameter):
    """Availability Zones to be used"""

    type = LIST_AVAILABILITY_ZONE
    description = 'Availability Zones to be used'


class VPC(Parameter):
    """VPC to be used"""

    type = VPC_ID
    description = 'VPC to be used'


class Region2ExamplesMapping(Mapping):
    map_data = {
        'us-east-1': {
            'Examples': 'https://s3.amazonaws.com/cloudformation-examples-us-east-1',
        },
        'us-west-2': {
            'Examples': 'https://s3-us-west-2.amazonaws.com/cloudformation-examples-us-west-2',
        },
        'us-west-1': {
            'Examples': 'https://s3-us-west-1.amazonaws.com/cloudformation-examples-us-west-1',
        },
        'eu-west-1': {
            'Examples': 'https://s3-eu-west-1.amazonaws.com/cloudformation-examples-eu-west-1',
        },
        'eu-central-1': {
            'Examples': 'https://s3-eu-central-1.amazonaws.com/cloudformation-examples-eu-central-1',
        },
        'ap-southeast-1': {
            'Examples': 'https://s3-ap-southeast-1.amazonaws.com/cloudformation-examples-ap-southeast-1',
        },
        'ap-northeast-1': {
            'Examples': 'https://s3-ap-northeast-1.amazonaws.com/cloudformation-examples-ap-northeast-1',
        },
        'ap-northeast-2': {
            'Examples': 'https://s3-ap-northeast-2.amazonaws.com/cloudformation-examples-ap-northeast-2',
        },
        'ap-southeast-2': {
            'Examples': 'https://s3-ap-southeast-2.amazonaws.com/cloudformation-examples-ap-southeast-2',
        },
        'ap-south-1': {
            'Examples': 'https://s3-ap-south-1.amazonaws.com/cloudformation-examples-ap-south-1',
        },
        'us-east-2': {
            'Examples': 'https://s3-us-east-2.amazonaws.com/cloudformation-examples-us-east-2',
        },
        'sa-east-1': {
            'Examples': 'https://s3-sa-east-1.amazonaws.com/cloudformation-examples-sa-east-1',
        },
        'cn-north-1': {
            'Examples': 'https://s3.cn-north-1.amazonaws.com.cn/cloudformation-examples-cn-north-1',
        },
    }
