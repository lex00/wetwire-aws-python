"""Security resources: EventBridgeRole, EventBridgeRolePolicy."""

from . import *  # noqa: F403


class EventBridgeRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'events.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class EventBridgeRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [EventBridgeRoleAllowStatement0]


class EventBridgeRole(iam.Role):
    assume_role_policy_document = EventBridgeRoleAssumeRolePolicyDocument


class EventBridgeRolePolicyAllowStatement0(PolicyStatement):
    action = 'events:PutEvents'
    resource_arn = CentralEventBusArn


class EventBridgeRolePolicyPolicyDocument(PolicyDocument):
    statement = [EventBridgeRolePolicyAllowStatement0]


class EventBridgeRolePolicy(iam.RolePolicy):
    policy_name = 'EventBridgeRolePolicy'
    policy_document = EventBridgeRolePolicyPolicyDocument
    role_name = EventBridgeRole
