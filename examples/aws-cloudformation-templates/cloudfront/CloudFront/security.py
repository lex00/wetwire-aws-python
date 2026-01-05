"""Security resources: LambdaEdgeIAMRole, AdministratorAccessIAMRole, LoggingBucketKMSKey, LoggingBucketKMSKeyAlias."""

from . import *  # noqa: F403


class LambdaEdgeIAMRoleAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowLambdaServiceToAssumeRole'
    principal = {
        'Service': [
            'edgelambda.amazonaws.com',
            'lambda.amazonaws.com',
        ],
    }
    action = ['sts:AssumeRole']


class LambdaEdgeIAMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaEdgeIAMRoleAllowStatement0]


class LambdaEdgeIAMRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['lambda:PublishVersion']
    resource_arn = '*'


class LambdaEdgeIAMRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaEdgeIAMRoleAllowStatement0_1]


class LambdaEdgeIAMRolePolicy:
    resource: iam.User.Policy
    policy_name = 'PublishNewLambdaEdgeVersion'
    policy_document = LambdaEdgeIAMRolePolicies0PolicyDocument


class LambdaEdgeIAMRole(iam.Role):
    role_name = Sub('${AppName}-iam-lambda-edge-role-${Environment}')
    assume_role_policy_document = LambdaEdgeIAMRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole', 'arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess']
    path = '/'
    policies = [LambdaEdgeIAMRolePolicy]


class AdministratorAccessIAMRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class AdministratorAccessIAMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AdministratorAccessIAMRoleAllowStatement0]


class AdministratorAccessIAMRole(iam.Role):
    role_name = Sub('AdministratorAccess-${AppName}')
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AdministratorAccess')]
    assume_role_policy_document = AdministratorAccessIAMRoleAssumeRolePolicyDocument
    path = '/'


class LoggingBucketKMSKeyAllowStatement0:
    resource: PolicyStatement
    sid = 'Enable IAM policies to allow access to the Key'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = ['kms:*']
    resource_arn = '*'


class LoggingBucketKMSKeyAllowStatement1:
    resource: PolicyStatement
    sid = 'Allow administration of the key'
    principal = {
        'AWS': [Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:role/AdministratorAccess-${AppName}')],
    }
    action = [
        'kms:Put*',
        'kms:ScheduleKeyDeletion',
        'kms:CancelKeyDeletion',
        'kms:Describe*',
        'kms:Revoke*',
        'kms:Disable*',
        'kms:Enable*',
        'kms:Delete*',
        'kms:List*',
        'kms:Update*',
        'kms:Create*',
    ]
    resource_arn = '*'


class LoggingBucketKMSKeyKeyPolicy:
    resource: PolicyDocument
    statement = [LoggingBucketKMSKeyAllowStatement0, LoggingBucketKMSKeyAllowStatement1]


class LoggingBucketKMSKey(kms.Key):
    description = 'Logging S3 Bucket KMS Key'
    enabled = True
    enable_key_rotation = True
    key_policy = LoggingBucketKMSKeyKeyPolicy
    depends_on = [AdministratorAccessIAMRole]


class LoggingBucketKMSKeyAlias(kms.Alias):
    alias_name = Sub('alias/${AppName}/${Environment}/s3-logging-kms')
    target_key_id = LoggingBucketKMSKey
