"""Template outputs."""

from . import *  # noqa: F403


class DirectoryIDOutput:
    """ID of the MS Directory"""

    resource: Output
    value = rMSDirectory
    description = 'ID of the MS Directory'


class PrimaryDNSOutput:
    """DNS IPs of the MS Directory"""

    resource: Output
    value = Select(0, rMSDirectory.DnsIpAddresses)
    description = 'DNS IPs of the MS Directory'


class SecondaryDNSOutput:
    """DNS IPs of the MSDirectory"""

    resource: Output
    value = Select(1, rMSDirectory.DnsIpAddresses)
    description = 'DNS IPs of the MSDirectory'


class DirectoryAliasOutput:
    """URL for the alias"""

    resource: Output
    value = rMSDirectory.Alias
    description = 'URL for the alias'
    condition = 'cAlias'
