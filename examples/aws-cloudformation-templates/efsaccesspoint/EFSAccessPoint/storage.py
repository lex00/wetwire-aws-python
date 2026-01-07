"""Storage resources: EFSFileSystem, EFSMountTarget3, EFSMountTarget1, EFSMountTarget2, EFSAccessPoint."""

from . import *  # noqa: F403


class EFSFileSystemAccessPointTag(efs.AccessPoint.AccessPointTag):
    key = 'Name'
    value = EFSFileSystemName


class EFSFileSystem(efs.FileSystem):
    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'
    file_system_tags = [EFSFileSystemAccessPointTag]


class EFSMountTarget3(efs.MountTarget):
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup3]
    subnet_id = Subnet3


class EFSMountTarget1(efs.MountTarget):
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup1]
    subnet_id = Subnet1


class EFSMountTarget2(efs.MountTarget):
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup2]
    subnet_id = Subnet2


class EFSAccessPointAccessPointTag(efs.AccessPoint.AccessPointTag):
    key = 'Name'
    value = AccessPointName


class EFSAccessPoint(efs.AccessPoint):
    resource: efs.AccessPoint
    file_system_id = EFSFileSystem
    access_point_tags = [EFSAccessPointAccessPointTag]
