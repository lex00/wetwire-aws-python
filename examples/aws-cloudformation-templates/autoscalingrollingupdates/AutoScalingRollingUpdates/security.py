"""Security resources: DescribeHealthRole, WebServerInstanceProfile."""

from . import *  # noqa: F403


class DescribeHealthRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class DescribeHealthRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DescribeHealthRoleAllowStatement0]


class DescribeHealthRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['elasticloadbalancing:DescribeInstanceHealth']
    resource_arn = '*'


class DescribeHealthRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [DescribeHealthRoleAllowStatement0_1]


class DescribeHealthRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'describe-instance-health-policy'
    policy_document = DescribeHealthRolePolicies0PolicyDocument


class DescribeHealthRole:
    resource: iam.Role
    assume_role_policy_document = DescribeHealthRoleAssumeRolePolicyDocument
    path = '/'
    policies = [DescribeHealthRolePolicy]


class WebServerInstanceProfile:
    resource: iam.InstanceProfile
    path = '/'
    roles = [DescribeHealthRole]
