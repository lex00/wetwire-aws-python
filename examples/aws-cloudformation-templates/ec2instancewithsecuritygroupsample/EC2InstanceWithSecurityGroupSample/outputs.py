"""Template outputs."""

from . import *  # noqa: F403


class InstanceIdOutput(Output):
    """InstanceId of the newly created EC2 instance"""

    value = EC2Instance
    description = 'InstanceId of the newly created EC2 instance'


class AZOutput(Output):
    """Availability Zone of the newly created EC2 instance"""

    value = EC2Instance.AvailabilityZone
    description = 'Availability Zone of the newly created EC2 instance'


class PublicDNSOutput(Output):
    """Public DNSName of the newly created EC2 instance"""

    value = EC2Instance.PublicDnsName
    description = 'Public DNSName of the newly created EC2 instance'


class PublicIPOutput(Output):
    """Public IP address of the newly created EC2 instance"""

    value = EC2Instance.PublicIp
    description = 'Public IP address of the newly created EC2 instance'
