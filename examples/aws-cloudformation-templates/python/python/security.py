"""Security resources: TransformExecutionRole."""

from . import *  # noqa: F403


class TransformExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class TransformExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TransformExecutionRoleAllowStatement0]


class TransformExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['logs:*']
    resource_arn = 'arn:aws:logs:*:*:*'


class TransformExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [TransformExecutionRoleAllowStatement0_1]


class TransformExecutionRolePolicy:
    resource: iam.User.Policy
    policy_name = 'root'
    policy_document = TransformExecutionRolePolicies0PolicyDocument


class TransformExecutionRole:
    resource: iam.Role
    assume_role_policy_document = TransformExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [TransformExecutionRolePolicy]
    managed_policy_arns = [If("AdditionalPolicyProvided", AdditionalExecutionPolicy, AWS_NO_VALUE)]
