"""Template outputs."""

from . import *  # noqa: F403


class InstanceOutput(Output):
    """DNS Name of the newly created EC2 instance"""

    value = EC2Instance.PublicDnsName
    description = 'DNS Name of the newly created EC2 instance'
