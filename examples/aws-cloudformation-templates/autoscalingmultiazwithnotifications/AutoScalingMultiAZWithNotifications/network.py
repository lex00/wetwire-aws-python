"""Network resources: LoadBalancerSecurityGroup, InstanceSecurityGroup, ElasticLoadBalancer, TargetGroup, LoadBalancerListener."""

from . import *  # noqa: F403


class LoadBalancerSecurityGroupEgress(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


class LoadBalancerSecurityGroup(ec2.SecurityGroup):
    group_description = 'Allows inbound traffic on port 443'
    security_group_ingress = [LoadBalancerSecurityGroupEgress]
    vpc_id = VPC


class InstanceSecurityGroupEgress(ec2.SecurityGroup.Egress):
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = SSHLocation


class InstanceSecurityGroupIngress(ec2.SecurityGroup.Ingress):
    ip_protocol = 'tcp'
    from_port = 80
    to_port = 80
    source_security_group_id = LoadBalancerSecurityGroup


class InstanceSecurityGroup(ec2.SecurityGroup):
    group_description = 'Enable SSH access and HTTP from the load balancer only'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupIngress]


class ElasticLoadBalancer(elasticloadbalancingv2.LoadBalancer):
    scheme = 'internet-facing'
    security_groups = [LoadBalancerSecurityGroup]
    subnets = Subnets
    type_ = 'application'


class TargetGroup(elasticloadbalancingv2.TargetGroup):
    health_check_path = '/'
    name = 'MyTargetGroup'
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    target_type = elasticloadbalancingv2.TargetTypeEnum.INSTANCE
    vpc_id = VPC


class LoadBalancerListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    type_ = 'forward'
    target_group_arn = TargetGroup


class LoadBalancerListenerCertificate(elasticloadbalancingv2.ListenerCertificate.Certificate):
    certificate_arn = CertificateArn


class LoadBalancerListener(elasticloadbalancingv2.Listener):
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn = ElasticLoadBalancer
    port = 443
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTPS
    ssl_policy = 'ELBSecurityPolicy-2016-08'
    certificates = [LoadBalancerListenerCertificate]
