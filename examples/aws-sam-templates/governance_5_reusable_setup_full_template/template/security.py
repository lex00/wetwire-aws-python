"""Security resources: ConfigRole."""

from . import *  # noqa: F403


class ConfigRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'config.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class ConfigRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [ConfigRoleAllowStatement0]


class ConfigRolePolicy(iam.User.Policy):
    policy_name = 'S3ConfigPolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': [
                's3:PutObject',
                's3:GetBucketAcl',
            ],
            'Effect': 'Allow',
            'Resource': [
                DataBucket.Arn,
                Sub('${BucketArn}/*', {
    'BucketArn': DataBucket.Arn,
}),
            ],
        },
    }


class ConfigRolePolicy1(iam.User.Policy):
    policy_name = 'SNSConfigPolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': ['sns:Publish'],
            'Effect': 'Allow',
            'Resource': [NotificationTopic],
        },
    }


class ConfigRole(iam.Role):
    assume_role_policy_document = ConfigRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSConfigRole']
    policies = [ConfigRolePolicy, ConfigRolePolicy1]
