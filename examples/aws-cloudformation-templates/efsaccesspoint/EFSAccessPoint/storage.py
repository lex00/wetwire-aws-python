"""Storage resources: EFSFileSystem, EFSMountTarget2, EFSMountTarget3, EFSAccessPoint, EFSMountTarget1."""

from . import *  # noqa: F403


class EFSFileSystemAccessPointTag:
    resource: efs.AccessPoint.AccessPointTag
    key = 'Name'
    value = EFSFileSystemName


class EFSFileSystem:
    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'
    file_system_tags = [EFSFileSystemAccessPointTag]


class EFSMountTarget2:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup2]
    subnet_id = Subnet2


class EFSMountTarget3:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup3]
    subnet_id = Subnet3


class EFSAccessPointAccessPointTag:
    resource: efs.AccessPoint.AccessPointTag
    key = 'Name'
    value = AccessPointName


class EFSAccessPoint:
    resource: efs.AccessPoint
    file_system_id = EFSFileSystem
    access_point_tags = [EFSAccessPointAccessPointTag]


class EFSMountTarget1:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup1]
    subnet_id = Subnet1
