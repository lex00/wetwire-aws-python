"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class EFSFileSystemName:
    """Name for the EFS file system"""

    resource: Parameter
    type = STRING
    description = 'Name for the EFS file system'
    default = 'SampleEFSFilesystem'


class AccessPointName:
    """Name for the EFS access point"""

    resource: Parameter
    type = STRING
    description = 'Name for the EFS access point'
    default = 'SampleEFSAccessPoint'


class Subnet1:
    """A subnet for the first EFS mount target"""

    resource: Parameter
    type = SUBNET_ID
    description = 'A subnet for the first EFS mount target'


class Subnet2:
    """A subnet for the second EFS mount target"""

    resource: Parameter
    type = SUBNET_ID
    description = 'A subnet for the second EFS mount target'


class Subnet3:
    """A subnet for the third EFS mount target"""

    resource: Parameter
    type = SUBNET_ID
    description = 'A subnet for the third EFS mount target'


class SecurityGroup1:
    """Security group for the first EFS mount target"""

    resource: Parameter
    type = SECURITY_GROUP_ID
    description = 'Security group for the first EFS mount target'


class SecurityGroup2:
    """Security group for the second EFS mount target"""

    resource: Parameter
    type = SECURITY_GROUP_ID
    description = 'Security group for the second EFS mount target'


class SecurityGroup3:
    """Security group for the third EFS mount target"""

    resource: Parameter
    type = SECURITY_GROUP_ID
    description = 'Security group for the third EFS mount target'
