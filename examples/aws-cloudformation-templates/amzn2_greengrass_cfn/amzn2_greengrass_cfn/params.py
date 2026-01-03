"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CoreName:
    """Greengrass Core name to be created. A "Thing" with be created with _Core appended to the name"""

    resource: Parameter
    type = STRING
    description = 'Greengrass Core name to be created. A "Thing" with be created with _Core appended to the name'
    default = 'gg_cfn'


class SecurityAccessCIDR:
    """CIDR block to limit inbound access for only SSH"""

    resource: Parameter
    type = STRING
    description = 'CIDR block to limit inbound access for only SSH'
    default = '0.0.0.0/0'


class myKeyPair:
    """Amazon EC2 Key Pair for accessing Greengrass Core instance"""

    resource: Parameter
    type = KEY_PAIR
    description = 'Amazon EC2 Key Pair for accessing Greengrass Core instance'


class LatestAmiId:
    resource: Parameter
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'


class InstanceType:
    resource: Parameter
    type = STRING
    default = 't3.micro'
