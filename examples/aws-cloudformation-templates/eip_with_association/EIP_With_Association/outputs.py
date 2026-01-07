"""Template outputs."""

from . import *  # noqa: F403


class InstanceIdOutput(Output):
    """InstanceId of the newly created EC2 instance"""

    value = EC2Instance
    description = 'InstanceId of the newly created EC2 instance'


class InstanceIPAddressOutput(Output):
    """IP address of the newly created EC2 instance"""

    value = IPAddress
    description = 'IP address of the newly created EC2 instance'
