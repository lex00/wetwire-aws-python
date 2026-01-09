"""Network resources: VPC, DummyTargetGroupPublic, PrivateRouteTableOne, EcsHostSecurityGroup, PrivateSubnetTwo, PrivateSubnetOne, PrivateRouteTableTwo, DynamoDBEndpoint, InternetGateway, PublicRouteTable, GatewayAttachement, NatGatewayOneAttachment, PublicSubnetOne, NatGatewayOne, PrivateRouteOne, DummyTargetGroupPrivate, PrivateLoadBalancerSG, EcsSecurityGroupIngressFromPrivateALB, PublicLoadBalancerSG, PublicSubnetTwo, PublicLoadBalancer, PublicLoadBalancerListener, EcsSecurityGroupIngressFromPublicALB, PrivateRouteTableTwoAssociation, PrivateRouteTableOneAssociation, PublicSubnetOneRouteTableAssociation, EcsSecurityGroupIngressFromSelf, PrivateLoadBalancer, PrivateLoadBalancerListener, NatGatewayTwoAttachment, PublicRoute, NatGatewayTwo, PrivateRouteTwo, PublicSubnetTwoRouteTableAssociation, PrivateLoadBalancerIngressFromECS."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')


class DummyTargetGroupPublic(elasticloadbalancingv2.TargetGroup):
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = Join('-', [
    AWS_STACK_NAME,
    'drop-1',
])
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    unhealthy_threshold_count = 2
    vpc_id = VPC


class PrivateRouteTableOne(ec2.RouteTable):
    vpc_id = VPC


class EcsHostSecurityGroup(ec2.SecurityGroup):
    group_description = 'Access to the ECS hosts that run containers'
    vpc_id = VPC


class PrivateSubnetTwo(ec2.Subnet):
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateTwo', 'CIDR')


class PrivateSubnetOne(ec2.Subnet):
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateOne', 'CIDR')


class PrivateRouteTableTwo(ec2.RouteTable):
    vpc_id = VPC


class DynamoDBEndpointAllowStatement0(PolicyStatement):
    principal = '*'
    action = '*'
    resource_arn = '*'


class DynamoDBEndpointPolicyDocument(PolicyDocument):
    statement = [DynamoDBEndpointAllowStatement0]


class DynamoDBEndpoint(ec2.VPCEndpoint):
    policy_document = DynamoDBEndpointPolicyDocument
    route_table_ids = [PrivateRouteTableOne, PrivateRouteTableTwo]
    service_name = Join('', [
    'com.amazonaws.',
    AWS_REGION,
    '.dynamodb',
])
    vpc_id = VPC


class InternetGateway(ec2.InternetGateway):
    pass


class PublicRouteTable(ec2.RouteTable):
    vpc_id = VPC


class GatewayAttachement(ec2.VPCGatewayAttachment):
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class NatGatewayOneAttachment(ec2.EIP):
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class PublicSubnetOne(ec2.Subnet):
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True


class NatGatewayOne(ec2.NatGateway):
    allocation_id = NatGatewayOneAttachment.AllocationId
    subnet_id = PublicSubnetOne


class PrivateRouteOne(ec2.Route):
    route_table_id = PrivateRouteTableOne
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayOne


class DummyTargetGroupPrivate(elasticloadbalancingv2.TargetGroup):
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = Join('-', [
    AWS_STACK_NAME,
    'drop-2',
])
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    unhealthy_threshold_count = 2
    vpc_id = VPC


class PrivateLoadBalancerSG(ec2.SecurityGroup):
    group_description = 'Access to the internal load balancer'
    vpc_id = VPC


class EcsSecurityGroupIngressFromPrivateALB(ec2.SecurityGroupIngress):
    description = 'Ingress from the private ALB'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = PrivateLoadBalancerSG


class PublicLoadBalancerSGEgress(ec2.SecurityGroup.Egress):
    cidr_ip = '0.0.0.0/0'
    ip_protocol = -1


class PublicLoadBalancerSG(ec2.SecurityGroup):
    group_description = 'Access to the public facing load balancer'
    vpc_id = VPC
    security_group_ingress = [PublicLoadBalancerSGEgress]


class PublicSubnetTwo(ec2.Subnet):
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicTwo', 'CIDR')
    map_public_ip_on_launch = True


class PublicLoadBalancerTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'idle_timeout.timeout_seconds'
    value = '30'


class PublicLoadBalancer(elasticloadbalancingv2.LoadBalancer):
    scheme = 'internet-facing'
    load_balancer_attributes = [PublicLoadBalancerTargetGroupAttribute]
    subnets = [PublicSubnetOne, PublicSubnetTwo]
    security_groups = [PublicLoadBalancerSG]


class PublicLoadBalancerListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    target_group_arn = DummyTargetGroupPublic
    type_ = 'forward'


class PublicLoadBalancerListener(elasticloadbalancingv2.Listener):
    default_actions = [PublicLoadBalancerListenerAction]
    load_balancer_arn = PublicLoadBalancer
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    depends_on = [PublicLoadBalancer]


class EcsSecurityGroupIngressFromPublicALB(ec2.SecurityGroupIngress):
    description = 'Ingress from the public ALB'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = PublicLoadBalancerSG


class PrivateRouteTableTwoAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTableTwo
    subnet_id = PrivateSubnetTwo


class PrivateRouteTableOneAssociation(ec2.SubnetRouteTableAssociation):
    route_table_id = PrivateRouteTableOne
    subnet_id = PrivateSubnetOne


class PublicSubnetOneRouteTableAssociation(ec2.SubnetRouteTableAssociation):
    subnet_id = PublicSubnetOne
    route_table_id = PublicRouteTable


class EcsSecurityGroupIngressFromSelf(ec2.SecurityGroupIngress):
    description = 'Ingress from other containers in the same security group'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = EcsHostSecurityGroup


class PrivateLoadBalancerTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'idle_timeout.timeout_seconds'
    value = '30'


class PrivateLoadBalancer(elasticloadbalancingv2.LoadBalancer):
    scheme = 'internal'
    load_balancer_attributes = [PrivateLoadBalancerTargetGroupAttribute]
    subnets = [PrivateSubnetOne, PrivateSubnetTwo]
    security_groups = [PrivateLoadBalancerSG]


class PrivateLoadBalancerListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    target_group_arn = DummyTargetGroupPrivate
    type_ = 'forward'


class PrivateLoadBalancerListener(elasticloadbalancingv2.Listener):
    default_actions = [PrivateLoadBalancerListenerAction]
    load_balancer_arn = PrivateLoadBalancer
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    depends_on = [PrivateLoadBalancer]


class NatGatewayTwoAttachment(ec2.EIP):
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class PublicRoute(ec2.Route):
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [GatewayAttachement]


class NatGatewayTwo(ec2.NatGateway):
    allocation_id = NatGatewayTwoAttachment.AllocationId
    subnet_id = PublicSubnetTwo


class PrivateRouteTwo(ec2.Route):
    route_table_id = PrivateRouteTableTwo
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayTwo


class PublicSubnetTwoRouteTableAssociation(ec2.SubnetRouteTableAssociation):
    subnet_id = PublicSubnetTwo
    route_table_id = PublicRouteTable


class PrivateLoadBalancerIngressFromECS(ec2.SecurityGroupIngress):
    description = 'Only accept traffic from a container in the container host security group'
    group_id = PrivateLoadBalancerSG
    ip_protocol = -1
    source_security_group_id = EcsHostSecurityGroup
