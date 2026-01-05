"""Security resources: ASCPrivateLinkLambdaRole."""

from . import *  # noqa: F403


class ASCPrivateLinkLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ASCPrivateLinkLambdaRoleAllowStatement0]


class ASCPrivateLinkLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'ec2:DescribeVpcEndpointServiceConfigurations',
        'ec2:ModifyVpcEndpointServiceConfiguration',
        'route53:ChangeResourceRecordSets',
    ]
    resource_arn = '*'


class ASCPrivateLinkLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ASCPrivateLinkLambdaRoleAllowStatement0_1]


class ASCPrivateLinkLambdaRolePolicy:
    resource: iam.User.Policy
    policy_name = 'ASCPrivateLinkLambdaPolicy'
    policy_document = ASCPrivateLinkLambdaRolePolicies0PolicyDocument


class ASCPrivateLinkLambdaRole(iam.Role):
    assume_role_policy_document = ASCPrivateLinkLambdaRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ASCPrivateLinkLambdaRolePolicy]
