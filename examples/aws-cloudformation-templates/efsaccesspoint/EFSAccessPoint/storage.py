"""Storage resources: EFSFileSystem, EFSMountTarget1, EFSMountTarget3, EFSMountTarget2, EFSAccessPoint."""

from . import *  # noqa: F403


class EFSFileSystemElasticFileSystemTag:
    resource: efs.FileSystem.ElasticFileSystemTag
    key = 'Name'
    value = EFSFileSystemName


class EFSFileSystem:
    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'
    file_system_tags = [EFSFileSystemElasticFileSystemTag]


class EFSMountTarget1:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup1]
    subnet_id = Subnet1


class EFSMountTarget3:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup3]
    subnet_id = Subnet3


class EFSMountTarget2:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [SecurityGroup2]
    subnet_id = Subnet2


class EFSAccessPointElasticFileSystemTag:
    resource: efs.FileSystem.ElasticFileSystemTag
    key = 'Name'
    value = AccessPointName


class EFSAccessPoint:
    resource: efs.AccessPoint
    file_system_id = EFSFileSystem
    access_point_tags = [EFSAccessPointElasticFileSystemTag]
