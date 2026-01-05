"""Network resources: TargetGroup, LoadBalancerRule."""

from . import *  # noqa: F403


class TargetGroup(elasticloadbalancingv2.TargetGroup):
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    name = ServiceName
    port = 80
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    unhealthy_threshold_count = 2
    vpc_id = ImportValue(Join(':', [
    StackName,
    'VPCId',
]))


class LoadBalancerRuleAction:
    resource: elasticloadbalancingv2.ListenerRule.Action
    target_group_arn = TargetGroup
    type_ = 'forward'


class LoadBalancerRuleRuleCondition:
    resource: elasticloadbalancingv2.ListenerRule.RuleCondition
    field_ = 'path-pattern'
    values = [Path]


class LoadBalancerRule(elasticloadbalancingv2.ListenerRule):
    actions = [LoadBalancerRuleAction]
    conditions = [LoadBalancerRuleRuleCondition]
    listener_arn = ImportValue(Join(':', [
    StackName,
    'PublicListener',
]))
    priority = Priority
