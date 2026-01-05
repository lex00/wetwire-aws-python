"""Security resources: AWSCloudFormationStackSetAdministrationRole."""

from . import *  # noqa: F403


class AWSCloudFormationStackSetAdministrationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'cloudformation.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AWSCloudFormationStackSetAdministrationRoleAllowStatement0]


class AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'sts:AssumeRole'
    resource_arn = 'arn:aws:iam::*:role/AWSCloudFormationStackSetExecutionRole'


class AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1]


class AWSCloudFormationStackSetAdministrationRolePolicy:
    resource: iam.User.Policy
    policy_name = 'AssumeRole-AWSCloudFormationStackSetExecutionRole'
    policy_document = AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument


class AWSCloudFormationStackSetAdministrationRole:
    resource: iam.Role
    role_name = 'AWSCloudFormationStackSetAdministrationRole'
    assume_role_policy_document = AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument
    policies = [AWSCloudFormationStackSetAdministrationRolePolicy]
