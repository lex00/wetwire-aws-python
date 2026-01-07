"""Network resources: ElasticLoadBalancer, InstanceSecurityGroup."""

from . import *  # noqa: F403


class ElasticLoadBalancerListeners(elasticloadbalancing.LoadBalancer.Listeners):
    load_balancer_port = '80'
    instance_port = '80'
    protocol = 'HTTP'


class ElasticLoadBalancerHealthCheck(elasticloadbalancing.LoadBalancer.HealthCheck):
    target = 'HTTP:80/'
    healthy_threshold = '3'
    unhealthy_threshold = '5'
    interval = '30'
    timeout = '5'


class ElasticLoadBalancer(elasticloadbalancing.LoadBalancer):
    resource: elasticloadbalancing.LoadBalancer
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck


class InstanceSecurityGroupEgress(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = SSHLocation


class InstanceSecurityGroupEgress1(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


class InstanceSecurityGroup(ec2.SecurityGroup):
    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the configured port'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupEgress1]
