"""Network resources: ASCPrivateLinkNLB, ASCPrivateLinkVPCES, ASCPrivateLinkVPCESPermission, ASCPrivateLinkTargetGroup, ASCPrivateLinkListener."""

from . import *  # noqa: F403


class ASCPrivateLinkNLBListenerAttribute:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'load_balancing.cross_zone.enabled'
    value = True


class ASCPrivateLinkNLB:
    resource: elasticloadbalancingv2.LoadBalancer
    type_ = 'network'
    scheme = 'internal'
    subnets = Subnets
    load_balancer_attributes = [ASCPrivateLinkNLBListenerAttribute]
    depends_on = [ASCPrivateLinkCertificate]


class ASCPrivateLinkVPCES:
    resource: ec2.VPCEndpointService
    acceptance_required = False
    network_load_balancer_arns = [ASCPrivateLinkNLB]


class ASCPrivateLinkVPCESPermission:
    resource: ec2.VPCEndpointServicePermissions
    allowed_principals = ['appflow.amazonaws.com']
    service_id = ASCPrivateLinkVPCES


class ASCPrivateLinkTargetGroupTargetDescription:
    resource: elasticloadbalancingv2.TargetGroup.TargetDescription
    availability_zone = If("IpInVpc", AWS_NO_VALUE, 'all')
    id = IP
    port = Port


class ASCPrivateLinkTargetGroup:
    resource: elasticloadbalancingv2.TargetGroup
    vpc_id = VpcId
    protocol = If("SapUseHttps", 'TLS', 'TCP')
    port = 443
    target_type = elasticloadbalancingv2.TargetTypeEnum.IP
    targets = [ASCPrivateLinkTargetGroupTargetDescription]
    health_check_path = HealthCheckPath
    health_check_protocol = Protocol
    depends_on = [ASCPrivateLinkCertificate]


class ASCPrivateLinkListenerCertificate:
    resource: elasticloadbalancingv2.Listener.Certificate
    certificate_arn = ASCPrivateLinkCertificate


class ASCPrivateLinkListenerAction:
    resource: elasticloadbalancingv2.Listener.Action
    type_ = 'forward'
    target_group_arn = ASCPrivateLinkTargetGroup


class ASCPrivateLinkListener:
    resource: elasticloadbalancingv2.Listener
    load_balancer_arn = ASCPrivateLinkNLB
    protocol = elasticloadbalancingv2.ProtocolEnum.TLS
    port = 443
    ssl_policy = 'ELBSecurityPolicy-TLS13-1-0-2021-06'
    certificates = [ASCPrivateLinkListenerCertificate]
    default_actions = [ASCPrivateLinkListenerAction]
