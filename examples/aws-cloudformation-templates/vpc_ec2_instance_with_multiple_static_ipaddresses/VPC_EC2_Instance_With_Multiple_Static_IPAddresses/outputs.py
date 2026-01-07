"""Template outputs."""

from . import *  # noqa: F403


class InstanceIdOutput(Output):
    """Instance Id of newly created instance"""

    value = EC2Instance
    description = 'Instance Id of newly created instance'


class EIP1Output(Output):
    """Primary public IP of Eth0"""

    value = Join(' ', [
    'IP address',
    EIP1,
    'on subnet',
    SubnetId,
])
    description = 'Primary public IP of Eth0'


class PrimaryPrivateIPAddressOutput(Output):
    """Primary private IP address of Eth0"""

    value = Join(' ', [
    'IP address',
    Eth0.PrimaryPrivateIpAddress,
    'on subnet',
    SubnetId,
])
    description = 'Primary private IP address of Eth0'


class SecondaryPrivateIPAddressesOutput(Output):
    """Secondary private IP address of Eth0"""

    value = Join(' ', [
    'IP address',
    Select(0, Eth0.SecondaryPrivateIpAddresses),
    'on subnet',
    SubnetId,
])
    description = 'Secondary private IP address of Eth0'
