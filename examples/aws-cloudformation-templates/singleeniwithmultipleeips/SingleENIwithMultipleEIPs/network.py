"""Network resources: EIP1, ENI, EIP2, Association2, Association1."""

from . import *  # noqa: F403


class EIP1(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'


class ENI(ec2.NetworkInterface):
    resource: ec2.NetworkInterface
    secondary_private_ip_address_count = 2
    source_dest_check = True
    subnet_id = Select(0, Subnet)


class EIP2(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'


class Association2(ec2.EIPAssociation):
    resource: ec2.EIPAssociation
    allocation_id = EIP2.AllocationId
    network_interface_id = ENI
    private_ip_address = Select(1, ENI.SecondaryPrivateIpAddresses)
    depends_on = [ENI, EIP2]


class Association1(ec2.EIPAssociation):
    resource: ec2.EIPAssociation
    allocation_id = EIP1.AllocationId
    network_interface_id = ENI
    private_ip_address = Select(0, ENI.SecondaryPrivateIpAddresses)
    depends_on = [ENI, EIP1]
