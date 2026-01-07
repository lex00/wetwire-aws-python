"""Security resources: KmsKey, ReplicationRole, KmsKeyAlias."""

from . import *  # noqa: F403


class KmsKeyAllowStatement0(PolicyStatement):
    sid = 'Allow source account access to KMS key in source account'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 'kms:*'
    resource_arn = '*'


class KmsKeyKeyPolicy(PolicyDocument):
    statement = [KmsKeyAllowStatement0]


class KmsKey(kms.Key):
    resource: kms.Key
    enable_key_rotation = True
    key_policy = KmsKeyKeyPolicy


class ReplicationRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 's3.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class ReplicationRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [ReplicationRoleAllowStatement0]


class ReplicationRoleAllowStatement0_1(PolicyStatement):
    sid = 'AllowActionsOnSourceBucket'
    action = [
        's3:ListBucket',
        's3:GetReplicationConfiguration',
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
    ]
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AWS::AccountId}-bucket/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AWS::AccountId}-bucket'),
    ]


class ReplicationRoleAllowStatement1(PolicyStatement):
    sid = 'AllowActionsOnDestinationBucket'
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicateTags',
        's3:GetObjectVersionTagging',
        's3:ObjectOwnerOverrideToBucketOwner',
    ]
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AccountIdDestination}-bucket/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AccountIdDestination}-bucket'),
    ]


class ReplicationRoleAllowStatement2(PolicyStatement):
    sid = 'AllowKmsDecryptOnSourceKey'
    action = 'kms:Decrypt'
    resource_arn = KmsKey.Arn


class ReplicationRoleAllowStatement3(PolicyStatement):
    sid = 'AllowKmsEncryptOnDestinationKey'
    action = 'kms:Encrypt'
    resource_arn = '*'
    condition = {
        STRING_EQUALS: {
            'kms:RequestAlias': Sub('alias/${AWS::StackName}-${AccountIdDestination}-kms-key'),
        },
    }


class ReplicationRolePolicies0PolicyDocument(PolicyDocument):
    statement = [ReplicationRoleAllowStatement0_1, ReplicationRoleAllowStatement1, ReplicationRoleAllowStatement2, ReplicationRoleAllowStatement3]


class ReplicationRolePolicy(iam.User.Policy):
    policy_name = Sub('${AWS::StackName}-${AccountIdDestination}-role-policy')
    policy_document = ReplicationRolePolicies0PolicyDocument


class ReplicationRole(iam.Role):
    resource: iam.Role
    role_name = Sub('${AWS::StackName}-${AccountIdDestination}-role')
    description = 'IAM Role used by S3 bucket replication'
    assume_role_policy_document = ReplicationRoleAssumeRolePolicyDocument
    policies = [ReplicationRolePolicy]


class KmsKeyAlias(kms.Alias):
    resource: kms.Alias
    alias_name = Sub('alias/${AWS::StackName}-${AWS::AccountId}-kms-key')
    target_key_id = KmsKey
