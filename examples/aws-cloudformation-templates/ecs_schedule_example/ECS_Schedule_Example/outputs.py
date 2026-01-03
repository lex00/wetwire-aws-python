"""Template outputs."""

from . import *  # noqa: F403


class EcsServiceOutput:
    resource: Output
    value = Service


class EcsClusterOutput:
    resource: Output
    value = ECSCluster


class EcsTaskDefOutput:
    resource: Output
    value = TaskDefinition


class ECSALBOutput:
    """Your ALB DNS URL"""

    resource: Output
    value = Join('', [ECSALB.DNSName])
    description = 'Your ALB DNS URL'
