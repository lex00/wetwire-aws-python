"""Template outputs."""

from . import *  # noqa: F403


class InstanceIdOutput:
    """InstanceId of the newly created EC2 instance"""

    resource: Output
    value = EC2Instance
    description = 'InstanceId of the newly created EC2 instance'


class InstanceIPAddressOutput:
    """IP address of the newly created EC2 instance"""

    resource: Output
    value = IPAddress
    description = 'IP address of the newly created EC2 instance'
