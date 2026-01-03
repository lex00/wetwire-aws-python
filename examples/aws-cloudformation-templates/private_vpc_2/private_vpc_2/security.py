"""Security resources: ECSRole, ECSTaskExecutionRole."""

from . import *  # noqa: F403


class ECSRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ECSRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSRoleAllowStatement0]


class ECSRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ec2:AttachNetworkInterface',
        'ec2:CreateNetworkInterface',
        'ec2:CreateNetworkInterfacePermission',
        'ec2:DeleteNetworkInterface',
        'ec2:DeleteNetworkInterfacePermission',
        'ec2:Describe*',
        'ec2:DetachNetworkInterface',
        'elasticloadbalancing:DeregisterInstancesFromLoadBalancer',
        'elasticloadbalancing:DeregisterTargets',
        'elasticloadbalancing:Describe*',
        'elasticloadbalancing:RegisterInstancesWithLoadBalancer',
        'elasticloadbalancing:RegisterTargets',
    ]
    resource_arn = '*'


class ECSRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSRoleAllowStatement0_1]


class ECSRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'ecs-service'
    policy_document = ECSRolePolicies0PolicyDocument


class ECSRole:
    resource: iam.Role
    assume_role_policy_document = ECSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSRolePolicy]


class ECSTaskExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs-tasks.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ECSTaskExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSTaskExecutionRoleAllowStatement0]


class ECSTaskExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecr:GetAuthorizationToken',
        'ecr:BatchCheckLayerAvailability',
        'ecr:GetDownloadUrlForLayer',
        'ecr:BatchGetImage',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = '*'


class ECSTaskExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSTaskExecutionRoleAllowStatement0_1]


class ECSTaskExecutionRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'AmazonECSTaskExecutionRolePolicy'
    policy_document = ECSTaskExecutionRolePolicies0PolicyDocument


class ECSTaskExecutionRole:
    resource: iam.Role
    assume_role_policy_document = ECSTaskExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSTaskExecutionRolePolicy]
