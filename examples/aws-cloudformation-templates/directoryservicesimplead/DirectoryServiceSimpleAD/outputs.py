"""Template outputs."""

from . import *  # noqa: F403


class DirectoryIDOutput:
    """ID of the SimpleAD"""

    resource: Output
    value = SimpleAD
    description = 'ID of the SimpleAD'


class PrimaryDNSOutput:
    """DNS IPs of the SimpleAD"""

    resource: Output
    value = Select(0, SimpleAD.DnsIpAddresses)
    description = 'DNS IPs of the SimpleAD'


class SecondaryDNSOutput:
    """DNS IPs of the SimpleAD"""

    resource: Output
    value = Select(1, SimpleAD.DnsIpAddresses)
    description = 'DNS IPs of the SimpleAD'


class DirectoryAliasOutput:
    """URL for the alias"""

    resource: Output
    value = SimpleAD.Alias
    description = 'URL for the alias'
    condition = 'Alias'
