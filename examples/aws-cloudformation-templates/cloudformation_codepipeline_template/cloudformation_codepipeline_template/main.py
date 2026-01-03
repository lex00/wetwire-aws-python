"""Stack resources."""

from . import *  # noqa: F403


class EventRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class EventRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EventRoleAllowStatement0]


class EventRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'codepipeline:StartPipelineExecution'
    resource_arn = Join('', [
    'arn:aws:codepipeline:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    Pipeline,
])


class EventRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [EventRoleAllowStatement0_1]


class EventRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'eb-pipeline-execution'
    policy_document = EventRolePolicies0PolicyDocument


class EventRole:
    resource: iam.Role
    assume_role_policy_document = EventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [EventRolePolicy]
