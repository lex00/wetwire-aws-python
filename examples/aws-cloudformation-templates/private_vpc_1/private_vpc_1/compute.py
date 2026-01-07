"""Compute resources: ECSCluster, ContainerInstances, ECSAutoScalingGroup."""

from . import *  # noqa: F403


class ECSCluster(ecs.Cluster):
    resource: ecs.Cluster


class ContainerInstancesIamInstanceProfile(ec2.LaunchTemplate.IamInstanceProfile):
    arn = EC2InstanceProfile.Arn


class ContainerInstancesLaunchTemplateData(ec2.LaunchTemplate.LaunchTemplateData):
    image_id = ECSAMI
    security_group_ids = [EcsHostSecurityGroup]
    instance_type = InstanceType
    iam_instance_profile = ContainerInstancesIamInstanceProfile
    user_data = Base64(Sub("""#!/bin/bash -xe
echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource ECSAutoScalingGroup --region ${AWS::Region}
"""))


class ContainerInstances(ec2.LaunchTemplate):
    resource: ec2.LaunchTemplate
    launch_template_data = ContainerInstancesLaunchTemplateData


class ECSAutoScalingGroupLaunchTemplateSpecification(autoscaling.AutoScalingGroup.LaunchTemplateSpecification):
    launch_template_id = ContainerInstances
    version = ContainerInstances.LatestVersionNumber


class ECSAutoScalingGroup(autoscaling.AutoScalingGroup):
    resource: autoscaling.AutoScalingGroup
    vpc_zone_identifier = [PrivateSubnetOne, PrivateSubnetTwo]
    launch_template = ECSAutoScalingGroupLaunchTemplateSpecification
    min_size = 1
    max_size = MaxSize
    desired_capacity = DesiredCapacity
