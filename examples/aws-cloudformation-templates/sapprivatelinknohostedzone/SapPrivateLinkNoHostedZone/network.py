"""Network resources: ASCPrivateLinkNLB, ASCPrivateLinkVPCES, ASCPrivateLinkTargetGroup, ASCPrivateLinkVPCESPermission, ASCPrivateLinkListener."""

from . import *  # noqa: F403


class ASCPrivateLinkNLBTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'load_balancing.cross_zone.enabled'
    value = True


class ASCPrivateLinkNLB(elasticloadbalancingv2.LoadBalancer):
    resource: elasticloadbalancingv2.LoadBalancer
    type_ = 'network'
    scheme = 'internal'
    subnets = Subnets
    load_balancer_attributes = [ASCPrivateLinkNLBTargetGroupAttribute]
    depends_on = [ASCPrivateLinkCertificate]


class ASCPrivateLinkVPCES(ec2.VPCEndpointService):
    resource: ec2.VPCEndpointService
    acceptance_required = False
    network_load_balancer_arns = [ASCPrivateLinkNLB]


class ASCPrivateLinkTargetGroupTargetDescription(elasticloadbalancingv2.TargetGroup.TargetDescription):
    availability_zone = If("IpInVpc", AWS_NO_VALUE, 'all')
    id = IP
    port = Port


class ASCPrivateLinkTargetGroup(elasticloadbalancingv2.TargetGroup):
    resource: elasticloadbalancingv2.TargetGroup
    vpc_id = VpcId
    protocol = If("SapUseHttps", 'TLS', 'TCP')
    port = 443
    target_type = elasticloadbalancingv2.TargetTypeEnum.IP
    targets = [ASCPrivateLinkTargetGroupTargetDescription]
    health_check_path = HealthCheckPath
    health_check_protocol = Protocol
    depends_on = [ASCPrivateLinkCertificate]


class ASCPrivateLinkVPCESPermission(ec2.VPCEndpointServicePermissions):
    resource: ec2.VPCEndpointServicePermissions
    allowed_principals = ['appflow.amazonaws.com']
    service_id = ASCPrivateLinkVPCES


class ASCPrivateLinkListenerCertificate(elasticloadbalancingv2.ListenerCertificate.Certificate):
    certificate_arn = ASCPrivateLinkCertificate


class ASCPrivateLinkListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    type_ = 'forward'
    target_group_arn = ASCPrivateLinkTargetGroup


class ASCPrivateLinkListener(elasticloadbalancingv2.Listener):
    resource: elasticloadbalancingv2.Listener
    load_balancer_arn = ASCPrivateLinkNLB
    protocol = elasticloadbalancingv2.ProtocolEnum.TLS
    port = 443
    ssl_policy = 'ELBSecurityPolicy-TLS13-1-0-2021-06'
    certificates = [ASCPrivateLinkListenerCertificate]
    default_actions = [ASCPrivateLinkListenerAction]
