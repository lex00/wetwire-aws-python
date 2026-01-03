"""Security resources: EventBridgeRole, EventBridgeRolePolicy."""

from . import *  # noqa: F403


class EventBridgeRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'events.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class EventBridgeRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EventBridgeRoleAllowStatement0]


class EventBridgeRole:
    resource: iam.Role
    assume_role_policy_document = EventBridgeRoleAssumeRolePolicyDocument


class EventBridgeRolePolicyAllowStatement0:
    resource: PolicyStatement
    action = 'events:PutEvents'
    resource_arn = CentralEventBusArn


class EventBridgeRolePolicyPolicyDocument:
    resource: PolicyDocument
    statement = [EventBridgeRolePolicyAllowStatement0]


class EventBridgeRolePolicy:
    resource: iam.RolePolicy
    policy_name = 'EventBridgeRolePolicy'
    policy_document = EventBridgeRolePolicyPolicyDocument
    role_name = EventBridgeRole
