"""Stack resources."""

from . import *  # noqa: F403


class TaskDefinitionLogConfiguration:
    resource: ecs.TaskDefinition.LogConfiguration
    log_driver = 'awslogs'
    options = {
        'awslogs-group': CloudwatchLogsGroup,
        'awslogs-region': AWS_REGION,
        'awslogs-stream-prefix': 'ecs-demo-app',
    }


class TaskDefinitionMountPoint:
    resource: ecs.TaskDefinition.MountPoint
    container_path = '/usr/local/apache2/htdocs'
    source_volume = 'my-vol'


class TaskDefinitionPortMapping:
    resource: ecs.TaskDefinition.PortMapping
    container_port = 80


class TaskDefinitionContainerDefinition:
    resource: ecs.TaskDefinition.ContainerDefinition
    name = 'simple-app'
    cpu = '10'
    essential = 'true'
    image = 'httpd:2.4'
    memory = '300'
    log_configuration = TaskDefinitionLogConfiguration
    mount_points = [TaskDefinitionMountPoint]
    port_mappings = [TaskDefinitionPortMapping]


class TaskDefinitionLogConfiguration1:
    resource: ecs.TaskDefinition.LogConfiguration
    log_driver = 'awslogs'
    options = {
        'awslogs-group': CloudwatchLogsGroup,
        'awslogs-region': AWS_REGION,
        'awslogs-stream-prefix': 'ecs-demo-app',
    }


class TaskDefinitionVolumeFrom:
    resource: ecs.TaskDefinition.VolumeFrom
    source_container = 'simple-app'


class TaskDefinitionContainerDefinition1:
    resource: ecs.TaskDefinition.ContainerDefinition
    name = 'busybox'
    cpu = 10
    command = ['/bin/sh -c "while true; do echo \'<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p>\' > top; /bin/date > date ; echo \'</div></body></html>\' > bottom; cat top date bottom > /usr/local/apache2/htdocs/index.html ; sleep 1; done"']
    entry_point = ['sh', '-c']
    essential = False
    image = 'busybox'
    memory = 200
    log_configuration = TaskDefinitionLogConfiguration1
    volumes_from = [TaskDefinitionVolumeFrom]


class TaskDefinitionSecret:
    resource: ecs.Service.Secret
    name = 'my-vol'


class TaskDefinition:
    resource: ecs.TaskDefinition
    family = Join('', [
    AWS_STACK_NAME,
    '-ecs-demo-app',
])
    container_definitions = [TaskDefinitionContainerDefinition, TaskDefinitionContainerDefinition1]
    volumes = [TaskDefinitionSecret]


class ServiceScalingTarget:
    resource: applicationautoscaling.ScalableTarget
    max_capacity = 2
    min_capacity = 1
    resource_id = Join('', [
    'service/',
    ECSCluster,
    '/',
    Service.Name,
])
    role_arn = AutoscalingRole.Arn
    scalable_dimension = 'ecs:service:DesiredCount'
    service_namespace = 'ecs'
    depends_on = [Service]


class ServiceScalingPolicyStepAdjustment:
    resource: applicationautoscaling.ScalingPolicy.StepAdjustment
    metric_interval_lower_bound = 0
    scaling_adjustment = 200


class ServiceScalingPolicyStepScalingPolicyConfiguration:
    resource: applicationautoscaling.ScalingPolicy.StepScalingPolicyConfiguration
    adjustment_type = 'PercentChangeInCapacity'
    cooldown = 60
    metric_aggregation_type = 'Average'
    step_adjustments = [ServiceScalingPolicyStepAdjustment]


class ServiceScalingPolicy:
    resource: applicationautoscaling.ScalingPolicy
    policy_name = 'AStepPolicy'
    policy_type = 'StepScaling'
    scaling_target_id = ServiceScalingTarget
    step_scaling_policy_configuration = ServiceScalingPolicyStepScalingPolicyConfiguration
