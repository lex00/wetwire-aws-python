"""Template outputs."""

from . import *  # noqa: F403


class ClusterNameOutput:
    """The name of the ECS cluster"""

    resource: Output
    value = ECSCluster
    description = 'The name of the ECS cluster'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ClusterName',
])


class ExternalUrlOutput:
    """The url of the external load balancer"""

    resource: Output
    value = Join('', [
    'http://',
    PublicLoadBalancer.DNSName,
])
    description = 'The url of the external load balancer'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ExternalUrl',
])


class ECSRoleOutput:
    """The ARN of the ECS role"""

    resource: Output
    value = ECSRole.Arn
    description = 'The ARN of the ECS role'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ECSRole',
])


class ECSTaskExecutionRoleOutput:
    """The ARN of the ECS role"""

    resource: Output
    value = ECSTaskExecutionRole.Arn
    description = 'The ARN of the ECS role'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'ECSTaskExecutionRole',
])


class PublicListenerOutput:
    """The ARN of the public load balancer's Listener"""

    resource: Output
    value = PublicLoadBalancerListener
    description = "The ARN of the public load balancer's Listener"
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicListener',
])


class VPCIdOutput:
    """The ID of the VPC that this stack is deployed in"""

    resource: Output
    value = VPC
    description = 'The ID of the VPC that this stack is deployed in'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'VPCId',
])


class PublicSubnetOneOutput:
    """Public subnet one"""

    resource: Output
    value = PublicSubnetOne
    description = 'Public subnet one'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicSubnetOne',
])


class PublicSubnetTwoOutput:
    """Public subnet two"""

    resource: Output
    value = PublicSubnetTwo
    description = 'Public subnet two'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'PublicSubnetTwo',
])


class FargateContainerSecurityGroupOutput:
    """A security group used to allow Fargate containers to receive traffic"""

    resource: Output
    value = FargateContainerSecurityGroup
    description = 'A security group used to allow Fargate containers to receive traffic'
    export_name = Join(':', [
    AWS_STACK_NAME,
    'FargateContainerSecurityGroup',
])
