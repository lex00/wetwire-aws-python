"""Network resources: EIP1, EIP2, TargetGroup, SecondEIP, FirstEIP, loadBalancer, Listener."""

from . import *  # noqa: F403


class EIP1(ec2.EIP):
    domain = 'vpc'


class EIP2(ec2.EIP):
    domain = 'vpc'


class TargetGroupTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'deregistration_delay.timeout_seconds'
    value = '20'


class TargetGroup(elasticloadbalancingv2.TargetGroup):
    name = 'MyTargets'
    port = 10
    protocol = elasticloadbalancingv2.ProtocolEnum.TCP
    target_group_attributes = [TargetGroupTargetGroupAttribute]
    vpc_id = Select(0, VPC)


class SecondEIP(ec2.EIP):
    domain = 'vpc'


class FirstEIP(ec2.EIP):
    domain = 'vpc'


class loadBalancerSubnetMapping(elasticloadbalancingv2.LoadBalancer.SubnetMapping):
    allocation_id = EIP1.AllocationId
    subnet_id = Select(0, Subnet1)


class loadBalancerSubnetMapping1(elasticloadbalancingv2.LoadBalancer.SubnetMapping):
    allocation_id = EIP2.AllocationId
    subnet_id = Select(0, Subnet2)


class loadBalancer(elasticloadbalancingv2.LoadBalancer):
    subnet_mappings = [loadBalancerSubnetMapping, loadBalancerSubnetMapping1]
    type_ = ELBType
    ip_address_type = ELBIpAddressType
    depends_on = [EIP2, EIP1]


class ListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    type_ = 'forward'
    target_group_arn = TargetGroup


class Listener(elasticloadbalancingv2.Listener):
    default_actions = [ListenerAction]
    load_balancer_arn = loadBalancer
    port = '80'
    protocol = elasticloadbalancingv2.ProtocolEnum.TCP
