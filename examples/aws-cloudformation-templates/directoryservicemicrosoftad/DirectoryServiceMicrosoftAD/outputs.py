"""Template outputs."""

from . import *  # noqa: F403


class DirectoryIDOutput(Output):
    """ID of the MS Directory"""

    value = rMSDirectory
    description = 'ID of the MS Directory'


class PrimaryDNSOutput(Output):
    """DNS IPs of the MS Directory"""

    value = Select(0, rMSDirectory.DnsIpAddresses)
    description = 'DNS IPs of the MS Directory'


class SecondaryDNSOutput(Output):
    """DNS IPs of the MSDirectory"""

    value = Select(1, rMSDirectory.DnsIpAddresses)
    description = 'DNS IPs of the MSDirectory'


class DirectoryAliasOutput(Output):
    """URL for the alias"""

    value = rMSDirectory.Alias
    description = 'URL for the alias'
    condition = 'cAlias'
