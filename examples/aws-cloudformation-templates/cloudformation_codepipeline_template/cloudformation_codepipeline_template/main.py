"""Stack resources."""

from . import *  # noqa: F403


class EventRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class EventRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [EventRoleAllowStatement0]


class EventRoleAllowStatement0_1(PolicyStatement):
    action = 'codepipeline:StartPipelineExecution'
    resource_arn = Join('', [
    'arn:aws:codepipeline:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    Pipeline,
])


class EventRolePolicies0PolicyDocument(PolicyDocument):
    statement = [EventRoleAllowStatement0_1]


class EventRolePolicy(iam.User.Policy):
    policy_name = 'eb-pipeline-execution'
    policy_document = EventRolePolicies0PolicyDocument


class EventRole(iam.Role):
    assume_role_policy_document = EventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [EventRolePolicy]
