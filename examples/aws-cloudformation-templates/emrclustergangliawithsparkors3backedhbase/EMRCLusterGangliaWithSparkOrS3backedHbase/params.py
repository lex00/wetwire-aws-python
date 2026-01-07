"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class EMRClusterName(Parameter):
    """Name of the cluster"""

    type = STRING
    description = 'Name of the cluster'
    default = 'emrcluster'


class KeyName(Parameter):
    """Must be an existing Keyname"""

    type = STRING
    description = 'Must be an existing Keyname'


class MasterInstanceType(Parameter):
    """Instance type to be used for the master instance."""

    type = STRING
    description = 'Instance type to be used for the master instance.'
    default = 'm3.xlarge'


class CoreInstanceType(Parameter):
    """Instance type to be used for core instances."""

    type = STRING
    description = 'Instance type to be used for core instances.'
    default = 'm3.xlarge'


class NumberOfCoreInstances(Parameter):
    """Must be a valid number"""

    type = NUMBER
    description = 'Must be a valid number'
    default = 2


class SubnetID(Parameter):
    """Must be Valid public subnet ID"""

    type = STRING
    description = 'Must be Valid public subnet ID'
    default = 'subnet-dba430ad'


class LogUri(Parameter):
    """Must be a valid S3 URL"""

    type = STRING
    description = 'Must be a valid S3 URL'
    default = 's3://emrclusterlogbucket/'


class S3DataUri(Parameter):
    """Must be a valid S3 bucket URL """

    type = STRING
    description = 'Must be a valid S3 bucket URL '
    default = 's3://emrclusterdatabucket/'


class ReleaseLabel(Parameter):
    """Must be a valid EMR release  version"""

    type = STRING
    description = 'Must be a valid EMR release  version'
    default = 'emr-5.7.0'


class Applications(Parameter):
    """Please select which application will be installed on the cluster this would be either Ganglia and spark, or Ganglia and s3 acked Hbase"""

    type = STRING
    description = 'Please select which application will be installed on the cluster this would be either Ganglia and spark, or Ganglia and s3 acked Hbase'
    allowed_values = [
    'Spark',
    'Hbase',
]


class SparkCondition(TemplateCondition):
    logical_id = 'Spark'
    expression = Equals(Applications, 'Spark')


class HbaseCondition(TemplateCondition):
    logical_id = 'Hbase'
    expression = Equals(Applications, 'Hbase')
