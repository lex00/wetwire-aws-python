"""Template outputs."""

from . import *  # noqa: F403


class DirectoryAliasUrlOutput:
    """Directory Alias"""

    resource: Output
    value = DirectorySettingsResource.AliasUrl
    description = 'Directory Alias'
