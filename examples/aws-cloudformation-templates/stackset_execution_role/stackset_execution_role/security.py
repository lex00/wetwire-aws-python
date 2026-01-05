"""Security resources: AWSCloudFormationStackSetExecutionRole."""

from . import *  # noqa: F403


class AWSCloudFormationStackSetExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'AWS': Sub('arn:aws:iam::${AdministrationAccountId}:role/AWSCloudFormationStackSetAdministrationRole'),
    }
    action = 'sts:AssumeRole'


class AWSCloudFormationStackSetExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AWSCloudFormationStackSetExecutionRoleAllowStatement0]


class AWSCloudFormationStackSetExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'cloudformation:CreateStack',
        'cloudformation:UpdateStack',
        'cloudformation:DeleteStack',
        'cloudformation:DescribeStacks',
        'cloudformation:DescribeStackEvents',
        'cloudformation:DescribeStackResources',
        'cloudformation:GetTemplate',
        'cloudformation:ValidateTemplate',
    ]
    resource_arn = '*'


class AWSCloudFormationStackSetExecutionRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        'cloudwatch:PutDashboard',
        'cloudwatch:DeleteDashboards',
        'cloudwatch:PutMetricAlarm',
        'cloudwatch:DeleteAlarms',
        'cloudwatch:DescribeAlarms',
    ]
    resource_arn = '*'


class AWSCloudFormationStackSetExecutionRoleAllowStatement2:
    resource: PolicyStatement
    action = [
        'sns:CreateTopic',
        'sns:DeleteTopic',
        'sns:Subscribe',
        'sns:Unsubscribe',
        'sns:SetTopicAttributes',
        'sns:GetTopicAttributes',
        'sns:ListSubscriptionsByTopic',
    ]
    resource_arn = '*'


class AWSCloudFormationStackSetExecutionRoleAllowStatement3:
    resource: PolicyStatement
    action = [
        'kms:Decrypt',
        'kms:DescribeKey',
    ]
    resource_arn = '*'


class AWSCloudFormationStackSetExecutionRoleAllowStatement4:
    resource: PolicyStatement
    action = [
        'ssm:GetParameter',
        'ssm:GetParameters',
        'ssm:GetParametersByPath',
    ]
    resource_arn = ['arn:aws:ssm:*:*:parameter/cdk-bootstrap/*']


class AWSCloudFormationStackSetExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AWSCloudFormationStackSetExecutionRoleAllowStatement0_1, AWSCloudFormationStackSetExecutionRoleAllowStatement1, AWSCloudFormationStackSetExecutionRoleAllowStatement2, AWSCloudFormationStackSetExecutionRoleAllowStatement3, AWSCloudFormationStackSetExecutionRoleAllowStatement4]


class AWSCloudFormationStackSetExecutionRolePolicy:
    resource: iam.User.Policy
    policy_name = 'ExecutionRolePolicy'
    policy_document = AWSCloudFormationStackSetExecutionRolePolicies0PolicyDocument


class AWSCloudFormationStackSetExecutionRole:
    resource: iam.Role
    role_name = 'AWSCloudFormationStackSetExecutionRole'
    assume_role_policy_document = AWSCloudFormationStackSetExecutionRoleAssumeRolePolicyDocument
    policies = [AWSCloudFormationStackSetExecutionRolePolicy]
