"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DomainName:
    """FQDN of the domain for this directory"""

    resource: Parameter
    type = STRING
    description = 'FQDN of the domain for this directory'
    default = 'corp.example.com'


class SimpleADShortName:
    """Netbios name of the domain for this directory"""

    resource: Parameter
    type = STRING
    description = 'Netbios name of the domain for this directory'
    default = 'corp'


class CreateAlias:
    """Only required for applications which need a URL to connect to the directory"""

    resource: Parameter
    type = STRING
    description = 'Only required for applications which need a URL to connect to the directory'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class PrivateSubnet1:
    """Subnet to be used for the Directoty"""

    resource: Parameter
    type = LIST_SUBNET_ID
    description = 'Subnet to be used for the Directoty'


class PrivateSubnet2:
    """Subnet to be used for the Directoty"""

    resource: Parameter
    type = LIST_SUBNET_ID
    description = 'Subnet to be used for the Directoty'


class VPCID:
    """The VPC the directory will be created in"""

    resource: Parameter
    type = 'List<AWS::EC2::VPC::Id>'
    description = 'The VPC the directory will be created in'


class Size:
    """Size of the Simple AD"""

    resource: Parameter
    type = STRING
    description = 'Size of the Simple AD'
    default = 'Small'
    allowed_values = [
    'Small',
    'Large',
]


class AliasCondition:
    resource: TemplateCondition
    logical_id = 'Alias'
    expression = Equals(CreateAlias, 'true')
