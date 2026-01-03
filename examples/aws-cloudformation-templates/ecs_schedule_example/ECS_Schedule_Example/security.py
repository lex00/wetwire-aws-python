"""Security resources: ECSServiceRole, EC2Role, EC2InstanceProfile, LogsKmsKey, ECSEventRole, AutoscalingRole."""

from . import *  # noqa: F403


class ECSServiceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ECSServiceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSServiceRoleAllowStatement0]


class ECSServiceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'elasticloadbalancing:DeregisterInstancesFromLoadBalancer',
        'elasticloadbalancing:DeregisterTargets',
        'elasticloadbalancing:Describe*',
        'elasticloadbalancing:RegisterInstancesWithLoadBalancer',
        'elasticloadbalancing:RegisterTargets',
        'ec2:Describe*',
        'ec2:AuthorizeSecurityGroupIngress',
    ]
    resource_arn = '*'


class ECSServiceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSServiceRoleAllowStatement0_1]


class ECSServiceRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'ecs-service'
    policy_document = ECSServiceRolePolicies0PolicyDocument


class ECSServiceRole:
    resource: iam.Role
    assume_role_policy_document = ECSServiceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSServiceRolePolicy]


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


class LogsKmsKey:
    resource: kms.Key
    description = 'ECS Logs Encryption Key'
    enable_key_rotation = True


class ECSEventRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ECSEventRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSEventRoleAllowStatement0]


class ECSEventRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['ecs:RunTask']
    resource_arn = '*'


class ECSEventRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSEventRoleAllowStatement0_1]


class ECSEventRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'ecs-service'
    policy_document = ECSEventRolePolicies0PolicyDocument


class ECSEventRole:
    resource: iam.Role
    assume_role_policy_document = ECSEventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSEventRolePolicy]


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
