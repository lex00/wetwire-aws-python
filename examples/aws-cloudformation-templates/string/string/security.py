"""Security resources: TransformExecutionRole."""

from . import *  # noqa: F403


class TransformExecutionRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class TransformExecutionRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [TransformExecutionRoleAllowStatement0]


class TransformExecutionRoleAllowStatement0_1(PolicyStatement):
    action = ['logs:*']
    resource_arn = 'arn:aws:logs:*:*:*'


class TransformExecutionRolePolicies0PolicyDocument(PolicyDocument):
    statement = [TransformExecutionRoleAllowStatement0_1]


class TransformExecutionRolePolicy(iam.User.Policy):
    policy_name = 'root'
    policy_document = TransformExecutionRolePolicies0PolicyDocument


class TransformExecutionRole(iam.Role):
    assume_role_policy_document = TransformExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [TransformExecutionRolePolicy]
