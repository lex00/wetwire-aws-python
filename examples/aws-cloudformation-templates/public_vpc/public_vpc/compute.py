"""Compute resources: ECSCluster, ContainerInstances, ECSAutoScalingGroup."""

from . import *  # noqa: F403


class ECSCluster(ecs.Cluster):
    resource: ecs.Cluster


class ContainerInstances(autoscaling.LaunchConfiguration):
    resource: autoscaling.LaunchConfiguration
    image_id = ECSAMI
    security_groups = [EcsHostSecurityGroup]
    instance_type = InstanceType
    iam_instance_profile = EC2InstanceProfile
    user_data = Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource ECSAutoScalingGroup --region ${AWS::Region}
"""))


class ECSAutoScalingGroup(autoscaling.AutoScalingGroup):
    resource: autoscaling.AutoScalingGroup
    vpc_zone_identifier = [PublicSubnetOne, PublicSubnetTwo]
    launch_configuration_name = ContainerInstances
    min_size = '1'
    max_size = MaxSize
    desired_capacity = DesiredCapacity
