"""Network resources: InstanceSecurityGroup, ElasticLoadBalancer."""

from . import *  # noqa: F403


class InstanceSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = SSHLocation


class InstanceSecurityGroupEgress1:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


class InstanceSecurityGroup(ec2.SecurityGroup):
    group_description = 'Enable SSH access and HTTP access on the configured port'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupEgress1]


class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.LoadBalancer.Listeners
    load_balancer_port = '80'
    instance_port = '80'
    protocol = 'HTTP'


class ElasticLoadBalancerHealthCheck:
    resource: elasticloadbalancing.LoadBalancer.HealthCheck
    target = 'HTTP:80/'
    healthy_threshold = '3'
    unhealthy_threshold = '5'
    interval = '30'
    timeout = '5'


class ElasticLoadBalancerConnectionDrainingPolicy:
    resource: elasticloadbalancing.LoadBalancer.ConnectionDrainingPolicy
    enabled = 'true'
    timeout = '300'


class ElasticLoadBalancerAccessLoggingPolicy:
    resource: elasticloadbalancing.LoadBalancer.AccessLoggingPolicy
    s3_bucket_name = LogsBucket
    s3_bucket_prefix = 'Logs'
    enabled = 'true'
    emit_interval = '60'


class ElasticLoadBalancer(elasticloadbalancing.LoadBalancer):
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck
    connection_draining_policy = ElasticLoadBalancerConnectionDrainingPolicy
    access_logging_policy = ElasticLoadBalancerAccessLoggingPolicy
    depends_on = [LogsBucketPolicy]
