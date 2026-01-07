"""Security resources: InstanceRole, InstanceRolePolicy, InstanceProfile."""

from . import *  # noqa: F403


class InstanceRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'ec2.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class InstanceRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [InstanceRoleAllowStatement0]


class InstanceRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = InstanceRoleAssumeRolePolicyDocument
    tags = [{
        'Key': 'Name',
        'Value': 'gitlab-server-instance',
    }]


class InstanceRolePolicyAllowStatement0(PolicyStatement):
    action = [
        'ec2messages:*',
        'ssm:UpdateInstanceInformation',
        'ssmmessages:*',
        'secretsmanager:GetSecretValue',
    ]
    resource_arn = '*'


class InstanceRolePolicyPolicyDocument(PolicyDocument):
    statement = [InstanceRolePolicyAllowStatement0]


class InstanceRolePolicy(iam.RolePolicy):
    resource: iam.RolePolicy
    policy_document = InstanceRolePolicyPolicyDocument
    policy_name = 'InstanceRolePolicy'
    role_name = InstanceRole


class InstanceProfile(iam.InstanceProfile):
    resource: iam.InstanceProfile
    roles = [InstanceRole]
