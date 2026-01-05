"""Compute resources: TaskDefinition, Service."""

from . import *  # noqa: F403


class TaskDefinitionPortMapping:
    resource: ecs.TaskDefinition.PortMapping
    container_port = ContainerPort


class TaskDefinitionContainerDefinition:
    resource: ecs.TaskDefinition.ContainerDefinition
    name = ServiceName
    essential = True
    cpu = ContainerCpu
    memory = ContainerMemory
    image = ImageUrl
    port_mappings = [TaskDefinitionPortMapping]


class TaskDefinition(ecs.TaskDefinition):
    family = ServiceName
    cpu = ContainerCpu
    memory = ContainerMemory
    network_mode = ecs.NetworkMode.AWSVPC
    requires_compatibilities = ['FARGATE']
    execution_role_arn = ImportValue(Join(':', [
    StackName,
    'ECSTaskExecutionRole',
]))
    task_role_arn = If("HasCustomRole", Role, AWS_NO_VALUE)
    container_definitions = [TaskDefinitionContainerDefinition]


class ServiceDeploymentConfiguration:
    resource: ecs.Service.DeploymentConfiguration
    maximum_percent = 200
    minimum_healthy_percent = 75


class ServiceAwsVpcConfiguration:
    resource: ecs.Service.AwsVpcConfiguration
    security_groups = [ImportValue(Join(':', [
    StackName,
    'FargateContainerSecurityGroup',
]))]
    subnets = [ImportValue(Join(':', [
    StackName,
    'PrivateSubnetOne',
])), ImportValue(Join(':', [
    StackName,
    'PrivateSubnetTwo',
]))]


class ServiceNetworkConfiguration:
    resource: ecs.Service.NetworkConfiguration
    awsvpc_configuration = ServiceAwsVpcConfiguration


class ServiceLoadBalancer:
    resource: ecs.TaskSet.LoadBalancer
    container_name = ServiceName
    container_port = ContainerPort
    target_group_arn = TargetGroup


class Service(ecs.Service):
    service_name = ServiceName
    cluster = ImportValue(Join(':', [
    StackName,
    'ClusterName',
]))
    launch_type = ecs.LaunchType.FARGATE
    deployment_configuration = ServiceDeploymentConfiguration
    desired_count = DesiredCount
    network_configuration = ServiceNetworkConfiguration
    task_definition = TaskDefinition
    load_balancers = [ServiceLoadBalancer]
    depends_on = [LoadBalancerRule]
