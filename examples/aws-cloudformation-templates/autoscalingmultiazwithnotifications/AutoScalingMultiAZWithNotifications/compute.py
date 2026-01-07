"""Compute resources: LaunchTemplate, WebServerGroup, WebServerScaleUpPolicy, WebServerScaleDownPolicy."""

from . import *  # noqa: F403


class LaunchTemplateEbs(ec2.LaunchTemplate.Ebs):
    volume_size = 32


class LaunchTemplateBlockDeviceMapping(ec2.LaunchTemplate.BlockDeviceMapping):
    device_name = '/dev/sda1'
    ebs = LaunchTemplateEbs


class LaunchTemplateTagSpecification(ec2.LaunchTemplate.TagSpecification):
    resource_type = 'instance'
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-Instance'),
    }]


class LaunchTemplateLaunchTemplateData(ec2.LaunchTemplate.LaunchTemplateData):
    image_id = LatestAmiId
    instance_type = InstanceType
    security_group_ids = SecurityGroups
    key_name = KeyName
    block_device_mappings = [LaunchTemplateBlockDeviceMapping]
    user_data = Base64(Sub("""#!/bin/bash
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
"""))
    tag_specifications = [LaunchTemplateTagSpecification]


class LaunchTemplate(ec2.LaunchTemplate):
    resource: ec2.LaunchTemplate
    launch_template_name = Sub('${AWS::StackName}-LaunchTemplate')
    launch_template_data = LaunchTemplateLaunchTemplateData


class WebServerGroupLaunchTemplateSpecification(autoscaling.AutoScalingGroup.LaunchTemplateSpecification):
    launch_template_id = LaunchTemplate
    version = LaunchTemplate.LatestVersionNumber


class WebServerGroupNotificationConfiguration(autoscaling.AutoScalingGroup.NotificationConfiguration):
    topic_arn = NotificationTopic
    notification_types = ['autoscaling:EC2_INSTANCE_LAUNCH', 'autoscaling:EC2_INSTANCE_LAUNCH_ERROR', 'autoscaling:EC2_INSTANCE_TERMINATE', 'autoscaling:EC2_INSTANCE_TERMINATE_ERROR']


class WebServerGroup(autoscaling.AutoScalingGroup):
    resource: autoscaling.AutoScalingGroup
    availability_zones = AZs
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = '1'
    max_size = '3'
    target_group_ar_ns = [TargetGroup]
    notification_configurations = [WebServerGroupNotificationConfiguration]
    health_check_type = 'ELB'
    vpc_zone_identifier = Subnets


class WebServerScaleUpPolicy(autoscaling.ScalingPolicy):
    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = WebServerGroup
    cooldown = '60'
    scaling_adjustment = 1


class WebServerScaleDownPolicy(autoscaling.ScalingPolicy):
    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = WebServerGroup
    cooldown = '60'
    scaling_adjustment = -1
