"""Network resources: EcsSecurityGroup, EcsSecurityGroupALBports, ECSALB, ECSTG, EcsSecurityGroupSSHinbound, ALBListener, ECSALBListenerRule, EcsSecurityGroupHTTPinbound."""

from . import *  # noqa: F403


class EcsSecurityGroup(ec2.SecurityGroup):
    group_description = 'ECS Security Group'
    vpc_id = VpcId


class EcsSecurityGroupALBports(ec2.SecurityGroupIngress):
    group_id = EcsSecurityGroup
    ip_protocol = 'tcp'
    from_port = '31000'
    to_port = '61000'
    source_security_group_id = EcsSecurityGroup


class ECSALBTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'idle_timeout.timeout_seconds'
    value = '30'


class ECSALB(elasticloadbalancingv2.LoadBalancer):
    name = 'ECSALB'
    scheme = 'internet-facing'
    load_balancer_attributes = [ECSALBTargetGroupAttribute]
    subnets = SubnetId
    security_groups = [EcsSecurityGroup]


class ECSTG(elasticloadbalancingv2.TargetGroup):
    health_check_interval_seconds = 10
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = 'ECSTG'
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    unhealthy_threshold_count = 2
    vpc_id = VpcId
    depends_on = [ECSALB]


class EcsSecurityGroupSSHinbound(ec2.SecurityGroupIngress):
    group_id = EcsSecurityGroup
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = '192.168.1.0/0'


class ALBListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    type_ = 'forward'
    target_group_arn = ECSTG


class ALBListener(elasticloadbalancingv2.Listener):
    default_actions = [ALBListenerAction]
    load_balancer_arn = ECSALB
    port = '80'
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    depends_on = [ECSServiceRole]


class ECSALBListenerRuleAction(elasticloadbalancingv2.ListenerRule.Action):
    type_ = 'forward'
    target_group_arn = ECSTG


class ECSALBListenerRuleRuleCondition(elasticloadbalancingv2.ListenerRule.RuleCondition):
    field_ = 'path-pattern'
    values = ['/']


class ECSALBListenerRule(elasticloadbalancingv2.ListenerRule):
    actions = [ECSALBListenerRuleAction]
    conditions = [ECSALBListenerRuleRuleCondition]
    listener_arn = ALBListener
    priority = 1
    depends_on = [ALBListener]


class EcsSecurityGroupHTTPinbound(ec2.SecurityGroupIngress):
    group_id = EcsSecurityGroup
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'
