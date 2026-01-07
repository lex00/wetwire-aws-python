"""Template outputs."""

from . import *  # noqa: F403


class VPCPeeringConnectionIdOutput(Output):
    """VPC Peering Connection ID"""

    value = VPCPeeringConnection
    description = 'VPC Peering Connection ID'
