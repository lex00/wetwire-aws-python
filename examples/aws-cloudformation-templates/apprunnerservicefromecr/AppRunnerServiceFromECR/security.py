"""Security resources: AppRunnerRole."""

from . import *  # noqa: F403


class AppRunnerRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['build.apprunner.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class AppRunnerRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [AppRunnerRoleAllowStatement0]


class AppRunnerRoleAllowStatement0_1(PolicyStatement):
    action = [
        'ecr:GetDownloadUrlForLayer',
        'ecr:BatchGetImage',
        'ecr:DescribeImages',
        'ecr:GetAuthorizationToken',
        'ecr:BatchCheckLayerAvailability',
    ]
    resource_arn = '*'


class AppRunnerRolePolicies0PolicyDocument(PolicyDocument):
    statement = [AppRunnerRoleAllowStatement0_1]


class AppRunnerRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = AppRunnerRolePolicies0PolicyDocument


class AppRunnerRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = AppRunnerRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AppRunnerRolePolicy]
