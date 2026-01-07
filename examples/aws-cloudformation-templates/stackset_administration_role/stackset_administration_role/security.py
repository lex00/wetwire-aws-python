"""Security resources: AWSCloudFormationStackSetAdministrationRole."""

from . import *  # noqa: F403


class AWSCloudFormationStackSetAdministrationRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'cloudformation.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [AWSCloudFormationStackSetAdministrationRoleAllowStatement0]


class AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1(PolicyStatement):
    action = 'sts:AssumeRole'
    resource_arn = 'arn:aws:iam::*:role/AWSCloudFormationStackSetExecutionRole'


class AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument(PolicyDocument):
    statement = [AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1]


class AWSCloudFormationStackSetAdministrationRolePolicy(iam.User.Policy):
    policy_name = 'AssumeRole-AWSCloudFormationStackSetExecutionRole'
    policy_document = AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument


class AWSCloudFormationStackSetAdministrationRole(iam.Role):
    resource: iam.Role
    role_name = 'AWSCloudFormationStackSetAdministrationRole'
    assume_role_policy_document = AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument
    policies = [AWSCloudFormationStackSetAdministrationRolePolicy]
