"""Security resources: EC2Role, EC2InstanceProfile, ECSRole, AutoscalingRole."""

from . import *  # noqa: F403


class EC2RoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class EC2RoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0]


class EC2RoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecs:CreateCluster',
        'ecs:DeregisterContainerInstance',
        'ecs:DiscoverPollEndpoint',
        'ecs:Poll',
        'ecs:RegisterContainerInstance',
        'ecs:StartTelemetrySession',
        'ecs:Submit*',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'ecr:GetAuthorizationToken',
        'ecr:BatchGetImage',
        'ecr:GetDownloadUrlForLayer',
    ]
    resource_arn = '*'


class EC2RolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0_1]


class EC2RolePolicy:
    resource: iam.Role.Policy
    policy_name = 'ecs-service'
    policy_document = EC2RolePolicies0PolicyDocument


class EC2Role:
    resource: iam.Role
    assume_role_policy_document = EC2RoleAssumeRolePolicyDocument
    path = '/'
    policies = [EC2RolePolicy]


class EC2InstanceProfile:
    resource: iam.InstanceProfile
    path = '/'
    roles = [EC2Role]


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


class AutoscalingRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['application-autoscaling.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class AutoscalingRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0]


class AutoscalingRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'application-autoscaling:*',
        'cloudwatch:DescribeAlarms',
        'cloudwatch:PutMetricAlarm',
        'ecs:DescribeServices',
        'ecs:UpdateService',
    ]
    resource_arn = '*'


class AutoscalingRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0_1]


class AutoscalingRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'service-autoscaling'
    policy_document = AutoscalingRolePolicies0PolicyDocument


class AutoscalingRole:
    resource: iam.Role
    assume_role_policy_document = AutoscalingRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AutoscalingRolePolicy]
