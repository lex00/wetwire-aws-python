"""Security resources: CloudFrontLogsReplicationRole, ContentReplicationRole, CloudFrontLogsReplicationPolicy, ContentReplicationPolicy."""

from . import *  # noqa: F403


class CloudFrontLogsReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class CloudFrontLogsReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsReplicationRoleAllowStatement0]


class CloudFrontLogsReplicationRole:
    resource: iam.Role
    assume_role_policy_document = CloudFrontLogsReplicationRoleAssumeRolePolicyDocument
    path = '/'


class ContentReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ContentReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ContentReplicationRoleAllowStatement0]


class ContentReplicationRole:
    resource: iam.Role
    assume_role_policy_document = ContentReplicationRoleAssumeRolePolicyDocument
    path = '/'


class CloudFrontLogsReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')


class CloudFrontLogsReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')


class CloudFrontLogsReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')


class CloudFrontLogsReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsReplicationPolicyAllowStatement0, CloudFrontLogsReplicationPolicyAllowStatement1, CloudFrontLogsReplicationPolicyAllowStatement2]


class CloudFrontLogsReplicationPolicy:
    resource: iam.RolePolicy
    policy_document = CloudFrontLogsReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = CloudFrontLogsReplicationRole


class ContentReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


class ContentReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


class ContentReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


class ContentReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentReplicationPolicyAllowStatement0, ContentReplicationPolicyAllowStatement1, ContentReplicationPolicyAllowStatement2]


class ContentReplicationPolicy:
    resource: iam.RolePolicy
    policy_document = ContentReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ContentReplicationRole
