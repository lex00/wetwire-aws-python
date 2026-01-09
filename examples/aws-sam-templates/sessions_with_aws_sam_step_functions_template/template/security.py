"""Security resources: AnalyticsWorkflowRole."""

from . import *  # noqa: F403


class AnalyticsWorkflowRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': [Sub('states.${AWS::Region}.amazonaws.com')],
    }
    action = 'sts:AssumeRole'


class AnalyticsWorkflowRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [AnalyticsWorkflowRoleAllowStatement0]


class AnalyticsWorkflowRoleAllowStatement0_1(PolicyStatement):
    action = ['states:StartExecution']
    resource_arn = [
        GatherStackOverflowMetrics,
        GatherTwitchMetrics,
    ]


class AnalyticsWorkflowRoleAllowStatement1(PolicyStatement):
    action = [
        'states:DescribeExecution',
        'states:StopExecution',
    ]
    resource_arn = [
        GatherStackOverflowMetrics,
        GatherTwitchMetrics,
    ]


class AnalyticsWorkflowRoleAllowStatement2(PolicyStatement):
    action = [
        'events:PutTargets',
        'events:PutRule',
        'events:DescribeRule',
    ]
    resource_arn = [Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule')]


class AnalyticsWorkflowRoleAllowStatement3(PolicyStatement):
    action = ['sns:Publish']
    resource_arn = [AnalyticsTopic]


class AnalyticsWorkflowRolePolicies0PolicyDocument(PolicyDocument):
    statement = [AnalyticsWorkflowRoleAllowStatement0_1, AnalyticsWorkflowRoleAllowStatement1, AnalyticsWorkflowRoleAllowStatement2, AnalyticsWorkflowRoleAllowStatement3]


class AnalyticsWorkflowRolePolicy(iam.User.Policy):
    policy_name = 'ParentWorkflowExecutionPolicy'
    policy_document = AnalyticsWorkflowRolePolicies0PolicyDocument


class AnalyticsWorkflowRole(iam.Role):
    assume_role_policy_document = AnalyticsWorkflowRoleAssumeRolePolicyDocument
    policies = [AnalyticsWorkflowRolePolicy]
