"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class EFSFileSystemName(Parameter):
    """Name for the EFS file system"""

    type = STRING
    description = 'Name for the EFS file system'
    default = 'SampleEFSFilesystem'


class AccessPointName(Parameter):
    """Name for the EFS access point"""

    type = STRING
    description = 'Name for the EFS access point'
    default = 'SampleEFSAccessPoint'


class Subnet1(Parameter):
    """A subnet for the first EFS mount target"""

    type = SUBNET_ID
    description = 'A subnet for the first EFS mount target'


class Subnet2(Parameter):
    """A subnet for the second EFS mount target"""

    type = SUBNET_ID
    description = 'A subnet for the second EFS mount target'


class Subnet3(Parameter):
    """A subnet for the third EFS mount target"""

    type = SUBNET_ID
    description = 'A subnet for the third EFS mount target'


class SecurityGroup1(Parameter):
    """Security group for the first EFS mount target"""

    type = SECURITY_GROUP_ID
    description = 'Security group for the first EFS mount target'


class SecurityGroup2(Parameter):
    """Security group for the second EFS mount target"""

    type = SECURITY_GROUP_ID
    description = 'Security group for the second EFS mount target'


class SecurityGroup3(Parameter):
    """Security group for the third EFS mount target"""

    type = SECURITY_GROUP_ID
    description = 'Security group for the third EFS mount target'
