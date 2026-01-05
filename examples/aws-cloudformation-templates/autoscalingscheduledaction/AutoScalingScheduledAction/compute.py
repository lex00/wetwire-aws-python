"""Compute resources: LaunchConfig, WebServerGroup, ScheduledActionUp, ScheduledActionDown."""

from . import *  # noqa: F403


class LaunchConfig(autoscaling.LaunchConfiguration):
    key_name = KeyName
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", InstanceType, 'Arch'))
    security_groups = [InstanceSecurityGroup]
    instance_type = InstanceType
    user_data = Base64(Join('', [
    '#!/bin/bash -xe ',
    'yum update -y aws-cfn-bootstrap ',
    '/opt/aws/bin/cfn-init -v ',
    '         --stack ',
    AWS_STACK_NAME,
    '         --resource LaunchConfig ',
    '         --region ',
    AWS_REGION,
    ' ',
    '/opt/aws/bin/cfn-signal -e $? ',
    '         --stack ',
    AWS_STACK_NAME,
    '         --resource WebServerGroup ',
    '         --region ',
    AWS_REGION,
    ' ',
]))


class WebServerGroup(autoscaling.AutoScalingGroup):
    availability_zones = GetAZs()
    launch_configuration_name = LaunchConfig
    min_size = 2
    max_size = 5
    load_balancer_names = [ElasticLoadBalancer]


class ScheduledActionUp(autoscaling.ScheduledAction):
    auto_scaling_group_name = WebServerGroup
    max_size = '10'
    min_size = '5'
    recurrence = '0 7 * * *'


class ScheduledActionDown(autoscaling.ScheduledAction):
    auto_scaling_group_name = WebServerGroup
    max_size = '1'
    min_size = '1'
    recurrence = '0 19 * * *'
