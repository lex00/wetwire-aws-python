"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Env(Parameter):
    """Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE."""

    type = STRING
    description = 'Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'dev'
    allowed_values = [
    'test',
    'dev',
    'prod',
]


class AppName(Parameter):
    """Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE."""

    type = STRING
    description = 'Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'appname'


class User(Parameter):
    """Please specify the User. Used for tagging"""

    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'test'


class Owner(Parameter):
    """Please specify the Owner. Used for tagging"""

    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = ''


class Tier(Parameter):
    """Please specify the Tier. Used for tagging"""

    type = STRING
    description = 'Please specify the Tier. Used for tagging'
    default = ''


class Version(Parameter):
    """Please specify the Application Version. Used for tagging"""

    type = STRING
    description = 'Please specify the Application Version. Used for tagging'
    default = ''


class Storage(Parameter):
    """Please specify the Storage Type. Used for tagging"""

    type = STRING
    description = 'Please specify the Storage Type. Used for tagging'
    default = 'ebs'
    allowed_values = [
    'ebs',
    'efs',
    's3',
]


class VPCStack(Parameter):
    """Please specify the VPC Stack Name."""

    type = STRING
    description = 'Please specify the VPC Stack Name.'
    default = 'vpc'


class DBInstanceClass(Parameter):
    """Neptune DB instance class that will be used for primary and all replicas"""

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


class DBClusterIdentifier(Parameter):
    """Neptune DB cluster identifier. Must contain from 1 to 63 alphanumeric characters or hyphens. First character must be a letter. Cannot end with a hyphen or contain two consecutive hyphens."""

    type = STRING
    description = 'Neptune DB cluster identifier. Must contain from 1 to 63 alphanumeric characters or hyphens. First character must be a letter. Cannot end with a hyphen or contain two consecutive hyphens.'


class Port(Parameter):
    """Port used to connect to the Neptune cluster. Must be a valid port number between"""

    type = STRING
    description = 'Port used to connect to the Neptune cluster. Must be a valid port number between'
    default = 8182


class NeptuneQueryTimeout(Parameter):
    """Neptune DB parameters. Allowed values \"10-2147483647\""""

    type = STRING
    description = 'Neptune DB parameters. Allowed values "10-2147483647"'
    default = 120000


class StorageEncrypted(Parameter):
    """Data-at-rest encryption"""

    type = STRING
    description = 'Data-at-rest encryption'
    default = False
    allowed_values = [
    True,
    False,
]


class NeptuneDBSubnetGroupName(Parameter):
    """The name for the DB Subnet Group. This value is stored as a lowercase string. Constraints, Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default."""

    type = STRING
    description = 'The name for the DB Subnet Group. This value is stored as a lowercase string. Constraints, Must contain no more than 255 letters, numbers, periods, underscores, spaces, or hyphens. Must not be default.'


class NeptuneSNSTopicArn(Parameter):
    """Custom SNS topic alarm. Optional. If not provided, an new SNS topic will be created for you"""

    type = STRING
    description = 'Custom SNS topic alarm. Optional. If not provided, an new SNS topic will be created for you'


class SNSEmailSubscription(Parameter):
    """SNS Email subscription. Optional. If not provided, no alarm subscriptions will be created"""

    type = STRING
    description = 'SNS Email subscription. Optional. If not provided, no alarm subscriptions will be created'
    allowed_pattern = '^[\\w-\\+]+(\\.[\\w]+)*@[\\w-]+(\\.[\\w]+)*(\\.[a-z]{2,})$|^$'


class HighCpuAlarmThreshold(Parameter):
    """High CPU alarm threshold. Alert when CPU goes above this value.  In percentage used"""

    type = STRING
    description = 'High CPU alarm threshold. Alert when CPU goes above this value.  In percentage used'
    default = 80
    allowed_pattern = '(100|[1-9]?[0-9])$'


class LowMemoryAlarmThreshold(Parameter):
    """Low memory alarm threshold. Alert when memory falls below this value.  In bytes"""

    type = NUMBER
    description = 'Low memory alarm threshold. Alert when memory falls below this value.  In bytes'
    default = 700000000


class GremlinRequestsPerSecThreshold(Parameter):
    """Gremlin Requests Per Sec alarm threshold. Alert when Gremlin Requests Per Sec goes above this value. In percentage used"""

    type = STRING
    description = 'Gremlin Requests Per Sec alarm threshold. Alert when Gremlin Requests Per Sec goes above this value. In percentage used'
    default = 10000


class SparqlRequestsPerSecThreshold(Parameter):
    """Sparql Requests Per Sec alarm threshold. Alert when Sparql Requests Per Sec goes above this value. In percentage used"""

    type = STRING
    description = 'Sparql Requests Per Sec alarm threshold. Alert when Sparql Requests Per Sec goes above this value. In percentage used'
    default = 10000


class UploadAuditLogs(Parameter):
    """Enable upload of audit logs?"""

    type = STRING
    description = 'Enable upload of audit logs?'
    default = 'Yes'
    allowed_values = [
    'Yes',
    'No',
]


class BackupRetentionPeriod(Parameter):
    """Backup retention period (in days).  Must be between 1 - 35"""

    type = STRING
    description = 'Backup retention period (in days).  Must be between 1 - 35'
    default = 31
    allowed_pattern = '([1-9]|[12][0-9]|3[0-5])'


class NeptuneDBClusterPreferredMaintenanceWindow(Parameter):
    """Neptune DB cluster preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window."""

    type = STRING
    description = 'Neptune DB cluster preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window.'
    default = 'mon:03:00-mon:04:00'


class NeptuneDBInstancePreferredMaintenanceWindow(Parameter):
    """Neptune DB instance preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window."""

    type = STRING
    description = 'Neptune DB instance preferred maintenance window. Format - ddd:hh24:mi-ddd:hh24:mi. Valid Days - Mon, Tue, Wed, Thu, Fri, Sat, Sun. Constraints - Minimum 30-minute window.'
    default = 'mon:03:00-mon:04:00'


class NeptuneDBClusterPreferredBackupWindow(Parameter):
    """Neptune DB cluster preferred backup window. Constrains - Must be in the format hh24:mi-hh24:mi. Must be in Universal Coordinated Time (UTC). Must not conflict with the preferred maintenance window. Must be at least 30 minutes."""

    type = STRING
    description = 'Neptune DB cluster preferred backup window. Constrains - Must be in the format hh24:mi-hh24:mi. Must be in Universal Coordinated Time (UTC). Must not conflict with the preferred maintenance window. Must be at least 30 minutes.'
    default = '02:00-03:00'


class MajorVersionUpgrade(Parameter):
    """Neptune DB major version upgrade"""

    type = STRING
    description = 'Neptune DB major version upgrade'
    default = True
    allowed_values = [
    True,
    False,
]


class MinorVersionUpgrade(Parameter):
    """Neptune DB minor version upgrade"""

    type = STRING
    description = 'Neptune DB minor version upgrade'
    default = True
    allowed_values = [
    True,
    False,
]


class IAMAuthEnabled(Parameter):
    """Neptune DB IAM authentication"""

    type = STRING
    description = 'Neptune DB IAM authentication'
    default = False
    allowed_values = [
    True,
    False,
]


class EnableAuditLogUploadCondition(TemplateCondition):
    logical_id = 'EnableAuditLogUpload'
    expression = Equals(UploadAuditLogs, 'Yes')


class CreateSnsTopicCondition(TemplateCondition):
    logical_id = 'CreateSnsTopic'
    expression = Equals(NeptuneSNSTopicArn, '')


class CreateSnsSubscriptionCondition(TemplateCondition):
    logical_id = 'CreateSnsSubscription'
    expression = Not(Equals(SNSEmailSubscription, ''))
