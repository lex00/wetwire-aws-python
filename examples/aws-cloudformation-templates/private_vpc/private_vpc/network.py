"""Network resources: VPC, PublicSubnetTwo, PublicRouteTable, PublicSubnetTwoRouteTableAssociation, PrivateRouteTableOne, InternetGateway, GatewayAttachement, NatGatewayOneAttachment, PublicSubnetOne, NatGatewayOne, PrivateRouteOne, PublicSubnetOneRouteTableAssociation, DummyTargetGroupPublic, PrivateRouteTableTwo, PrivateSubnetTwo, PrivateRouteTableTwoAssociation, DummyTargetGroupPrivate, PrivateSubnetOne, PrivateLoadBalancerSG, PrivateLoadBalancer, PrivateLoadBalancerListener, PublicLoadBalancerSG, PublicLoadBalancer, EcsHostSecurityGroup, EcsSecurityGroupIngressFromPublicALB, NatGatewayTwoAttachment, NatGatewayTwo, DynamoDBEndpoint, PublicLoadBalancerListener, PublicRoute, PrivateLoadBalancerIngressFromECS, EcsSecurityGroupIngressFromPrivateALB, PrivateRouteTwo, EcsSecurityGroupIngressFromSelf, PrivateRouteTableOneAssociation."""

from . import *  # noqa: F403


class VPC:
    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')


class PublicSubnetTwo:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicTwo', 'CIDR')
    map_public_ip_on_launch = True


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnetTwoRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetTwo
    route_table_id = PublicRouteTable


class PrivateRouteTableOne:
    resource: ec2.RouteTable
    vpc_id = VPC


class InternetGateway:
    resource: ec2.InternetGateway


class GatewayAttachement:
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class NatGatewayOneAttachment:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class PublicSubnetOne:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True


class NatGatewayOne:
    resource: ec2.NatGateway
    allocation_id = NatGatewayOneAttachment.AllocationId
    subnet_id = PublicSubnetOne


class PrivateRouteOne:
    resource: ec2.Route
    route_table_id = PrivateRouteTableOne
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayOne


class PublicSubnetOneRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetOne
    route_table_id = PublicRouteTable


class DummyTargetGroupPublic:
    resource: elasticloadbalancingv2.TargetGroup
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


class PrivateRouteTableTwo:
    resource: ec2.RouteTable
    vpc_id = VPC


class PrivateSubnetTwo:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateTwo', 'CIDR')


class PrivateRouteTableTwoAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTableTwo
    subnet_id = PrivateSubnetTwo


class DummyTargetGroupPrivate:
    resource: elasticloadbalancingv2.TargetGroup
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


class PrivateSubnetOne:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateOne', 'CIDR')


class PrivateLoadBalancerSG:
    resource: ec2.SecurityGroup
    group_description = 'Access to the internal load balancer'
    vpc_id = VPC


class PrivateLoadBalancerTargetGroupAttribute:
    resource: elasticloadbalancingv2.TargetGroup.TargetGroupAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


class PrivateLoadBalancer:
    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internal'
    load_balancer_attributes = [PrivateLoadBalancerTargetGroupAttribute]
    subnets = [PrivateSubnetOne, PrivateSubnetTwo]
    security_groups = [PrivateLoadBalancerSG]


class PrivateLoadBalancerListenerAction:
    resource: elasticloadbalancingv2.ListenerRule.Action
    target_group_arn = DummyTargetGroupPrivate
    type_ = 'forward'


class PrivateLoadBalancerListener:
    resource: elasticloadbalancingv2.Listener
    default_actions = [PrivateLoadBalancerListenerAction]
    load_balancer_arn = PrivateLoadBalancer
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    depends_on = [PrivateLoadBalancer]


class PublicLoadBalancerSGEgress:
    resource: ec2.SecurityGroup.Egress
    cidr_ip = '0.0.0.0/0'
    ip_protocol = -1


class PublicLoadBalancerSG:
    resource: ec2.SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id = VPC
    security_group_ingress = [PublicLoadBalancerSGEgress]


class PublicLoadBalancerTargetGroupAttribute:
    resource: elasticloadbalancingv2.TargetGroup.TargetGroupAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


class PublicLoadBalancer:
    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internet-facing'
    load_balancer_attributes = [PublicLoadBalancerTargetGroupAttribute]
    subnets = [PublicSubnetOne, PublicSubnetTwo]
    security_groups = [PublicLoadBalancerSG]


class EcsHostSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Access to the ECS hosts that run containers'
    vpc_id = VPC


class EcsSecurityGroupIngressFromPublicALB:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = PublicLoadBalancerSG


class NatGatewayTwoAttachment:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class NatGatewayTwo:
    resource: ec2.NatGateway
    allocation_id = NatGatewayTwoAttachment.AllocationId
    subnet_id = PublicSubnetTwo


class DynamoDBEndpointAllowStatement0:
    resource: PolicyStatement
    principal = '*'
    action = '*'
    resource_arn = '*'


class DynamoDBEndpointPolicyDocument:
    resource: PolicyDocument
    statement = [DynamoDBEndpointAllowStatement0]


class DynamoDBEndpoint:
    resource: ec2.VPCEndpoint
    policy_document = DynamoDBEndpointPolicyDocument
    route_table_ids = [PrivateRouteTableOne, PrivateRouteTableTwo]
    service_name = Join('', [
    'com.amazonaws.',
    AWS_REGION,
    '.dynamodb',
])
    vpc_id = VPC


class PublicLoadBalancerListenerAction:
    resource: elasticloadbalancingv2.ListenerRule.Action
    target_group_arn = DummyTargetGroupPublic
    type_ = 'forward'


class PublicLoadBalancerListener:
    resource: elasticloadbalancingv2.Listener
    default_actions = [PublicLoadBalancerListenerAction]
    load_balancer_arn = PublicLoadBalancer
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    depends_on = [PublicLoadBalancer]


class PublicRoute:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [GatewayAttachement]


class PrivateLoadBalancerIngressFromECS:
    resource: ec2.SecurityGroupIngress
    description = 'Only accept traffic from a container in the container host security group'
    group_id = PrivateLoadBalancerSG
    ip_protocol = -1
    source_security_group_id = EcsHostSecurityGroup


class EcsSecurityGroupIngressFromPrivateALB:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the private ALB'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = PrivateLoadBalancerSG


class PrivateRouteTwo:
    resource: ec2.Route
    route_table_id = PrivateRouteTableTwo
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayTwo


class EcsSecurityGroupIngressFromSelf:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = EcsHostSecurityGroup


class PrivateRouteTableOneAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTableOne
    subnet_id = PrivateSubnetOne
