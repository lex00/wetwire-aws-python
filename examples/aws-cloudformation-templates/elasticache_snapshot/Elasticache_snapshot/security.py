"""Security resources: IamRoleLambda."""

from . import *  # noqa: F403


class IamRoleLambdaAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class IamRoleLambdaAssumeRolePolicyDocument(PolicyDocument):
    statement = [IamRoleLambdaAllowStatement0]


class IamRoleLambdaAllowStatement0_1(PolicyStatement):
    action = ['elasticache:ModifyReplicationGroup']
    resource_arn = RedisReplicationGroup


class IamRoleLambdaPolicies0PolicyDocument(PolicyDocument):
    statement = [IamRoleLambdaAllowStatement0_1]


class IamRoleLambdaPolicy(iam.User.Policy):
    policy_name = 'ElastiCacheSnapshotPolicy'
    policy_document = IamRoleLambdaPolicies0PolicyDocument


class IamRoleLambda(iam.Role):
    assume_role_policy_document = IamRoleLambdaAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']
    policies = [IamRoleLambdaPolicy]
    condition = 'EnableBackups'
