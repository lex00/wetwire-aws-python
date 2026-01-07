"""Security resources: DMSCloudwatchRole, DMSVpcRole, S3TargetDMSRole."""

from . import *  # noqa: F403


class DMSCloudwatchRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class DMSCloudwatchRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [DMSCloudwatchRoleAllowStatement0]


class DMSCloudwatchRole(iam.Role):
    resource: iam.Role
    role_name = 'dms-cloudwatch-logs-role'
    assume_role_policy_document = DMSCloudwatchRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSCloudWatchLogsRole']
    path = '/'
    condition = 'NotExistsDMSCloudwatchRole'


class DMSVpcRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class DMSVpcRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [DMSVpcRoleAllowStatement0]


class DMSVpcRole(iam.Role):
    resource: iam.Role
    role_name = 'dms-vpc-role'
    assume_role_policy_document = DMSVpcRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonDMSVPCManagementRole']
    path = '/'
    condition = 'NotExistsDMSVPCRole'


class S3TargetDMSRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['dms.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class S3TargetDMSRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [S3TargetDMSRoleAllowStatement0]


class S3TargetDMSRoleAllowStatement0_1(PolicyStatement):
    action = [
        's3:PutObject',
        's3:DeleteObject',
    ]
    resource_arn = [
        S3Bucket.Arn,
        Sub('${S3Bucket.Arn}/*'),
    ]


class S3TargetDMSRoleAllowStatement1(PolicyStatement):
    action = 's3:ListBucket'
    resource_arn = S3Bucket.Arn


class S3TargetDMSRolePolicies0PolicyDocument(PolicyDocument):
    statement = [S3TargetDMSRoleAllowStatement0_1, S3TargetDMSRoleAllowStatement1]


class S3TargetDMSRolePolicy(iam.User.Policy):
    policy_name = 'S3AccessForDMSPolicy'
    policy_document = S3TargetDMSRolePolicies0PolicyDocument


class S3TargetDMSRole(iam.Role):
    resource: iam.Role
    role_name = 'dms-s3-target-role'
    assume_role_policy_document = S3TargetDMSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [S3TargetDMSRolePolicy]
    depends_on = [S3Bucket]
