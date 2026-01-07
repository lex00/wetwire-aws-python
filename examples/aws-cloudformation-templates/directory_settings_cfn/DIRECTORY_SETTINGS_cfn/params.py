"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CreateDirectoryConsoleDelegatedAccessRoles(Parameter):
    """Create sample IAM ROLES that can be used to delegate users/groups access to certain areas of the AWS Management Console. User/Group assignment to these IAM roles has to be done manually via Directory Services -> Directory -> Application Management Tab."""

    type = STRING
    description = 'Create sample IAM ROLES that can be used to delegate users/groups access to certain areas of the AWS Management Console. User/Group assignment to these IAM roles has to be done manually via Directory Services -> Directory -> Application Management Tab.'
    default = 'No'
    allowed_values = [
    'Yes',
    'No',
]


class CreateDirectoryAlias(Parameter):
    """Create an alias for the directory. The alias is used to construct the access URL for the directory, such as http://<alias>.awsapps.com. NOTE, after an alias has been created, it cannot be deleted or reused. Hence if a different alias already exists, then you must use the existing alias (also shown in CloudFormation error)."""

    type = STRING
    description = 'Create an alias for the directory. The alias is used to construct the access URL for the directory, such as http://<alias>.awsapps.com. NOTE, after an alias has been created, it cannot be deleted or reused. Hence if a different alias already exists, then you must use the existing alias (also shown in CloudFormation error).'
    default = 'No'
    allowed_values = [
    'Yes',
    'No',
]


class DirectoryAlias(Parameter):
    """(Optional) Specifies an alias to be assigned to the directory, such as http://<alias>.awsapps.com. Note, after alias is created it cannot be deleted or reused. Note, will only be set, if `CreateDirectoryAlias` parameter, has a value of `Yes`."""

    type = STRING
    description = '(Optional) Specifies an alias to be assigned to the directory, such as http://<alias>.awsapps.com. Note, after alias is created it cannot be deleted or reused. Note, will only be set, if `CreateDirectoryAlias` parameter, has a value of `Yes`.'
    allowed_pattern = '^$|^(?!d-)([\\da-zA-Z]+)([-]*[\\da-zA-Z])*$'
    max_length = 62


class DirectoryID(Parameter):
    """Directory ID that will have settings updated"""

    type = STRING
    description = 'Directory ID that will have settings updated'
    allowed_pattern = '^d-[0-9a-f]{10}$'


class DirectoryMonitoringEmail(Parameter):
    """Email for SNS Topic to monitor directory changes."""

    type = STRING
    description = 'Email for SNS Topic to monitor directory changes.'
    allowed_pattern = '^[\\w%+.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,63}$'


class DirectoryMonitoringSNSTopicKMSKey(Parameter):
    """(Optional) KMS Key ID to use for encrypting the directory monitoring SNS topic messages. If empty, encryption is enabled with SNS managing the server-side encryption keys."""

    type = STRING
    description = '(Optional) KMS Key ID to use for encrypting the directory monitoring SNS topic messages. If empty, encryption is enabled with SNS managing the server-side encryption keys.'
    allowed_pattern = '^$|^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$'
    constraint_description = 'Key ID example: 1234abcd-12ab-34cd-56ef-1234567890ab'


class EnableDirectorySSO(Parameter):
    """Enable single sign-on for a directory. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If true, "DirectoryAlias" must also be true, & "DirectoryAlias" parameter input required."""

    type = STRING
    description = 'Enable single sign-on for a directory. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If true, "DirectoryAlias" must also be true, & "DirectoryAlias" parameter input required.'
    default = 'No'
    allowed_values = [
    'Yes',
    'No',
]


class LambdaFunctionName(Parameter):
    """Lambda Function Name for Custom Resource"""

    type = STRING
    description = 'Lambda Function Name for Custom Resource'
    default = 'CR-DirectorySettings'
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


class LambdaLogsCloudWatchKMSKey(Parameter):
    """(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys."""

    type = STRING
    description = '(Optional) KMS Key ARN to use for encrypting the Lambda logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.'
    allowed_pattern = '^$|^arn:(aws[a-zA-Z-]*)?:kms:[a-z0-9-]+:\\d{12}:key\\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$'
    constraint_description = 'Key ARN example:  arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'


class LambdaS3BucketName(Parameter):
    """Lambda S3 bucket name for the Lambda deployment package. Lambda bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    type = STRING
    description = 'Lambda S3 bucket name for the Lambda deployment package. Lambda bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'Lambda S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


class LambdaZipFileName(Parameter):
    """Amazon S3 key of the deployment package."""

    type = STRING
    description = 'Amazon S3 key of the deployment package.'
    default = 'directory_settings_custom_resource.zip'
    min_length = 1
    max_length = 1024


class Subnets(Parameter):
    type = LIST_SUBNET_ID


class SecurityGroups(Parameter):
    type = LIST_SECURITY_GROUP_ID


class DirectoryConsoleDelegatedAccessRolesConditionCondition(TemplateCondition):
    logical_id = 'DirectoryConsoleDelegatedAccessRolesCondition'
    expression = Equals(CreateDirectoryConsoleDelegatedAccessRoles, 'Yes')


class DirectoryMonitoringSNSTopicKMSKeyConditionCondition(TemplateCondition):
    logical_id = 'DirectoryMonitoringSNSTopicKMSKeyCondition'
    expression = Not(Equals(DirectoryMonitoringSNSTopicKMSKey, ''))


class LambdaLogsCloudWatchKMSKeyConditionCondition(TemplateCondition):
    logical_id = 'LambdaLogsCloudWatchKMSKeyCondition'
    expression = Not(Equals(LambdaLogsCloudWatchKMSKey, ''))
