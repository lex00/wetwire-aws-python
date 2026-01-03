"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CreateVPCFlowLogsToCloudWatch:
    """Create VPC flow logs for the VPC and publish them to CloudWatch"""

    resource: Parameter
    type = STRING
    description = 'Create VPC flow logs for the VPC and publish them to CloudWatch'
    default = 'No'
    allowed_values = [
    'Yes',
    'No',
]


class CreateVPCFlowLogsToS3:
    """Create VPC flow logs for the VPC and publish them to S3"""

    resource: Parameter
    type = STRING
    description = 'Create VPC flow logs for the VPC and publish them to S3'
    default = 'No'
    allowed_values = [
    'Yes',
    'No',
]


class S3AccessLogsBucketName:
    """(Optional) S3 Server Access Logs bucket name for where Amazon S3 should store server access log files. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created as a destination for S3 server access logs, it will follow the format, aws-s3-access-logs-<account>-<region>"""

    resource: Parameter
    type = STRING
    description = '(Optional) S3 Server Access Logs bucket name for where Amazon S3 should store server access log files. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created as a destination for S3 server access logs, it will follow the format, aws-s3-access-logs-<account>-<region>'
    allowed_pattern = '^$|^(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


class TemplatesS3BucketName:
    """Templates S3 bucket name for the CloudFormation templates. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    resource: Parameter
    type = STRING
    description = 'Templates S3 bucket name for the CloudFormation templates. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '^(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'Templates S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


class TemplatesS3BucketRegion:
    """The AWS Region where the Templates S3 bucket (TemplatesS3BucketName) is hosted."""

    resource: Parameter
    type = STRING
    description = 'The AWS Region where the Templates S3 bucket (TemplatesS3BucketName) is hosted.'


class VPCFlowLogsBucketKeyEnabled:
    """Set to true to have Amazon S3 use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS). If false, S3 Bucket Key is not enabled. Note, will only be set if KMS Key parameter, "VPCFlowLogsBucketKMSKey", was provided."""

    resource: Parameter
    type = STRING
    description = 'Set to true to have Amazon S3 use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS). If false, S3 Bucket Key is not enabled. Note, will only be set if KMS Key parameter, "VPCFlowLogsBucketKMSKey", was provided.'
    default = False
    allowed_values = [
    True,
    False,
]


class VPCFlowLogsBucketKMSKey:
    """(Optional) KMS Key ID or ARN to use for the default encryption. If empty, server-side encryption with Amazon S3-managed encryption keys (SSE-S3) will be used. Note, will only be set if S3 Bucket parameter, "VPCFlowLogsBucketName", was not provided, thus a new S3 bucket is being created."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ID or ARN to use for the default encryption. If empty, server-side encryption with Amazon S3-managed encryption keys (SSE-S3) will be used. Note, will only be set if S3 Bucket parameter, "VPCFlowLogsBucketName", was not provided, thus a new S3 bucket is being created.'
    allowed_pattern = '^$|^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ID example: 1234abcd-12ab-34cd-56ef-1234567890ab  Key ARN examlpe:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


class VPCFlowLogsBucketName:
    """(Optional) S3 bucket name where VPC Flow Log data can be published. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created for VPC Flow Log data to be published."""

    resource: Parameter
    type = STRING
    description = '(Optional) S3 bucket name where VPC Flow Log data can be published. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-). If empty, a new S3 bucket will be created for VPC Flow Log data to be published.'
    allowed_pattern = '^$|^(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


class VPCFlowLogsCloudWatchKMSKey:
    """(Optional) KMS Key ARN to use for encrypting the VPC flow logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    resource: Parameter
    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the VPC flow logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


class VPCFlowLogsLogFormat:
    """The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value."""

    resource: Parameter
    type = STRING
    description = 'The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.'
    default = '${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}'
    allowed_pattern = '^(\\$\\{[a-z-]+\\})$|^((\\$\\{[a-z-]+\\} )*\\$\\{[a-z-]+\\})$'


class VPCFlowLogsLogGroupRetention:
    """Number of days to retain the VPC Flow Logs in CloudWatch"""

    resource: Parameter
    type = STRING
    description = 'Number of days to retain the VPC Flow Logs in CloudWatch'
    default = 14
    allowed_values = [
    1,
    3,
    5,
    7,
    14,
    30,
    60,
    90,
    120,
    150,
    180,
    365,
    400,
    545,
    731,
    1827,
    3653,
]


class VPCFlowLogsMaxAggregationInterval:
    """The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes)."""

    resource: Parameter
    type = STRING
    description = 'The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).'
    default = 600
    allowed_values = [
    60,
    600,
]


class VPCFlowLogsTrafficType:
    """The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic."""

    resource: Parameter
    type = STRING
    description = 'The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.'
    default = 'REJECT'
    allowed_values = [
    'ACCEPT',
    'ALL',
    'REJECT',
]


class VPCID:
    """ID of the VPC (e.g., vpc-0343606e)"""

    resource: Parameter
    type = VPC_ID
    description = 'ID of the VPC (e.g., vpc-0343606e)'


class VPCFlowLogsToCloudWatchConditionCondition:
    resource: TemplateCondition
    logical_id = 'VPCFlowLogsToCloudWatchCondition'
    expression = Equals(CreateVPCFlowLogsToCloudWatch, 'Yes')


class VPCFlowLogsToS3ConditionCondition:
    resource: TemplateCondition
    logical_id = 'VPCFlowLogsToS3Condition'
    expression = Equals(CreateVPCFlowLogsToS3, 'Yes')
