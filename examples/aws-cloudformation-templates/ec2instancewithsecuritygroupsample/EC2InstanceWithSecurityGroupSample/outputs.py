"""Template outputs."""

from . import *  # noqa: F403


class InstanceIdOutput:
    """InstanceId of the newly created EC2 instance"""

    resource: Output
    value = EC2Instance
    description = 'InstanceId of the newly created EC2 instance'


class AZOutput:
    """Availability Zone of the newly created EC2 instance"""

    resource: Output
    value = EC2Instance.AvailabilityZone
    description = 'Availability Zone of the newly created EC2 instance'


class PublicDNSOutput:
    """Public DNSName of the newly created EC2 instance"""

    resource: Output
    value = EC2Instance.PublicDnsName
    description = 'Public DNSName of the newly created EC2 instance'


class PublicIPOutput:
    """Public IP address of the newly created EC2 instance"""

    resource: Output
    value = EC2Instance.PublicIp
    description = 'Public IP address of the newly created EC2 instance'
