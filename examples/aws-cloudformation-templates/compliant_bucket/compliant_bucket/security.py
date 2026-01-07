"""Security resources: ObjectStorageReplicationRole, ObjectStorageReplicationPolicy."""

from . import *  # noqa: F403


class ObjectStorageReplicationRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ObjectStorageReplicationRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [ObjectStorageReplicationRoleAllowStatement0]


class ObjectStorageReplicationRole(iam.Role):
    assume_role_policy_document = ObjectStorageReplicationRoleAssumeRolePolicyDocument
    path = '/'


class ObjectStorageReplicationPolicyAllowStatement0(PolicyStatement):
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


class ObjectStorageReplicationPolicyAllowStatement1(PolicyStatement):
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


class ObjectStorageReplicationPolicyAllowStatement2(PolicyStatement):
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


class ObjectStorageReplicationPolicyPolicyDocument(PolicyDocument):
    statement = [ObjectStorageReplicationPolicyAllowStatement0, ObjectStorageReplicationPolicyAllowStatement1, ObjectStorageReplicationPolicyAllowStatement2]


class ObjectStorageReplicationPolicy(iam.RolePolicy):
    policy_document = ObjectStorageReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ObjectStorageReplicationRole
