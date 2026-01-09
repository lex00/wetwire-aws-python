"""Security resources: DDBRole."""

from . import *  # noqa: F403


class DDBRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['appsync.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class DDBRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [DDBRoleAllowStatement0]


class DDBRoleAllowStatement0_1(PolicyStatement):
    action = [
        'dynamodb:GetItem',
        'dynamodb:PutItem',
        'dynamodb:DeleteItem',
        'dynamodb:UpdateItem',
        'dynamodb:Query',
        'dynamodb:Scan',
    ]
    resource_arn = DDBTable.Arn


class DDBRolePolicies0PolicyDocument(PolicyDocument):
    statement = [DDBRoleAllowStatement0_1]


class DDBRolePolicy(iam.User.Policy):
    policy_name = 'DDBAccess'
    policy_document = DDBRolePolicies0PolicyDocument


class DDBRole(iam.Role):
    assume_role_policy_document = DDBRoleAssumeRolePolicyDocument
    policies = [DDBRolePolicy]
