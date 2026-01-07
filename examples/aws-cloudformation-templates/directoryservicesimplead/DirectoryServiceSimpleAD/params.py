"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DomainName(Parameter):
    """FQDN of the domain for this directory"""

    type = STRING
    description = 'FQDN of the domain for this directory'
    default = 'corp.example.com'


class SimpleADShortName(Parameter):
    """Netbios name of the domain for this directory"""

    type = STRING
    description = 'Netbios name of the domain for this directory'
    default = 'corp'


class CreateAlias(Parameter):
    """Only required for applications which need a URL to connect to the directory"""

    type = STRING
    description = 'Only required for applications which need a URL to connect to the directory'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class PrivateSubnet1(Parameter):
    """Subnet to be used for the Directoty"""

    type = LIST_SUBNET_ID
    description = 'Subnet to be used for the Directoty'


class PrivateSubnet2(Parameter):
    """Subnet to be used for the Directoty"""

    type = LIST_SUBNET_ID
    description = 'Subnet to be used for the Directoty'


class VPCID(Parameter):
    """The VPC the directory will be created in"""

    type = 'List<AWS::EC2::VPC::Id>'
    description = 'The VPC the directory will be created in'


class Size(Parameter):
    """Size of the Simple AD"""

    type = STRING
    description = 'Size of the Simple AD'
    default = 'Small'
    allowed_values = [
    'Small',
    'Large',
]


class AliasCondition(TemplateCondition):
    logical_id = 'Alias'
    expression = Equals(CreateAlias, 'true')
