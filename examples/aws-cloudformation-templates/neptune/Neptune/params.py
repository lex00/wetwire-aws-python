"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Env:
    """Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE."""

    resource: Parameter
    type = STRING
    description = 'Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'dev'
    allowed_values = [
    'test',
    'dev',
    'prod',
]


class AppName:
    """Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'appname'


class User:
    """Please specify the User. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'test'


class Owner:
    """Please specify the Owner. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = ''


class Tier:
    """Please specify the Tier. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Tier. Used for tagging'
    default = ''


class Version:
    """Please specify the Application Version. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Application Version. Used for tagging'
    default = ''


class Storage:
    """Please specify the Storage Type. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Storage Type. Used for tagging'
    default = 'ebs'
    allowed_values = [
    'ebs',
    'efs',
    's3',
]


class VPCStack:
    """Please specify the VPC Stack Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify the VPC Stack Name.'
    default = 'vpc'


class DBInstanceClass:
    """Neptune DB instance class that will be used for primary and all replicas"""

    resource: Parameter
    type = STRING
    description = 'Neptune DB instance class that will be used for primary and all replicas'
    default = 'db.r4.large'
    allowed_values = [
    'db.r4.large',
    'db.r4.xlarge',
    'db.r4.2xlarge',
    'db.r4.4xlarge',
    'db.r4.8xlarge',
]


class DBClusterIdentifier:
    """Neptune DB cluster identifier. Must contain from 1 to 63 alphanumeric characters or hyphens. First character must be a letter. Cannot end with a hyphen or contain two consecutive hyphens."""

    resource: Parameter
    type = STRING
    description = 'Neptune DB cluster identifier. Must contain from 1 to 63 alphanumeric characters or hyphens. First character must be a letter. Cannot end with a hyphen or contain two consecutive hyphens.'


class Port:
    """Port used to connect to the Neptune cluster. Must be a valid port number between"""

    resource: Parameter
    type = STRING
    description = 'Port used to connect to the Neptune cluster. Must be a valid port number between'
    default = 8182


class NeptuneQueryTimeout:
    """Neptune DB parameters. Allowed values \"10-2147483647\""""

    resource: Parameter
    type = STRING
    description = 'Neptune DB parameters. Allowed values "10-2147483647"'
    default = 120000


class StorageEncrypted:
    """Data-at-rest encryption"""

    resource: Parameter
    type = STRING
    description = 'Data-at-rest encryption'
    default = False
    allowed_values = [
    True,
    False,
]


class NeptuneDBSubnetGroupName:
    """The name for the DB Subnet Group. This value is stored as a lowercase string. Constraints, Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default."""

    resource: Parameter
    type = STRING
    description = 'The name for the DB Subnet Group. This value is stored as a lowercase string. Constraints, Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.'


class NeptuneSNSTopicArn:
    """Custom SNS topic alarm. Optional. If not provided, an new SNS topic will be created for you"""

    resource: Parameter
    type = STRING
    description = 'Custom SNS topic alarm. Optional. If not provided, an new SNS topic will be created for you'


class SNSEmailSubscription:
    """SNS Email subscription. Optional. If not provided, no alarm subscriptions will be created"""

    resource: Parameter
    type = STRING
    description = 'SNS Email subscription. Optional. If not provided, no alarm subscriptions will be created'
    allowed_pattern = '^[\\w-\\+]+(\\.[\\w]+)*@[\\w-]+(\\.[\\w]+)*(\\.[a-z]{2,})$|^$'


class HighCpuAlarmThreshold:
    """High CPU alarm threshold. Alert when CPU goes above this value.  In percentage used"""

    resource: Parameter
    type = STRING
    description = 'High CPU alarm threshold. Alert when CPU goes above this value.  In percentage used'
    default = 80
    allowed_pattern = '(100|[1-9]?[0-9])$'


class LowMemoryAlarmThreshold:
    """Low memory alarm threshold. Alert when memory falls below this value.  In bytes"""

    resource: Parameter
    type = NUMBER
    description = 'Low memory alarm threshold. Alert when memory falls below this value.  In bytes'
    default = 700000000


class GremlinRequestsPerSecThreshold:
    """Gremlin Requests Per Sec alarm threshold. Alert when Gremlin Requests Per Sec goes above this value. In percentage used"""

    resource: Parameter
    type = STRING
    description = 'Gremlin Requests Per Sec alarm threshold. Alert when Gremlin Requests Per Sec goes above this value. In percentage used'
    default = 10000


class SparqlRequestsPerSecThreshold:
    """Sparql Requests Per Sec alarm threshold. Alert when Sparql Requests Per Sec goes above this value. In percentage used"""

    resource: Parameter
    type = STRING
    description = 'Sparql Requests Per Sec alarm threshold. Alert when Sparql Requests Per Sec goes above this value. In percentage used'
    default = 10000


class UploadAuditLogs:
    """Enable upload of audit logs?"""

    resource: Parameter
    type = STRING
    description = 'Enable upload of audit logs?'
    default = True
    allowed_values = [
    True,
    False,
]


class BackupRetentionPeriod:
    """Backup retention period (in days).  Must be between 1 - 35"""

    resource: Parameter
    type = STRING
    description = 'Backup retention period (in days).  Must be between 1 - 35'
    default = 31
    allowed_pattern = '([1-9]|[12][0-9]|3[0-5])'


class NeptuneDBClusterPreferredMaintenanceWindow:
    """Neptune DB cluster preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window."""

    resource: Parameter
    type = STRING
    description = 'Neptune DB cluster preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window.'
    default = 'mon:03:00-mon:04:00'


class NeptuneDBInstancePreferredMaintenanceWindow:
    """Neptune DB instance preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window."""

    resource: Parameter
    type = STRING
    description = 'Neptune DB instance preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window.'
    default = 'mon:03:00-mon:04:00'


class NeptuneDBClusterPreferredBackupWindow:
    """Neptune DB cluster preferred backup window. Constrains - Must be in the format hh24:mi-hh24:mi. Must be in Universal Coordinated Time (UTC). Must not conflict with the preferred maintenance window. Must be at least 30 minutes."""

    resource: Parameter
    type = STRING
    description = 'Neptune DB cluster preferred backup window. Constrains - Must be in the format hh24:mi-hh24:mi. Must be in Universal Coordinated Time (UTC). Must not conflict with the preferred maintenance window. Must be at least 30 minutes.'
    default = '02:00-03:00'


class MajorVersionUpgrade:
    """Neptune DB major version upgrade"""

    resource: Parameter
    type = STRING
    description = 'Neptune DB major version upgrade'
    default = True
    allowed_values = [
    True,
    False,
]


class MinorVersionUpgrade:
    """Neptune DB minor version upgrade"""

    resource: Parameter
    type = STRING
    description = 'Neptune DB minor version upgrade'
    default = True
    allowed_values = [
    True,
    False,
]


class IAMAuthEnabled:
    """Neptune DB IAM authentication"""

    resource: Parameter
    type = STRING
    description = 'Neptune DB IAM authentication'
    default = False
    allowed_values = [
    True,
    False,
]


class EnableAuditLogUploadCondition:
    resource: TemplateCondition
    logical_id = 'EnableAuditLogUpload'
    expression = Equals(UploadAuditLogs, True)


class CreateSnsTopicCondition:
    resource: TemplateCondition
    logical_id = 'CreateSnsTopic'
    expression = Equals(NeptuneSNSTopicArn, '')


class CreateSnsSubscriptionCondition:
    resource: TemplateCondition
    logical_id = 'CreateSnsSubscription'
    expression = Not(Equals(SNSEmailSubscription, ''))
