"""Template outputs."""

from . import *  # noqa: F403


class EC2IPAddressOutput:
    """EC2 Instance Public IP Address"""

    resource: Output
    value = GreengrassInstance.PublicIp
    description = 'EC2 Instance Public IP Address'
