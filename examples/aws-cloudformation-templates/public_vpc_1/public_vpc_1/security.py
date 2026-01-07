"""Security resources: EC2Role, EC2InstanceProfile, AutoscalingRole, ECSRole."""

from . import *  # noqa: F403


class EC2RoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class EC2RoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [EC2RoleAllowStatement0]


class EC2RoleAllowStatement0_1(PolicyStatement):
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


class EC2RolePolicies0PolicyDocument(PolicyDocument):
    statement = [EC2RoleAllowStatement0_1]


class EC2RolePolicy(iam.User.Policy):
    policy_name = 'ecs-service'
    policy_document = EC2RolePolicies0PolicyDocument


class EC2Role(iam.Role):
    resource: iam.Role
    assume_role_policy_document = EC2RoleAssumeRolePolicyDocument
    path = '/'
    policies = [EC2RolePolicy]


class EC2InstanceProfile(iam.InstanceProfile):
    resource: iam.InstanceProfile
    path = '/'
    roles = [EC2Role]


class AutoscalingRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['application-autoscaling.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class AutoscalingRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [AutoscalingRoleAllowStatement0]


class AutoscalingRoleAllowStatement0_1(PolicyStatement):
    action = [
        'application-autoscaling:*',
        'cloudwatch:DescribeAlarms',
        'cloudwatch:PutMetricAlarm',
        'ecs:DescribeServices',
        'ecs:UpdateService',
    ]
    resource_arn = '*'


class AutoscalingRolePolicies0PolicyDocument(PolicyDocument):
    statement = [AutoscalingRoleAllowStatement0_1]


class AutoscalingRolePolicy(iam.User.Policy):
    policy_name = 'service-autoscaling'
    policy_document = AutoscalingRolePolicies0PolicyDocument


class AutoscalingRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = AutoscalingRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AutoscalingRolePolicy]


class ECSRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ECSRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [ECSRoleAllowStatement0]


class ECSRoleAllowStatement0_1(PolicyStatement):
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


class ECSRolePolicies0PolicyDocument(PolicyDocument):
    statement = [ECSRoleAllowStatement0_1]


class ECSRolePolicy(iam.User.Policy):
    policy_name = 'ecs-service'
    policy_document = ECSRolePolicies0PolicyDocument


class ECSRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = ECSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSRolePolicy]
