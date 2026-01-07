"""Compute resources: TaskDefinition, Service."""

from . import *  # noqa: F403


class TaskDefinitionPortMapping(ecs.TaskDefinition.PortMapping):
    container_port = ContainerPort


class TaskDefinitionContainerDefinition(ecs.TaskDefinition.ContainerDefinition):
    name = ServiceName
    essential = True
    cpu = ContainerCpu
    memory = ContainerMemory
    image = ImageUrl
    port_mappings = [TaskDefinitionPortMapping]


class TaskDefinition(ecs.TaskDefinition):
    resource: ecs.TaskDefinition
    family = ServiceName
    cpu = ContainerCpu
    memory = ContainerMemory
    task_role_arn = If("HasCustomRole", Role, AWS_NO_VALUE)
    container_definitions = [TaskDefinitionContainerDefinition]


class ServiceDeploymentConfiguration(ecs.Service.DeploymentConfiguration):
    maximum_percent = 200
    minimum_healthy_percent = 75


class ServiceLoadBalancer(ecs.TaskSet.LoadBalancer):
    container_name = ServiceName
    container_port = ContainerPort
    target_group_arn = TargetGroup


class Service(ecs.Service):
    resource: ecs.Service
    service_name = ServiceName
    cluster = ImportValue(Join(':', [
    StackName,
    'ClusterName',
]))
    deployment_configuration = ServiceDeploymentConfiguration
    desired_count = DesiredCount
    task_definition = TaskDefinition
    load_balancers = [ServiceLoadBalancer]
    depends_on = [LoadBalancerRule]
