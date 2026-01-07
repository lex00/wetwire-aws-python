"""Template outputs."""

from . import *  # noqa: F403


class EC2IPAddressOutput(Output):
    """EC2 Instance Public IP Address"""

    value = GreengrassInstance.PublicIp
    description = 'EC2 Instance Public IP Address'
