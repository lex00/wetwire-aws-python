"""Stack resources."""

from . import *  # noqa: F403


class IPAssoc:
    resource: ec2.EIPAssociation
    instance_id = EC2Instance
    allocation_id = IPAddress.AllocationId
