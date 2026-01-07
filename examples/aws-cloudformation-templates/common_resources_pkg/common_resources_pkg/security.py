"""Security resources: StorageReplicationRole, StorageReplicationPolicy."""

from . import *  # noqa: F403


class StorageReplicationRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class StorageReplicationRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [StorageReplicationRoleAllowStatement0]


class StorageReplicationRole(iam.Role):
    assume_role_policy_document = StorageReplicationRoleAssumeRolePolicyDocument
    path = '/'


class StorageReplicationPolicyAllowStatement0(PolicyStatement):
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


class StorageReplicationPolicyAllowStatement1(PolicyStatement):
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


class StorageReplicationPolicyAllowStatement2(PolicyStatement):
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


class StorageReplicationPolicyPolicyDocument(PolicyDocument):
    statement = [StorageReplicationPolicyAllowStatement0, StorageReplicationPolicyAllowStatement1, StorageReplicationPolicyAllowStatement2]


class StorageReplicationPolicy(iam.RolePolicy):
    policy_document = StorageReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = StorageReplicationRole
