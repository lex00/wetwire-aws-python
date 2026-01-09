"""Network resources: VPC, EcsHostSecurityGroup, PublicLoadBalancerSG, EcsSecurityGroupIngressFromPublicALB, PublicSubnetOne, PublicSubnetTwo, DummyTargetGroupPublic, PublicLoadBalancer, PublicLoadBalancerListener, PublicRouteTable, EcsSecurityGroupIngressFromSelf, InternetGateway, GatewayAttachement, PublicRoute, PublicSubnetTwoRouteTableAssociation, PublicSubnetOneRouteTableAssociation."""

from . import *  # noqa: F403


class VPC(ec2.VPC):
    enable_dns_support = True
    enable_dns_hostnames = True
    cidr_block = FindInMap("SubnetConfig", 'VPC', 'CIDR')


class EcsHostSecurityGroup(ec2.SecurityGroup):
    group_description = 'Access to the ECS hosts that run containers'
    vpc_id = VPC


class PublicLoadBalancerSGEgress(ec2.SecurityGroup.Egress):
    cidr_ip = '0.0.0.0/0'
    ip_protocol = -1


class PublicLoadBalancerSG(ec2.SecurityGroup):
    group_description = 'Access to the public facing load balancer'
    vpc_id = VPC
    security_group_ingress = [PublicLoadBalancerSGEgress]


class EcsSecurityGroupIngressFromPublicALB(ec2.SecurityGroupIngress):
    description = 'Ingress from the public ALB'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = PublicLoadBalancerSG


class PublicSubnetOne(ec2.Subnet):
    availability_zone = Select(0, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True


class PublicSubnetTwo(ec2.Subnet):
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = VPC
    cidr_block = FindInMap("SubnetConfig", 'PublicTwo', 'CIDR')
    map_public_ip_on_launch = True


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


class PublicRouteTable(ec2.RouteTable):
    vpc_id = VPC


class EcsSecurityGroupIngressFromSelf(ec2.SecurityGroupIngress):
    description = 'Ingress from other hosts in the same security group'
    group_id = EcsHostSecurityGroup
    ip_protocol = -1
    source_security_group_id = EcsHostSecurityGroup


class InternetGateway(ec2.InternetGateway):
    pass


class GatewayAttachement(ec2.VPCGatewayAttachment):
    vpc_id = VPC
    internet_gateway_id = InternetGateway


class PublicRoute(ec2.Route):
    route_table_id = PublicRouteTable
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = InternetGateway
    depends_on = [GatewayAttachement]


class PublicSubnetTwoRouteTableAssociation(ec2.SubnetRouteTableAssociation):
    subnet_id = PublicSubnetTwo
    route_table_id = PublicRouteTable


class PublicSubnetOneRouteTableAssociation(ec2.SubnetRouteTableAssociation):
    subnet_id = PublicSubnetOne
    route_table_id = PublicRouteTable
