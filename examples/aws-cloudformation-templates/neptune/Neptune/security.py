"""Security resources: NeptuneCloudWatchPolicy, NeptuneS3Policy, NeptuneRole."""

from . import *  # noqa: F403


class NeptuneCloudWatchPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'EnableLogGroups'
    action = [
        'logs:CreateLogGroup',
        'logs:PutRetentionPolicy',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*')]


class NeptuneCloudWatchPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'EnableLogStreams'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'logs:DescribeLogStreams',
        'logs:GetLogEvents',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:*:*:log-group:/aws/neptune/*:log-stream:*')]


class NeptuneCloudWatchPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneCloudWatchPolicyAllowStatement0, NeptuneCloudWatchPolicyAllowStatement1]


class NeptuneCloudWatchPolicy(iam.ManagedPolicy):
    description = 'Default policy for CloudWatch logs'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-cw-policy-${AWS::Region}')
    policy_document = NeptuneCloudWatchPolicyPolicyDocument


class NeptuneS3PolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowNeptuneAccessToS3'
    action = [
        's3:Get*',
        's3:List*',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::*')]


class NeptuneS3PolicyPolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneS3PolicyAllowStatement0]


class NeptuneS3Policy(iam.ManagedPolicy):
    description = 'Neptune default policy for S3 access for data load'
    managed_policy_name = Sub('${Env}-${AppName}-neptune-s3-policy-${AWS::Region}')
    policy_document = NeptuneS3PolicyPolicyDocument


class NeptuneRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': [
            'monitoring.rds.amazonaws.com',
            'rds.amazonaws.com',
        ],
    }
    action = 'sts:AssumeRole'


class NeptuneRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [NeptuneRoleAllowStatement0]


class NeptuneRole(iam.Role):
    role_name = Sub('${Env}-${AppName}-neptune-iam-role-${AWS::Region}')
    assume_role_policy_document = NeptuneRoleAssumeRolePolicyDocument
    managed_policy_arns = [NeptuneCloudWatchPolicy, NeptuneS3Policy]
    condition = 'EnableAuditLogUpload'
