"""Template outputs."""

from . import *  # noqa: F403


class ClusterNameOutput(Output):
    """The name of the ECS cluster"""

    value = ECSCluster
    description = 'The name of the ECS cluster'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ClusterName',
])


class ExternalUrlOutput(Output):
    """The url of the external load balancer"""

    value = Join('', [
    'http://',
    PublicLoadBalancer.DNSName,
])
    description = 'The url of the external load balancer'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ExternalUrl',
])


class ECSRoleOutput(Output):
    """The ARN of the ECS role"""

    value = ECSRole.Arn
    description = 'The ARN of the ECS role'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ECSRole',
])


class PublicListenerOutput(Output):
    """The ARN of the public load balancer's Listener"""

    value = PublicLoadBalancerListener
    description = "The ARN of the public load balancer's Listener"
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicListener',
])


class VPCIdOutput(Output):
    """The ID of the VPC that this stack is deployed in"""

    value = VPC
    description = 'The ID of the VPC that this stack is deployed in'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'VPCId',
])


class PublicSubnetOneOutput(Output):
    """Public subnet one"""

    value = PublicSubnetOne
    description = 'Public subnet one'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicSubnetOne',
])


class PublicSubnetTwoOutput(Output):
    """Public subnet two"""

    value = PublicSubnetTwo
    description = 'Public subnet two'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicSubnetTwo',
])


class EcsHostSecurityGroupOutput(Output):
    """A security group used to allow containers to receive traffic"""

    value = EcsHostSecurityGroup
    description = 'A security group used to allow containers to receive traffic'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'EcsHostSecurityGroup',
])
