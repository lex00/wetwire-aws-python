"""Template outputs."""

from . import *  # noqa: F403


class PeerRoleARNOutput(Output):
    """VPC Peer Role ARN"""

    value = PeerRole.Arn
    description = 'VPC Peer Role ARN'
