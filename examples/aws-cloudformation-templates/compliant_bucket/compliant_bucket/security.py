"""Security resources: ObjectStorageReplicationRole, ObjectStorageReplicationPolicy."""

from . import *  # noqa: F403


class ObjectStorageReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ObjectStorageReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageReplicationRoleAllowStatement0]


class ObjectStorageReplicationRole:
    resource: iam.Role
    assume_role_policy_document = ObjectStorageReplicationRoleAssumeRolePolicyDocument
    path = '/'


class ObjectStorageReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


class ObjectStorageReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


class ObjectStorageReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


class ObjectStorageReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageReplicationPolicyAllowStatement0, ObjectStorageReplicationPolicyAllowStatement1, ObjectStorageReplicationPolicyAllowStatement2]


class ObjectStorageReplicationPolicy:
    resource: iam.RolePolicy
    policy_document = ObjectStorageReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ObjectStorageReplicationRole
