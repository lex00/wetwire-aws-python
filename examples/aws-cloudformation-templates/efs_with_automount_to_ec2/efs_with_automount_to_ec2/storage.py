"""Storage resources: EFSFileSystem, EFSMountTarget2, EFSMountTarget3, EFSMountTarget1, EFSMountTarget4."""

from . import *  # noqa: F403


class EFSFileSystem:
    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'


class EFSMountTarget2:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(1, Subnets)


class EFSMountTarget3:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(2, Subnets)


class EFSMountTarget1:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(0, Subnets)


class EFSMountTarget4:
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(3, Subnets)
