"""Security resources: VPCFlowLogsRole."""

from . import *  # noqa: F403


class VPCFlowLogsRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['vpc-flow-logs.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class VPCFlowLogsRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [VPCFlowLogsRoleAllowStatement0]


class VPCFlowLogsRoleAllowStatement0_1(PolicyStatement):
    sid = 'CloudWatchLogs'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'logs:DescribeLogGroups',
        'logs:DescribeLogStreams',
    ]
    resource_arn = VPCFlowLogsLogGroup.Arn


class VPCFlowLogsRolePolicies0PolicyDocument(PolicyDocument):
    statement = [VPCFlowLogsRoleAllowStatement0_1]


class VPCFlowLogsRolePolicy(iam.User.Policy):
    policy_name = 'CloudWatchLogGroup'
    policy_document = VPCFlowLogsRolePolicies0PolicyDocument


class VPCFlowLogsRole(iam.Role):
    description = 'Rights to Publish VPC Flow Logs to CloudWatch Logs'
    assume_role_policy_document = VPCFlowLogsRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [VPCFlowLogsRolePolicy]
