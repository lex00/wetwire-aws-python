"""Network resources: EIP2, EIP1, ENI, Association1, Association2."""

from . import *  # noqa: F403


class EIP2(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'


class EIP1(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'


class ENI(ec2.NetworkInterface):
    resource: ec2.NetworkInterface
    secondary_private_ip_address_count = 2
    source_dest_check = True
    subnet_id = Select(0, Subnet)


class Association1(ec2.EIPAssociation):
    resource: ec2.EIPAssociation
    allocation_id = EIP1.AllocationId
    network_interface_id = ENI
    private_ip_address = Select(0, ENI.SecondaryPrivateIpAddresses)
    depends_on = [ENI, EIP1]


class Association2(ec2.EIPAssociation):
    resource: ec2.EIPAssociation
    allocation_id = EIP2.AllocationId
    network_interface_id = ENI
    private_ip_address = Select(1, ENI.SecondaryPrivateIpAddresses)
    depends_on = [ENI, EIP2]
