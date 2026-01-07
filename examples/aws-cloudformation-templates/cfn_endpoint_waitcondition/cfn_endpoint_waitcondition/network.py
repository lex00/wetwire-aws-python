"""Network resources: VPC, PrivateSubnet1, PrivateRouteTable2, BastionSG, PrivateSubnet2, EndpointSG, CfnEndpoint, PrivateSG, PrivateRouteTable1, PrivateSubnet1RouteTableAssociation, PublicRouteTable, PublicSubnet1, PublicSubnet1RouteTableAssociation, InternetGateway, PublicSubnet2, InternetGatewayAttachment, DefaultPublicRoute, PublicSubnet2RouteTableAssociation, PrivateSubnet2RouteTableAssociation, S3Endpoint."""

from . import *  # noqa: F403


class VPCAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = EnvironmentName


class VPC(ec2.VPC):
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = VpcCIDR
    tags = [VPCAssociationParameter]


class PrivateSubnet1AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ1)')


class PrivateSubnet1(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(0, GetAZs())
    cidr_block = PrivateSubnet1CIDR
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]


class PrivateRouteTable2AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ2)')


class PrivateRouteTable2(ec2.RouteTable):
    vpc_id = VPC
    tags = [PrivateRouteTable2AssociationParameter]


class BastionSGEgress(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = '0.0.0.0/0'


class BastionSGAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'BastionSG'


class BastionSG(ec2.SecurityGroup):
    group_description = 'Inbound Bastion Traffic'
    security_group_ingress = [BastionSGEgress]
    vpc_id = VPC
    tags = [BastionSGAssociationParameter]


class PrivateSubnet2AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ2)')


class PrivateSubnet2(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(1, GetAZs())
    cidr_block = PrivateSubnet2CIDR
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]


class EndpointSGEgress(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


class EndpointSGAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'EndpointSG'


class EndpointSG(ec2.SecurityGroup):
    group_description = 'Traffic into CloudFormation Endpoint'
    security_group_ingress = [EndpointSGEgress]
    vpc_id = VPC
    tags = [EndpointSGAssociationParameter]


class CfnEndpoint(ec2.VPCEndpoint):
    vpc_id = VPC
    service_name = Sub('com.amazonaws.${AWS::Region}.cloudformation')
    vpc_endpoint_type = 'Interface'
    private_dns_enabled = True
    subnet_ids = [PrivateSubnet1, PrivateSubnet2]
    security_group_ids = [EndpointSG]


class PrivateSGIngress(ec2.SecurityGroup.Ingress):
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    source_security_group_id = BastionSG


class PrivateSGAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'PrivateSG'


class PrivateSG(ec2.SecurityGroup):
    group_description = 'Traffic from Bastion'
    security_group_ingress = [PrivateSGIngress]
    vpc_id = VPC
    tags = [PrivateSGAssociationParameter]


class PrivateRouteTable1AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Sub('${EnvironmentName} Private Routes (AZ1)')


class PrivateRouteTable1(ec2.RouteTable):
    vpc_id = VPC
    tags = [PrivateRouteTable1AssociationParameter]


class PrivateSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTable1
    subnet_id = PrivateSubnet1


class PublicRouteTableAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Sub('${EnvironmentName} Public Routes')


class PublicRouteTable(ec2.RouteTable):
    vpc_id = VPC
    tags = [PublicRouteTableAssociationParameter]


class PublicSubnet1AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Sub('${EnvironmentName} Public Subnet (AZ1)')


class PublicSubnet1(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(0, GetAZs())
    cidr_block = PublicSubnet1CIDR
    map_public_ip_on_launch = True
    tags = [PublicSubnet1AssociationParameter]


class PublicSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet1


class InternetGatewayAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = EnvironmentName


class InternetGateway(ec2.InternetGateway):
    tags = [InternetGatewayAssociationParameter]


class PublicSubnet2AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Sub('${EnvironmentName} Public Subnet (AZ2)')


class PublicSubnet2(ec2.Subnet):
    vpc_id = VPC
    availability_zone = Select(1, GetAZs())
    cidr_block = PublicSubnet2CIDR
    map_public_ip_on_launch = True
    tags = [PublicSubnet2AssociationParameter]


class InternetGatewayAttachment(ec2.VPCGatewayAttachment):
    internet_gateway_id = InternetGateway
    vpc_id = VPC


class DefaultPublicRoute(ec2.Route):
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [InternetGatewayAttachment]


class PublicSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PublicRouteTable
    subnet_id = PublicSubnet2


class PrivateSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTable2
    subnet_id = PrivateSubnet2


class S3EndpointAllowStatement0(PolicyStatement):
    principal = '*'
    action = ['s3:PutObject']
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::cloudformation-waitcondition-${AWS::Region}/*')]


class S3EndpointPolicyDocument(PolicyDocument):
    statement = [S3EndpointAllowStatement0]


class S3Endpoint(ec2.VPCEndpoint):
    vpc_id = VPC
    service_name = Sub('com.amazonaws.${AWS::Region}.s3')
    vpc_endpoint_type = 'Gateway'
    policy_document = S3EndpointPolicyDocument
    route_table_ids = [PrivateRouteTable1, PrivateRouteTable2]
