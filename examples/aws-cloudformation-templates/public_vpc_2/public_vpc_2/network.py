"""Network resources: VPC, PublicLoadBalancerSG, PublicSubnetOne, PublicSubnetTwo, PublicRouteTable, PublicSubnetTwoRouteTableAssociation, InternetGateway, PublicLoadBalancer, DummyTargetGroupPublic, PublicLoadBalancerListener, FargateContainerSecurityGroup, EcsSecurityGroupIngressFromSelf, GatewayAttachement, PublicSubnetOneRouteTableAssociation, EcsSecurityGroupIngressFromPublicALB, PublicRoute."""

from . import *  # noqa: F403


class VPC:
    resource: ec2.VPC
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')


class PublicLoadBalancerSGEgress:
    resource: ec2.SecurityGroup.Egress
    cidr_ip = '0.0.0.0/0'
    ip_protocol = '-1'


class PublicLoadBalancerSG:
    resource: ec2.SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id = VPC
    security_group_ingress = [PublicLoadBalancerSGEgress]


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


class PublicRouteTable:
    resource: ec2.RouteTable
    vpc_id = VPC


class PublicSubnetTwoRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetTwo
    route_table_id = PublicRouteTable


class InternetGateway:
    resource: ec2.InternetGateway


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


class FargateContainerSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Access to the Fargate containers'
    vpc_id = VPC


class EcsSecurityGroupIngressFromSelf:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id = FargateContainerSecurityGroup
    ip_protocol = '-1'
    source_security_group_id = FargateContainerSecurityGroup


class GatewayAttachement:
    resource: ec2.VPCGatewayAttachment
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class PublicSubnetOneRouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    subnet_id = PublicSubnetOne
    route_table_id = PublicRouteTable


class EcsSecurityGroupIngressFromPublicALB:
    resource: ec2.SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id = FargateContainerSecurityGroup
    ip_protocol = '-1'
    source_security_group_id = PublicLoadBalancerSG


class PublicRoute:
    resource: ec2.Route
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [GatewayAttachement]
