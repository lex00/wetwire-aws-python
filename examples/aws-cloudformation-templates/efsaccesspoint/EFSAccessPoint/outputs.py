"""Template outputs."""

from . import *  # noqa: F403


class FileSystemIdOutput(Output):
    """ID of the created EFS File System"""

    value = EFSFileSystem
    description = 'ID of the created EFS File System'
