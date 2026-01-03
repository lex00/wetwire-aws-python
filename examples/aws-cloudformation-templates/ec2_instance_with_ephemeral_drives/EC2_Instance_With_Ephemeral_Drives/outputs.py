"""Template outputs."""

from . import *  # noqa: F403


class InstanceOutput:
    """DNS Name of the newly created EC2 instance"""

    resource: Output
    value = EC2Instance.PublicDnsName
    description = 'DNS Name of the newly created EC2 instance'
