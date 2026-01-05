"""Network resources: ADConnectorDomainMembersSG, DHCPOptions, DHCPOptionsVPCAssociation."""

from . import *  # noqa: F403


class ADConnectorDomainMembersSGEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '10.0.0.0/8'


class ADConnectorDomainMembersSGEgress1:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '172.16.0.0/12'


class ADConnectorDomainMembersSGEgress2:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = '-1'
    description = 'LAB - Allow All Private IP Communications'
    cidr_ip = '192.168.0.0/16'


class ADConnectorDomainMembersSGEgress3:
    resource: ec2.SecurityGroup.Egress
    description = 'Allow All Outbound Communications'
    ip_protocol = '-1'
    cidr_ip = '0.0.0.0/0'


class ADConnectorDomainMembersSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${DomainNetBiosName}-DomainMembersSG-ADConnector')


class ADConnectorDomainMembersSG(ec2.SecurityGroup):
    group_description = Sub('${DomainNetBiosName} Domain Members SG via AD Connector')
    vpc_id = VPCID
    security_group_ingress = [ADConnectorDomainMembersSGEgress, ADConnectorDomainMembersSGEgress1, ADConnectorDomainMembersSGEgress2]
    security_group_egress = [ADConnectorDomainMembersSGEgress3]
    tags = [ADConnectorDomainMembersSGAssociationParameter]
    condition = 'DomainMembersSGCondition'


class DHCPOptionsAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = DomainDNSName


class DHCPOptions(ec2.DHCPOptions):
    domain_name = DomainDNSName
    domain_name_servers = [DomainDNSServers]
    tags = [DHCPOptionsAssociationParameter]
    condition = 'DHCPOptionSetCondition'


class DHCPOptionsVPCAssociation(ec2.VPCDHCPOptionsAssociation):
    vpc_id = VPCID
    dhcp_options_id = DHCPOptions
    condition = 'DHCPOptionSetCondition'
