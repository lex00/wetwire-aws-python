"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class EMRClusterName:
    """Name of the cluster"""

    resource: Parameter
    type = STRING
    description = 'Name of the cluster'
    default = 'emrcluster'


class KeyName:
    """Must be an existing Keyname"""

    resource: Parameter
    type = STRING
    description = 'Must be an existing Keyname'


class MasterInstanceType:
    """Instance type to be used for the master instance."""

    resource: Parameter
    type = STRING
    description = 'Instance type to be used for the master instance.'
    default = 'm3.xlarge'


class CoreInstanceType:
    """Instance type to be used for core instances."""

    resource: Parameter
    type = STRING
    description = 'Instance type to be used for core instances.'
    default = 'm3.xlarge'


class NumberOfCoreInstances:
    """Must be a valid number"""

    resource: Parameter
    type = NUMBER
    description = 'Must be a valid number'
    default = 2


class SubnetID:
    """Must be a valid public subnet ID"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid public subnet ID'


class AdditionalCoreNodeSecurityGroups:
    """Comma-delimited list of additional security groups for core and task nodes"""

    resource: Parameter
    type = COMMA_DELIMITED_LIST
    description = 'Comma-delimited list of additional security groups for core and task nodes'


class AdditionalPrimaryNodeSecurityGroups:
    """Comma-delimited list of additional security groups for primary nodes"""

    resource: Parameter
    type = COMMA_DELIMITED_LIST
    description = 'Comma-delimited list of additional security groups for primary nodes'


class LogUri:
    """Must be a valid S3 URL"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid S3 URL'
    default = 's3://emrclusterlogbucket/'


class S3DataUri:
    """Must be a valid S3 bucket URL"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid S3 bucket URL'
    default = 's3://emrclusterdatabucket/'


class ReleaseLabel:
    """Must be a valid EMR release version"""

    resource: Parameter
    type = STRING
    description = 'Must be a valid EMR release version'
    default = 'emr-5.7.0'


class Applications:
    """Please select which application will be installed on the cluster. This would be either Ganglia and spark, or Ganglia and s3 backed Hbase"""

    resource: Parameter
    type = STRING
    description = 'Please select which application will be installed on the cluster. This would be either Ganglia and spark, or Ganglia and s3 backed Hbase'
    allowed_values = [
    'Spark',
    'Hbase',
]


class SparkCondition:
    resource: TemplateCondition
    logical_id = 'Spark'
    expression = Equals(Applications, 'Spark')


class HbaseCondition:
    resource: TemplateCondition
    logical_id = 'Hbase'
    expression = Equals(Applications, 'Hbase')
