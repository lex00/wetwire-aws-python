"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class pEdition:
    """The AWS Microsoft AD edition. Valid values include Standard and Enterprise. The default is Enterprise.
"""

    resource: Parameter
    type = STRING
    description = """The AWS Microsoft AD edition. Valid values include Standard and Enterprise. The default is Enterprise.
"""
    default = 'Enterprise'
    allowed_values = [
    'Standard',
    'Enterprise',
]


class pDomainName:
    """The fully qualified name for the Microsoft Active Directory in AWS, such as corp.example.com. The name doesn't need to be publicly resolvable; it will resolve inside your VPC only.
"""

    resource: Parameter
    type = STRING
    description = """The fully qualified name for the Microsoft Active Directory in AWS, such as corp.example.com. The name doesn't need to be publicly resolvable; it will resolve inside your VPC only.
"""
    default = 'corp.example.com'


class pMicrosoftADShortName:
    """The NetBIOS name for your domain, such as CORP. If you don't specify a value, AWS Directory Service uses the first part of your directory DNS server name. For example, if your directory DNS server name is corp.example.com, AWS Directory Service specifies CORP for the NetBIOS name.
"""

    resource: Parameter
    type = STRING
    description = """The NetBIOS name for your domain, such as CORP. If you don't specify a value, AWS Directory Service uses the first part of your directory DNS server name. For example, if your directory DNS server name is corp.example.com, AWS Directory Service specifies CORP for the NetBIOS name.
"""
    default = 'corp'


class pEnableSingleSignOn:
    """Whether to enable single sign-on for a Microsoft Active Directory in AWS. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default. If enabling SSO, then "Create Alias" need to be set to true.
"""

    resource: Parameter
    type = STRING
    description = """Whether to enable single sign-on for a Microsoft Active Directory in AWS. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default. If enabling SSO, then "Create Alias" need to be set to true.
"""
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class pCreateAlias:
    """A unique alias to assign to the Microsoft Active Directory in AWS. AWS Directory Service uses the alias to construct the access URL for the directory, such as http://alias.awsapps.com. By default, AWS CloudFormation does not create an alias.
"""

    resource: Parameter
    type = STRING
    description = """A unique alias to assign to the Microsoft Active Directory in AWS. AWS Directory Service uses the alias to construct the access URL for the directory, such as http://alias.awsapps.com. By default, AWS CloudFormation does not create an alias.
"""
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class pPrivateSubnet1:
    """A subnet within the selected VPC. Each subnet must be in different Availability Zones (AZs). AWS Directory Service creates a directory server and a DNS server in each subnet.
"""

    resource: Parameter
    type = SUBNET_ID
    description = """A subnet within the selected VPC. Each subnet must be in different Availability Zones (AZs). AWS Directory Service creates a directory server and a DNS server in each subnet.
"""


class pPrivateSubnet2:
    """A second subnet in same VPC that is in different AZ. Each subnet must be in different Availability Zones (AZs). AWS Directory Service creates a directory server and a DNS server in each subnet.
"""

    resource: Parameter
    type = SUBNET_ID
    description = """A second subnet in same VPC that is in different AZ. Each subnet must be in different Availability Zones (AZs). AWS Directory Service creates a directory server and a DNS server in each subnet.
"""


class pVPCID:
    """The VPC ID in which to create the Microsoft Active Directory server.
"""

    resource: Parameter
    type = VPC_ID
    description = """The VPC ID in which to create the Microsoft Active Directory server.
"""


class cAliasCondition:
    resource: TemplateCondition
    logical_id = 'cAlias'
    expression = Equals(pCreateAlias, 'true')
