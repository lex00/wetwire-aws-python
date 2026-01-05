"""Network resources: ELBSecurityGroup, InstanceSecurityGroup, EFSSecurityGroup, ElasticLoadBalancer."""

from . import *  # noqa: F403


class ELBSecurityGroupEgress(ec2.SecurityGroup.Egress):
    cidr_ip = '0.0.0.0/0'
    from_port = '80'
    ip_protocol = 'tcp'
    to_port = '80'


class ELBSecurityGroupEgress1(ec2.SecurityGroup.Egress):
    cidr_ip = '0.0.0.0/0'
    from_port = '443'
    ip_protocol = 'tcp'
    to_port = '443'


class ELBSecurityGroup(ec2.SecurityGroup):
    group_description = 'Enable public access HTTP and HTTPS'
    security_group_ingress = [ELBSecurityGroupEgress, ELBSecurityGroupEgress1]
    vpc_id = VPC


class InstanceSecurityGroupEgress(ec2.SecurityGroup.Egress):
    cidr_ip = '0.0.0.0/0'
    from_port = '22'
    ip_protocol = 'tcp'
    to_port = '22'


class InstanceSecurityGroupIngress(ec2.SecurityGroup.Ingress):
    from_port = '80'
    ip_protocol = 'tcp'
    source_security_group_id = ELBSecurityGroup.GroupId
    to_port = '80'


class InstanceSecurityGroup(ec2.SecurityGroup):
    group_description = 'Enable SSH public access and HTTP from the load balancer only'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupIngress]
    vpc_id = VPC


class EFSSecurityGroupIngress(ec2.SecurityGroup.Ingress):
    from_port = '2049'
    ip_protocol = 'tcp'
    to_port = '2049'
    source_security_group_id = InstanceSecurityGroup.GroupId


class EFSSecurityGroup(ec2.SecurityGroup):
    group_description = 'Enable NFS access from EC2'
    security_group_ingress = [EFSSecurityGroupIngress]
    vpc_id = VPC


class ElasticLoadBalancerHealthCheck(elasticloadbalancing.LoadBalancer.HealthCheck):
    healthy_threshold = '3'
    interval = '30'
    target = Join('', [
    'HTTP:',
    '80',
    '/',
])
    timeout = '5'
    unhealthy_threshold = '5'


class ElasticLoadBalancerListeners(elasticloadbalancing.LoadBalancer.Listeners):
    instance_port = '80'
    load_balancer_port = '80'
    protocol = 'HTTP'


class ElasticLoadBalancer(elasticloadbalancing.LoadBalancer):
    security_groups = [ELBSecurityGroup]
    subnets = Subnets
    cross_zone = 'true'
    health_check = ElasticLoadBalancerHealthCheck
    listeners = [ElasticLoadBalancerListeners]
