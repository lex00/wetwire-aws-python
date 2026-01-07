"""Template outputs."""

from . import *  # noqa: F403


class EcsServiceOutput(Output):
    value = Service


class EcsClusterOutput(Output):
    value = ECSCluster


class EcsTaskDefOutput(Output):
    value = TaskDefinition


class ECSALBOutput(Output):
    """Your ALB DNS URL"""

    value = Join('', [ECSALB.DNSName])
    description = 'Your ALB DNS URL'
