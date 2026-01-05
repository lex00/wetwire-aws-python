"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DomainName:
    """The fully qualified or wildcard domain name of DNS"""

    resource: Parameter
    type = STRING
    description = 'The fully qualified or wildcard domain name of DNS'


class HostedZone:
    """The public hostedZone of above domain name"""

    resource: Parameter
    type = HOSTED_ZONE_ID
    description = 'The public hostedZone of above domain name'


class VpcId:
    """VpcId of your existing Virtual Private Cloud (VPC) where SAP resides"""

    resource: Parameter
    type = VPC_ID
    description = 'VpcId of your existing Virtual Private Cloud (VPC) where SAP resides'


class Subnets:
    """The private subnets (must include one where SAP resides) of above VPC, recommend choose multiple covering different AZs"""

    resource: Parameter
    type = LIST_SUBNET_ID
    description = 'The private subnets (must include one where SAP resides) of above VPC, recommend choose multiple covering different AZs'


class SecurityGroups:
    resource: Parameter
    type = LIST_SECURITY_GROUP_ID


class IP:
    """SAP Gateway's private IP address within VPC"""

    resource: Parameter
    type = STRING
    description = "SAP Gateway's private IP address within VPC"


class Protocol:
    """SAP Gateway's connect protocol"""

    resource: Parameter
    type = STRING
    description = "SAP Gateway's connect protocol"
    default = 'HTTP'
    allowed_values = [
    'HTTP',
    'HTTPS',
]


class Port:
    """SAP Gateway's HTTP or HTTPS (match with protocol you choose above) port number"""

    resource: Parameter
    type = NUMBER
    description = "SAP Gateway's HTTP or HTTPS (match with protocol you choose above) port number"
    default = 50000


class HealthCheckPath:
    """SAP Gateway's ping path to do health check"""

    resource: Parameter
    type = STRING
    description = "SAP Gateway's ping path to do health check"
    default = '/sap/public/ping'


class InVpc:
    """Choose Yes if SAP resides in above VPC; choose No otherwise (in cases of above VPC just peers with another SAP residing VPC)"""

    resource: Parameter
    type = STRING
    description = 'Choose Yes if SAP resides in above VPC; choose No otherwise (in cases of above VPC just peers with another SAP residing VPC)'
    default = True
    allowed_values = [
    True,
    False,
]


class IpInVpcCondition:
    resource: TemplateCondition
    logical_id = 'IpInVpc'
    expression = Equals(InVpc, True)


class SapUseHttpsCondition:
    resource: TemplateCondition
    logical_id = 'SapUseHttps'
    expression = Equals(Protocol, 'HTTPS')
