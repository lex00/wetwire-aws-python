"""Network resources: LoadBalancerSecurityGroup, LoadBalancer, TargetGroup, LoadBalancerListener, LoadBalancerEgress."""

from . import *  # noqa: F403


class LoadBalancerSecurityGroupEgress(ec2.SecurityGroup.Egress):
    cidr_ip = '0.0.0.0/0'
    description = 'Allow from anyone on port 443'
    from_port = 443
    ip_protocol = 'tcp'
    to_port = 443


class LoadBalancerSecurityGroup(ec2.SecurityGroup):
    group_description = 'Automatically created Security Group for ELB'
    security_group_ingress = [LoadBalancerSecurityGroupEgress]
    vpc_id = VPCId


class LoadBalancerTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'deletion_protection.enabled'
    value = False


class LoadBalancerTargetGroupAttribute1(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'routing.http.drop_invalid_header_fields.enabled'
    value = True


class LoadBalancer(elasticloadbalancingv2.LoadBalancer):
    load_balancer_attributes = [LoadBalancerTargetGroupAttribute, LoadBalancerTargetGroupAttribute1]
    scheme = 'internet-facing'
    security_groups = [LoadBalancerSecurityGroup.GroupId]
    subnets = [PublicSubnet1, PublicSubnet2]
    type_ = 'application'


class TargetGroupTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'deregistration_delay.timeout_seconds'
    value = '10'


class TargetGroupTargetGroupAttribute1(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'stickiness.enabled'
    value = 'false'


class TargetGroup(elasticloadbalancingv2.TargetGroup):
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    target_group_attributes = [TargetGroupTargetGroupAttribute, TargetGroupTargetGroupAttribute1]
    target_type = elasticloadbalancingv2.TargetTypeEnum.IP
    vpc_id = VPCId


class LoadBalancerListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    target_group_arn = TargetGroup
    type_ = 'forward'


class LoadBalancerListenerCertificate(elasticloadbalancingv2.ListenerCertificate.Certificate):
    certificate_arn = CertificateArn


class LoadBalancerListener(elasticloadbalancingv2.Listener):
    default_actions = [LoadBalancerListenerAction]
    load_balancer_arn = LoadBalancer
    port = 443
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTPS
    certificates = [LoadBalancerListenerCertificate]
    ssl_policy = 'ELBSecurityPolicy-TLS13-1-2-2021-06'


class LoadBalancerEgress(ec2.SecurityGroupEgress):
    description = 'Load balancer to target'
    destination_security_group_id = DestinationSecurityGroupId
    from_port = 80
    group_id = LoadBalancerSecurityGroup.GroupId
    ip_protocol = 'tcp'
    to_port = 80
