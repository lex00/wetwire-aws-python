"""Security resources: DMSVpcRole, DMSCloudwatchRole, S3TargetDMSRole."""

from . import *  # noqa: F403


class DMSVpcRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class DMSVpcRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DMSVpcRoleAllowStatement0]


class DMSVpcRole(iam.Role):
    role_name = 'dms-vpc-role'
    assume_role_policy_document = DMSVpcRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole']
    path = '/'
    condition = 'NotExistsDMSVPCRole'


class DMSCloudwatchRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class DMSCloudwatchRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DMSCloudwatchRoleAllowStatement0]


class DMSCloudwatchRole(iam.Role):
    role_name = 'dms-cloudwatch-logs-role'
    assume_role_policy_document = DMSCloudwatchRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole']
    path = '/'
    condition = 'NotExistsDMSCloudwatchRole'


class S3TargetDMSRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class S3TargetDMSRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [S3TargetDMSRoleAllowStatement0]


class S3TargetDMSRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        's3:PutObject',
        's3:DeleteObject',
    ]
    resource_arn = [
        S3Bucket.Arn,
        Sub('${S3Bucket.Arn}/*'),
    ]


class S3TargetDMSRoleAllowStatement1:
    resource: PolicyStatement
    action = 's3:ListBucket'
    resource_arn = S3Bucket.Arn


class S3TargetDMSRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [S3TargetDMSRoleAllowStatement0_1, S3TargetDMSRoleAllowStatement1]


class S3TargetDMSRolePolicy:
    resource: iam.User.Policy
    policy_name = 'S3AccessForDMSPolicy'
    policy_document = S3TargetDMSRolePolicies0PolicyDocument


class S3TargetDMSRole(iam.Role):
    role_name = 'dms-s3-target-role'
    assume_role_policy_document = S3TargetDMSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [S3TargetDMSRolePolicy]
    depends_on = [S3Bucket]
