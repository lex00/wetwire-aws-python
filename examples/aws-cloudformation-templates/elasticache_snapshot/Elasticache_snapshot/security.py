"""Security resources: IamRoleLambda."""

from . import *  # noqa: F403


class IamRoleLambdaAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class IamRoleLambdaAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [IamRoleLambdaAllowStatement0]


class IamRoleLambdaAllowStatement0_1:
    resource: PolicyStatement
    action = ['elasticache:ModifyReplicationGroup']
    resource_arn = RedisReplicationGroup


class IamRoleLambdaPolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [IamRoleLambdaAllowStatement0_1]


class IamRoleLambdaPolicy:
    resource: iam.Role.Policy
    policy_name = 'ElastiCacheSnapshotPolicy'
    policy_document = IamRoleLambdaPolicies0PolicyDocument


class IamRoleLambda:
    resource: iam.Role
    assume_role_policy_document = IamRoleLambdaAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']
    policies = [IamRoleLambdaPolicy]
    condition = 'EnableBackups'
