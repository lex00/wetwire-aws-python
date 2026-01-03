"""Template outputs."""

from . import *  # noqa: F403


class VPCPeeringConnectionIdOutput:
    """VPC Peering Connection ID"""

    resource: Output
    value = VPCPeeringConnection
    description = 'VPC Peering Connection ID'
