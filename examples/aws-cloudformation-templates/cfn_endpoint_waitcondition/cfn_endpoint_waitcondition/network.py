"""Network resources: VPC, BastionSG, PrivateSG, PublicRouteTable, InternetGateway, InternetGatewayAttachment, DefaultPublicRoute, PublicSubnet2, PublicSubnet2RouteTableAssociation, PublicSubnet1, PrivateRouteTable1, PrivateSubnet1, PrivateSubnet1RouteTableAssociation, PrivateRouteTable2, PublicSubnet1RouteTableAssociation, EndpointSG, PrivateSubnet2, CfnEndpoint, PrivateSubnet2RouteTableAssociation, S3Endpoint."""

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


class BastionSGEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = '0.0.0.0/0'


class BastionSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'BastionSG'


class BastionSG:
    resource: ec2.SecurityGroup
    group_description = 'Inbound Bastion Traffic'
    security_group_ingress = [BastionSGEgress]
    vpc_id = VPC
    tags = [BastionSGAssociationParameter]


class PrivateSGIngress:
    resource: ec2.SecurityGroup.Ingress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    source_security_group_id = BastionSG


class PrivateSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'PrivateSG'


class PrivateSG:
    resource: ec2.SecurityGroup
    group_description = 'Traffic from Bastion'
    security_group_ingress = [PrivateSGIngress]
    vpc_id = VPC
    tags = [PrivateSGAssociationParameter]


class PublicRouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Routes')


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PublicRouteTableAssociationParameter]


class InternetGatewayAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = EnvironmentName


class InternetGateway:
    resource: ec2.InternetGateway
    tags = [InternetGatewayAssociationParameter]


class InternetGatewayAttachment:
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class DefaultPublicRoute:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [InternetGatewayAttachment]


class PublicSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Subnet (AZ2)')


class PublicSubnet2:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(1, GetAZs())
    cidr_block = PublicSubnet2CIDR
    map_public_ip_on_launch = True
    tags = [PublicSubnet2AssociationParameter]


class PublicSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class PublicSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Subnet (AZ1)')


class PublicSubnet1:
    resource: ec2.Subnet
    vpc_id = VPC
    availability_zone = Select(0, GetAZs())
    cidr_block = PublicSubnet1CIDR
    map_public_ip_on_launch = True
    tags = [PublicSubnet1AssociationParameter]


class PrivateRouteTable1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ1)')


class PrivateRouteTable1:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable1AssociationParameter]


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


class PrivateSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1


class PrivateRouteTable2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ2)')


class PrivateRouteTable2:
    resource: ec2.RouteTable
    vpc_id = VPC
    tags = [PrivateRouteTable2AssociationParameter]


class PublicSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


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


class CfnEndpoint:
    resource: ec2.VPCEndpoint
    vpc_id = VPC
    service_name = Sub('com.amazonaws.${AWS::Region}.cloudformation')
    vpc_endpoint_type = 'Interface'
    private_dns_enabled = True
    subnet_ids = [PrivateSubnet1, PrivateSubnet2]
    security_group_ids = [EndpointSG]


class PrivateSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


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
