"""Security resources: KmsKey, KmsKeyAlias."""

from . import *  # noqa: F403


class KmsKeyAllowStatement0:
    resource: PolicyStatement
    sid = 'Allow destination account access to KMS key in destination account'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 'kms:*'
    resource_arn = '*'


class KmsKeyAllowStatement1:
    resource: PolicyStatement
    sid = 'Allow source account access to KMS key in destination account'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AccountIdSource}:root'),
    }
    action = [
        'kms:Encrypt',
        'kms:ReEncrypt*',
        'kms:GenerateDataKey*',
        'kms:DescribeKey',
    ]
    resource_arn = '*'


class KmsKeyKeyPolicy:
    resource: PolicyDocument
    statement = [KmsKeyAllowStatement0, KmsKeyAllowStatement1]


class KmsKey:
    resource: kms.Key
    enable_key_rotation = True
    key_policy = KmsKeyKeyPolicy


class KmsKeyAlias:
    resource: kms.Alias
    alias_name = Sub('alias/${AWS::StackName}-${AWS::AccountId}-kms-key')
    target_key_id = KmsKey
