"""Template outputs."""

from . import *  # noqa: F403


class FileSystemIdOutput:
    """ID of the created EFS File System"""

    resource: Output
    value = EFSFileSystem
    description = 'ID of the created EFS File System'
