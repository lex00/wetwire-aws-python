"""Security resources: LambdaRole, StateMachineRole."""

from . import *  # noqa: F403


class LambdaRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class LambdaRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [LambdaRoleAllowStatement0]


class LambdaRoleAllowStatement0_1(PolicyStatement):
    action = ['glue:*']
    resource_arn = [Sub('arn:aws:glue:${AWS::Region}:${AWS::AccountId}:job/${pGlueJobName}')]


class LambdaRolePolicies0PolicyDocument(PolicyDocument):
    statement = [LambdaRoleAllowStatement0_1]


class LambdaRolePolicy(iam.User.Policy):
    policy_name = 'glue'
    policy_document = LambdaRolePolicies0PolicyDocument


class LambdaRole(iam.Role):
    assume_role_policy_document = LambdaRoleAssumeRolePolicyDocument
    path = '/service-role/'
    policies = [LambdaRolePolicy]


class StateMachineRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['states.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class StateMachineRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [StateMachineRoleAllowStatement0]


class StateMachineRoleAllowStatement0_1(PolicyStatement):
    action = ['glue:*']
    resource_arn = [Sub('arn:aws:glue:${AWS::Region}:${AWS::AccountId}:job/${pGlueJobName}')]


class StateMachineRolePolicies0PolicyDocument(PolicyDocument):
    statement = [StateMachineRoleAllowStatement0_1]


class StateMachineRolePolicy(iam.User.Policy):
    policy_name = 'glue'
    policy_document = StateMachineRolePolicies0PolicyDocument


class StateMachineRoleAllowStatement0_2(PolicyStatement):
    action = ['lambda:InvokeFunction']
    resource_arn = [
        FnCheck.Arn,
        FnSuccess.Arn,
        FnFailure.Arn,
    ]


class StateMachineRolePolicies1PolicyDocument(PolicyDocument):
    statement = [StateMachineRoleAllowStatement0_2]


class StateMachineRolePolicy1(iam.User.Policy):
    policy_name = 'lambda'
    policy_document = StateMachineRolePolicies1PolicyDocument


class StateMachineRole(iam.Role):
    assume_role_policy_document = StateMachineRoleAssumeRolePolicyDocument
    path = '/service-role/'
    policies = [StateMachineRolePolicy, StateMachineRolePolicy1]
