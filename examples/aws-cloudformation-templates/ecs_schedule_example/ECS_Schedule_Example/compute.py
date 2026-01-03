"""Compute resources: ECSCluster, ContainerInstances, ECSAutoScalingGroup, Service."""

from . import *  # noqa: F403


class ECSCluster:
    resource: ecs.Cluster


class ContainerInstances:
    resource: autoscaling.LaunchConfiguration
    image_id = LatestAmiId
    security_groups = [EcsSecurityGroup]
    instance_type = InstanceType
    iam_instance_profile = EC2InstanceProfile
    key_name = KeyName
    user_data = Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
    --resource ECSAutoScalingGroup \
    --region ${AWS::Region}
"""))


class ECSAutoScalingGroup:
    resource: autoscaling.AutoScalingGroup
    vpc_zone_identifier = SubnetId
    launch_configuration_name = ContainerInstances
    min_size = '1'
    max_size = MaxSize
    desired_capacity = DesiredCapacity


class ServiceLoadBalancer:
    resource: ecs.TaskSet.LoadBalancer
    container_name = 'simple-app'
    container_port = '80'
    target_group_arn = ECSTG


class Service:
    resource: ecs.Service
    cluster = ECSCluster
    desired_count = '1'
    load_balancers = [ServiceLoadBalancer]
    role = ECSServiceRole
    task_definition = TaskDefinition
    depends_on = [ALBListener]
