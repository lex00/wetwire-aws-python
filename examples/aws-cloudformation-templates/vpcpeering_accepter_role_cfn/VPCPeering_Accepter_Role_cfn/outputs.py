"""Template outputs."""

from . import *  # noqa: F403


class PeerRoleARNOutput:
    """VPC Peer Role ARN"""

    resource: Output
    value = PeerRole.Arn
    description = 'VPC Peer Role ARN'
