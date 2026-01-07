"""Template outputs."""

from . import *  # noqa: F403


class DirectoryAliasUrlOutput(Output):
    """Directory Alias"""

    value = DirectorySettingsResource.AliasUrl
    description = 'Directory Alias'
