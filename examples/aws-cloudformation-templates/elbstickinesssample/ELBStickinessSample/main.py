"""Stack resources."""

from . import *  # noqa: F403


class ElasticLoadBalancerLBCookieStickinessPolicy(elasticloadbalancing.LoadBalancer.LBCookieStickinessPolicy):
    policy_name = 'myLBPolicy'
    cookie_expiration_period = '180'


class ElasticLoadBalancerListeners(elasticloadbalancing.LoadBalancer.Listeners):
    load_balancer_port = '80'
    instance_port = '80'
    protocol = 'HTTP'
    policy_names = ['myLBPolicy']


class ElasticLoadBalancerHealthCheck(elasticloadbalancing.LoadBalancer.HealthCheck):
    target = 'HTTP:80/'
    healthy_threshold = '3'
    unhealthy_threshold = '5'
    interval = '30'
    timeout = '5'


class ElasticLoadBalancer(elasticloadbalancing.LoadBalancer):
    availability_zones = GetAZs()
    cross_zone = 'true'
    instances = [EC2Instance1, EC2Instance2]
    lb_cookie_stickiness_policy = [ElasticLoadBalancerLBCookieStickinessPolicy]
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck
