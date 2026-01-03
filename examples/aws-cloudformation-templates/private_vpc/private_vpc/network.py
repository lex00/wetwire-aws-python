"""Network resources: InternetGateway, VPC, GatewayAttachement, PrivateSubnetTwo, PublicSubnetOne, PublicRouteTable, PublicSubnetTwo, PublicSubnetTwoRouteTableAssociation, FargateContainerSecurityGroup, NatGatewayTwoAttachment, PublicLoadBalancerSG, EcsSecurityGroupIngressFromPublicALB, NatGatewayTwo, PrivateLoadBalancerSG, PrivateRouteTableOne, PrivateRouteTableTwo, DynamoDBEndpoint, NatGatewayOneAttachment, NatGatewayOne, PublicLoadBalancer, DummyTargetGroupPublic, PublicLoadBalancerListener, PrivateSubnetOne, PrivateLoadBalancer, PrivateLoadBalancerIngressFromECS, DummyTargetGroupPrivate, PrivateLoadBalancerListener, PrivateRouteTwo, PublicRoute, PublicSubnetOneRouteTableAssociation, PrivateRouteTableTwoAssociation, PrivateRouteTableOneAssociation, PrivateRouteOne, EcsSecurityGroupIngressFromPrivateALB, EcsSecurityGroupIngressFromSelf."""

from . import *  # noqa: F403


class InternetGateway:
    resource: ec2.InternetGateway


class VPC:
    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')


class GatewayAttachement:
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class PrivateSubnetTwo:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateTwo', 'CIDR')


class PublicSubnetOne:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnetTwo:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicTwo', 'CIDR')
    map_public_ip_on_launch = True


class PublicSubnetTwoRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetTwo
    route_table_id = PublicRouteTable


class FargateContainerSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Access to the Fargate containers'
    vpc_id = VPC


class NatGatewayTwoAttachment:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class PublicLoadBalancerSGEgress:
    resource: ec2.SecurityGroup.Egress
    cidr_ip = '0.0.0.0/0'
    ip_protocol = '-1'


class PublicLoadBalancerSG:
    resource: ec2.SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id = VPC
    security_group_ingress = [PublicLoadBalancerSGEgress]


class EcsSecurityGroupIngressFromPublicALB:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id = FargateContainerSecurityGroup
    ip_protocol = '-1'
    source_security_group_id = PublicLoadBalancerSG


class NatGatewayTwo:
    resource: ec2.NatGateway
    allocation_id = NatGatewayTwoAttachment.AllocationId
    subnet_id = PublicSubnetTwo


class PrivateLoadBalancerSG:
    resource: ec2.SecurityGroup
    group_description = 'Access to the internal load balancer'
    vpc_id = VPC


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


class NatGatewayOneAttachment:
    resource: ec2.EIP
    domain = 'vpc'
    depends_on = [GatewayAttachement]


class NatGatewayOne:
    resource: ec2.NatGateway
    allocation_id = NatGatewayOneAttachment.AllocationId
    subnet_id = PublicSubnetOne


class PublicLoadBalancerListenerAttribute:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


class PublicLoadBalancer:
    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internet-facing'
    load_balancer_attributes = [PublicLoadBalancerListenerAttribute]
    subnets = [PublicSubnetOne, PublicSubnetTwo]
    security_groups = [PublicLoadBalancerSG]
    depends_on = [GatewayAttachement]


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


class PublicLoadBalancerListenerAction:
    resource: elasticloadbalancingv2.Listener.Action
    target_group_arn = DummyTargetGroupPublic
    type_ = 'forward'


class PublicLoadBalancerListener:
    resource: elasticloadbalancingv2.Listener
    default_actions = [PublicLoadBalancerListenerAction]
    load_balancer_arn = PublicLoadBalancer
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP


class PrivateSubnetOne:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PrivateOne', 'CIDR')


class PrivateLoadBalancerListenerAttribute:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


class PrivateLoadBalancer:
    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internal'
    load_balancer_attributes = [PrivateLoadBalancerListenerAttribute]
    subnets = [PrivateSubnetOne, PrivateSubnetTwo]
    security_groups = [PrivateLoadBalancerSG]


class PrivateLoadBalancerIngressFromECS:
    resource: ec2.SecurityGroupIngress
    description = 'Only accept traffic from a container in the fargate container security group'
    group_id = PrivateLoadBalancerSG
    ip_protocol = '-1'
    source_security_group_id = FargateContainerSecurityGroup


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
    resource: elasticloadbalancingv2.Listener.Action
    target_group_arn = DummyTargetGroupPrivate
    type_ = 'forward'


class PrivateLoadBalancerListener:
    resource: elasticloadbalancingv2.Listener
    default_actions = [PrivateLoadBalancerListenerAction]
    load_balancer_arn = PrivateLoadBalancer
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP


class PrivateRouteTwo:
    resource: ec2.Route
    route_table_id = PrivateRouteTableTwo
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayTwo


class PublicRoute:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [GatewayAttachement]


class PublicSubnetOneRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetOne
    route_table_id = PublicRouteTable


class PrivateRouteTableTwoAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTableTwo
    subnet_id = PrivateSubnetTwo


class PrivateRouteTableOneAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = PrivateRouteTableOne
    subnet_id = PrivateSubnetOne


class PrivateRouteOne:
    resource: ec2.Route
    route_table_id = PrivateRouteTableOne
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NatGatewayOne


class EcsSecurityGroupIngressFromPrivateALB:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the private ALB'
    group_id = FargateContainerSecurityGroup
    ip_protocol = '-1'
    source_security_group_id = PrivateLoadBalancerSG


class EcsSecurityGroupIngressFromSelf:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = FargateContainerSecurityGroup
    ip_protocol = '-1'
    source_security_group_id = FargateContainerSecurityGroup
