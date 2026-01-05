"""Network resources: VPC, PrivateLoadBalancerSG, EcsHostSecurityGroup, EcsSecurityGroupIngressFromPrivateALB, EcsSecurityGroupIngressFromSelf, InternetGateway, GatewayAttachement, DummyTargetGroupPublic, PublicSubnetOne, PublicSubnetTwo, PublicLoadBalancerSG, PublicLoadBalancer, PublicLoadBalancerListener, PrivateRouteTableOne, PrivateRouteTableTwo, DynamoDBEndpoint, PrivateSubnetTwo, PublicRouteTable, PublicRoute, NatGatewayOneAttachment, NatGatewayOne, NatGatewayTwoAttachment, PrivateSubnetOne, EcsSecurityGroupIngressFromPublicALB, PrivateLoadBalancer, DummyTargetGroupPrivate, PrivateLoadBalancerListener, PrivateRouteTableTwoAssociation, PrivateLoadBalancerIngressFromECS, PrivateRouteOne, NatGatewayTwo, PrivateRouteTwo, PublicSubnetTwoRouteTableAssociation, PublicSubnetOneRouteTableAssociation, PrivateRouteTableOneAssociation."""

from . import *  # noqa: F403


class VPC:
    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')


class PrivateLoadBalancerSG:
    resource: ec2.SecurityGroup
    group_description = 'Access to the internal load balancer'
    vpc_id = VPC


class EcsHostSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Access to the ECS hosts that run containers'
    vpc_id = VPC


class EcsSecurityGroupIngressFromPrivateALB:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the private ALB'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = PrivateLoadBalancerSG


class EcsSecurityGroupIngressFromSelf:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = EcsHostSecurityGroup


class InternetGateway:
    resource: ec2.InternetGateway


class GatewayAttachement:
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


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


class PublicSubnetOne:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True


class PublicSubnetTwo:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicTwo', 'CIDR')
    map_public_ip_on_launch = True


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


class PrivateRouteTableOne:
    resource: ec2.RouteTable
    vpc_id = VPC


class PrivateRouteTableTwo:
    resource: ec2.RouteTable
    vpc_id = VPC


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


class PrivateSubnetTwo:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateTwo', 'CIDR')


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicRoute:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [GatewayAttachement]


class NatGatewayOneAttachment:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class NatGatewayOne:
    resource: ec2.NatGateway
    allocation_id = NatGatewayOneAttachment.AllocationId
    subnet_id = PublicSubnetOne


class NatGatewayTwoAttachment:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class PrivateSubnetOne:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateOne', 'CIDR')


class EcsSecurityGroupIngressFromPublicALB:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = PublicLoadBalancerSG


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


class PrivateRouteTableTwoAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTableTwo
    subnet_id = PrivateSubnetTwo


class PrivateLoadBalancerIngressFromECS:
    resource: ec2.SecurityGroupIngress
    description = 'Only accept traffic from a container in the container host security group'
    group_id = PrivateLoadBalancerSG
    ip_protocol = -1
    source_security_group_id = EcsHostSecurityGroup


class PrivateRouteOne:
    resource: ec2.Route
    route_table_id = PrivateRouteTableOne
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayOne


class NatGatewayTwo:
    resource: ec2.NatGateway
    allocation_id = NatGatewayTwoAttachment.AllocationId
    subnet_id = PublicSubnetTwo


class PrivateRouteTwo:
    resource: ec2.Route
    route_table_id = PrivateRouteTableTwo
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayTwo


class PublicSubnetTwoRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetTwo
    route_table_id = PublicRouteTable


class PublicSubnetOneRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetOne
    route_table_id = PublicRouteTable


class PrivateRouteTableOneAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTableOne
    subnet_id = PrivateSubnetOne
