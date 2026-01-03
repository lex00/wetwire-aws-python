"""Stack resources."""

from . import *  # noqa: F403


class ADConnectorResource:
    # Unknown resource type: Custom::ADConnectorResource
    resource: CloudFormationResource
    service_token = ADConnectorLambdaFunction.Arn
    adconnector_description = ADConnectorDescription
    adconnector_size = ADConnectorSize
    adconnector_subnet_id1 = PrivateSubnet1ID
    adconnector_subnet_id2 = PrivateSubnet2ID
    adconnector_vpcid = VPCID
    domain_dns_name = DomainDNSName
    domain_dns_servers = DomainDNSServers
    domain_netbios_name = DomainNetBiosName
    domain_join_secret_id = ADConnectorServiceAccountSecret
