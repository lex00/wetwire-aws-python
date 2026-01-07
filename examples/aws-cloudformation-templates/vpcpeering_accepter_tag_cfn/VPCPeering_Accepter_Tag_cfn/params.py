"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class LambdaFunctionName(Parameter):
    """Lambda Function Name for Custom Resource"""

    type = STRING
    description = 'Lambda Function Name for Custom Resource'
    default = 'CR-TagVpcPeeringConnections'
    allowed_pattern = '^[\\w-]{1,64}$'
    constraint_description = 'Max 64 alphanumeric characters. Also special characters supported [_, -]'


class LambdaLogLevel(Parameter):
    """Lambda logging level"""

    type = STRING
    description = 'Lambda logging level'
    default = 'INFO'
    allowed_values = [
    'INFO',
    'DEBUG',
]


class LambdaLogsCloudWatchKMSKey(Parameter):
    """(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


class LambdaLogsLogGroupRetention(Parameter):
    """Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs"""

    type = STRING
    description = 'Specifies the number of days you want to retain Lambda log events in the CloudWatch Logs'
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


class PeerName(Parameter):
    """Name of the VPC Peer"""

    type = STRING
    description = 'Name of the VPC Peer'
    max_length = 255


class VPCPeeringConnectionId(Parameter):
    """ID of the VPC Peering Connection"""

    type = STRING
    description = 'ID of the VPC Peering Connection'
    allowed_pattern = '^pcx-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "pcx-". Followed by 17 characters (numbers, letters "a-f")'


class LambdaLogsCloudWatchKMSKeyConditionCondition(TemplateCondition):
    logical_id = 'LambdaLogsCloudWatchKMSKeyCondition'
    expression = Not(Equals(LambdaLogsCloudWatchKMSKey, ''))
