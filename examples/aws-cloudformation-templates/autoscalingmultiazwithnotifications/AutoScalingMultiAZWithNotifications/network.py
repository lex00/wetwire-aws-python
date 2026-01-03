"""Network resources: TargetGroup, LoadBalancerSecurityGroup, ElasticLoadBalancer, LoadBalancerListener, InstanceSecurityGroup."""

from . import *  # noqa: F403


class TargetGroup:
    resource: elasticloadbalancingv2.TargetGroup
    health_check_path = '/'
    name = 'MyTargetGroup'
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    target_type = elasticloadbalancingv2.TargetTypeEnum.INSTANCE
    vpc_id = VPC


class LoadBalancerSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


class LoadBalancerSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Allows inbound traffic on port 443'
    security_group_ingress = [LoadBalancerSecurityGroupEgress]
    vpc_id = VPC


class ElasticLoadBalancer:
    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internet-facing'
    security_groups = [LoadBalancerSecurityGroup]
    subnets = Subnets
    type_ = 'application'


class LoadBalancerListenerAction:
    resource: elasticloadbalancingv2.Listener.Action
    type_ = 'forward'
    target_group_arn = TargetGroup


class LoadBalancerListenerCertificate:
    resource: elasticloadbalancingv2.Listener.Certificate
    certificate_arn = CertificateArn


class LoadBalancerListener:
    resource: elasticloadbalancingv2.Listener
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn = ElasticLoadBalancer
    port = 443
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTPS
    ssl_policy = 'ELBSecurityPolicy-2016-08'
    certificates = [LoadBalancerListenerCertificate]


class InstanceSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    ip_protocol = 'tcp'
    from_port = 22
    to_port = 22
    cidr_ip = SSHLocation


class InstanceSecurityGroupIngress:
    resource: ec2.SecurityGroup.Ingress
    ip_protocol = 'tcp'
    from_port = 80
    to_port = 80
    source_security_group_id = LoadBalancerSecurityGroup


class InstanceSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP from the load balancer only'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupIngress]
