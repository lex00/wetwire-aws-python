"""Security resources: EC2Role, EC2InstanceProfile, AutoscalingRole, LogsKmsKey, ECSServiceRole, ECSEventRole."""

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


class LogsKmsKey(kms.Key):
    resource: kms.Key
    description = 'ECS Logs Encryption Key'
    enable_key_rotation = True


class ECSServiceRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ECSServiceRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [ECSServiceRoleAllowStatement0]


class ECSServiceRoleAllowStatement0_1(PolicyStatement):
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


class ECSServiceRolePolicies0PolicyDocument(PolicyDocument):
    statement = [ECSServiceRoleAllowStatement0_1]


class ECSServiceRolePolicy(iam.User.Policy):
    policy_name = 'ecs-service'
    policy_document = ECSServiceRolePolicies0PolicyDocument


class ECSServiceRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = ECSServiceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSServiceRolePolicy]


class ECSEventRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class ECSEventRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [ECSEventRoleAllowStatement0]


class ECSEventRoleAllowStatement0_1(PolicyStatement):
    action = ['ecs:RunTask']
    resource_arn = '*'


class ECSEventRolePolicies0PolicyDocument(PolicyDocument):
    statement = [ECSEventRoleAllowStatement0_1]


class ECSEventRolePolicy(iam.User.Policy):
    policy_name = 'ecs-service'
    policy_document = ECSEventRolePolicies0PolicyDocument


class ECSEventRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = ECSEventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSEventRolePolicy]
