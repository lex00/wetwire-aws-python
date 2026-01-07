"""Template outputs."""

from . import *  # noqa: F403


class DirectoryIDOutput(Output):
    """ID of the SimpleAD"""

    value = SimpleAD
    description = 'ID of the SimpleAD'


class PrimaryDNSOutput(Output):
    """DNS IPs of the SimpleAD"""

    value = Select(0, SimpleAD.DnsIpAddresses)
    description = 'DNS IPs of the SimpleAD'


class SecondaryDNSOutput(Output):
    """DNS IPs of the SimpleAD"""

    value = Select(1, SimpleAD.DnsIpAddresses)
    description = 'DNS IPs of the SimpleAD'


class DirectoryAliasOutput(Output):
    """URL for the alias"""

    value = SimpleAD.Alias
    description = 'URL for the alias'
    condition = 'Alias'
