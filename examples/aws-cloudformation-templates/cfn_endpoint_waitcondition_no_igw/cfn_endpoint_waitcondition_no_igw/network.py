"""Network resources: VPC, PrivateRouteTable1, PrivateRouteTable2, S3Endpoint, PrivateSubnet2, PrivateSubnet2RouteTableAssociation, EndpointSG, PrivateSubnet1, CfnEndpoint, PrivateSubnet1RouteTableAssociation, PrivateSG."""

from . import *  # noqa: F403


class VPCAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = EnvironmentName


class VPC:
    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = VpcCIDR
    tags = [VPCAssociationParameter]


class PrivateRouteTable1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ1)')


class PrivateRouteTable1:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable1AssociationParameter]


class PrivateRouteTable2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ2)')


class PrivateRouteTable2:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable2AssociationParameter]


class S3EndpointAllowStatement0:
    resource: PolicyStatement
    principal = '*'
    action = ['s3:PutObject']
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::cloudformation-waitcondition-${AWS::Region}/*')]


class S3EndpointPolicyDocument:
    resource: PolicyDocument
    statement = [S3EndpointAllowStatement0]


class S3Endpoint:
    resource: ec2.VPCEndpoint
    vpc_id = VPC
    service_name = Sub('com.amazonaws.${AWS::Region}.s3')
    vpc_endpoint_type = 'Gateway'
    policy_document = S3EndpointPolicyDocument
    route_table_ids = [PrivateRouteTable1, PrivateRouteTable2]


class PrivateSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ2)')


class PrivateSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, GetAZs())
    cidr_block = PrivateSubnet2CIDR
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]


class PrivateSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


class EndpointSGEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


class EndpointSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'EndpointSG'


class EndpointSG:
    resource: ec2.SecurityGroup
    group_description = 'Traffic into CloudFormation Endpoint'
    security_group_ingress = [EndpointSGEgress]
    vpc_id = VPC
    tags = [EndpointSGAssociationParameter]


class PrivateSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ1)')


class PrivateSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, GetAZs())
    cidr_block = PrivateSubnet1CIDR
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]


class CfnEndpoint:
    resource: ec2.VPCEndpoint
    vpc_id = VPC
    service_name = Sub('com.amazonaws.${AWS::Region}.cloudformation')
    vpc_endpoint_type = 'Interface'
    private_dns_enabled = True
    subnet_ids = [PrivateSubnet1, PrivateSubnet2]
    security_group_ids = [EndpointSG]


class PrivateSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1


class PrivateSGEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = VpcCIDR


class PrivateSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'PrivateSG'


class PrivateSG:
    resource: ec2.SecurityGroup
    group_description = 'Traffic from Bastion'
    security_group_ingress = [PrivateSGEgress]
    vpc_id = VPC
    tags = [PrivateSGAssociationParameter]
