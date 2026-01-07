"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CoreName(Parameter):
    """Greengrass Core name to be created. A "Thing" with be created with _Core appended to the name"""

    type = STRING
    description = 'Greengrass Core name to be created. A "Thing" with be created with _Core appended to the name'
    default = 'gg_cfn'


class InstanceType(Parameter):
    type = STRING
    default = 't3.micro'


class LatestAmiId(Parameter):
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'


class SecurityAccessCIDR(Parameter):
    """CIDR block to limit inbound access for only SSH"""

    type = STRING
    description = 'CIDR block to limit inbound access for only SSH'
    default = '0.0.0.0/0'


class myKeyPair(Parameter):
    """Amazon EC2 Key Pair for accessing Greengrass Core instance"""

    type = KEY_PAIR
    description = 'Amazon EC2 Key Pair for accessing Greengrass Core instance'
