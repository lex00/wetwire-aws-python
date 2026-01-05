"""Security resources: CentralEventLogKey."""

from . import *  # noqa: F403


class CentralEventLogKeyAllowStatement0(PolicyStatement):
    principal = {
        'AWS': [Sub('arn:aws:iam::${AWS::AccountId}:role/Admin')],
    }
    action = [
        'kms:Create*',
        'kms:Describe*',
        'kms:Enable*',
        'kms:List*',
        'kms:Put*',
        'kms:Update*',
        'kms:Revoke*',
        'kms:Disable*',
        'kms:Get*',
        'kms:Delete*',
        'kms:ScheduleKeyDeletion',
        'kms:CancelKeyDeletion',
        'kms:GenerateDataKey',
        'kms:TagResource',
        'kms:UntagResource',
    ]
    resource_arn = Sub('arn:aws:kms:${AWS::Region}:${AWS::AccountId}:key/*')


class CentralEventLogKeyAllowStatement1(PolicyStatement):
    sid = 'Allow CloudWatch Logs to use the key'
    principal = {
        'Service': 'logs.amazonaws.com',
    }
    action = [
        'kms:Encrypt*',
        'kms:Decrypt*',
        'kms:ReEncrypt*',
        'kms:GenerateDataKey*',
        'kms:Describe*',
    ]
    resource_arn = Sub('arn:aws:kms:${AWS::Region}:${AWS::AccountId}:key/*')


class CentralEventLogKeyKeyPolicy(PolicyDocument):
    statement = [CentralEventLogKeyAllowStatement0, CentralEventLogKeyAllowStatement1]


class CentralEventLogKey(kms.Key):
    description = 'KMS key for log group'
    enable_key_rotation = True
    key_policy = CentralEventLogKeyKeyPolicy
