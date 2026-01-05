"""Stack resources."""

from . import *  # noqa: F403


class IPAssoc(ec2.EIPAssociation):
    instance_id = EC2Instance
    allocation_id = IPAddress.AllocationId
