"""Security resources: DescribeHealthRole, WebServerInstanceProfile."""

from . import *  # noqa: F403


class DescribeHealthRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class DescribeHealthRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [DescribeHealthRoleAllowStatement0]


class DescribeHealthRoleAllowStatement0_1(PolicyStatement):
    action = ['elasticloadbalancing:DescribeInstanceHealth']
    resource_arn = '*'


class DescribeHealthRolePolicies0PolicyDocument(PolicyDocument):
    statement = [DescribeHealthRoleAllowStatement0_1]


class DescribeHealthRolePolicy(iam.User.Policy):
    policy_name = 'describe-instance-health-policy'
    policy_document = DescribeHealthRolePolicies0PolicyDocument


class DescribeHealthRole(iam.Role):
    assume_role_policy_document = DescribeHealthRoleAssumeRolePolicyDocument
    path = '/'
    policies = [DescribeHealthRolePolicy]


class WebServerInstanceProfile(iam.InstanceProfile):
    path = '/'
    roles = [DescribeHealthRole]
