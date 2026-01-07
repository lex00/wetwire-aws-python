"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DomainName(Parameter):
    """The fully qualified or wildcard domain name of DNS"""

    type = STRING
    description = 'The fully qualified or wildcard domain name of DNS'


class HostedZone(Parameter):
    """The public hostedZone of above domain name"""

    type = HOSTED_ZONE_ID
    description = 'The public hostedZone of above domain name'


class VpcId(Parameter):
    """VpcId of your existing Virtual Private Cloud (VPC) where SAP resides"""

    type = VPC_ID
    description = 'VpcId of your existing Virtual Private Cloud (VPC) where SAP resides'


class Subnets(Parameter):
    """The private subnets (must include one where SAP resides) of above VPC, recommend choose multiple covering different AZs"""

    type = LIST_SUBNET_ID
    description = 'The private subnets (must include one where SAP resides) of above VPC, recommend choose multiple covering different AZs'


class SecurityGroups(Parameter):
    type = LIST_SECURITY_GROUP_ID


class IP(Parameter):
    """SAP Gateway's private IP address within VPC"""

    type = STRING
    description = "SAP Gateway's private IP address within VPC"


class Protocol(Parameter):
    """SAP Gateway's connect protocol"""

    type = STRING
    description = "SAP Gateway's connect protocol"
    default = 'HTTP'
    allowed_values = [
    'HTTP',
    'HTTPS',
]


class Port(Parameter):
    """SAP Gateway's HTTP or HTTPS (match with protocol you choose above) port number"""

    type = NUMBER
    description = "SAP Gateway's HTTP or HTTPS (match with protocol you choose above) port number"
    default = 50000


class HealthCheckPath(Parameter):
    """SAP Gateway's ping path to do health check"""

    type = STRING
    description = "SAP Gateway's ping path to do health check"
    default = '/sap/public/ping'


class InVpc(Parameter):
    """Choose Yes if SAP resides in above VPC; choose No otherwise (in cases of above VPC just peers with another SAP residing VPC)"""

    type = STRING
    description = 'Choose Yes if SAP resides in above VPC; choose No otherwise (in cases of above VPC just peers with another SAP residing VPC)'
    default = 'Yes'
    allowed_values = [
    'Yes',
    'No',
]


class IpInVpcCondition(TemplateCondition):
    logical_id = 'IpInVpc'
    expression = Equals(InVpc, 'Yes')


class SapUseHttpsCondition(TemplateCondition):
    logical_id = 'SapUseHttps'
    expression = Equals(Protocol, 'HTTPS')
