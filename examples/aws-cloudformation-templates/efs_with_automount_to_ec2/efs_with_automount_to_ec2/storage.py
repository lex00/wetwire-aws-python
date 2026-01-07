"""Storage resources: EFSFileSystem, EFSMountTarget4, EFSMountTarget1, EFSMountTarget2, EFSMountTarget3."""

from . import *  # noqa: F403


class EFSFileSystem(efs.FileSystem):
    resource: efs.FileSystem
    encrypted = True
    performance_mode = 'generalPurpose'


class EFSMountTarget4(efs.MountTarget):
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(3, Subnets)


class EFSMountTarget1(efs.MountTarget):
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(0, Subnets)


class EFSMountTarget2(efs.MountTarget):
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(1, Subnets)


class EFSMountTarget3(efs.MountTarget):
    resource: efs.MountTarget
    file_system_id = EFSFileSystem
    security_groups = [EFSSecurityGroup.GroupId]
    subnet_id = Select(2, Subnets)
