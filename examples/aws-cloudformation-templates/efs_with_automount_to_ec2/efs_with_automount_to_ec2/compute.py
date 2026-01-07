"""Compute resources: LaunchConfig, AutoScalingGroup, ScaleDownPolicy, ScaleUpPolicy."""

from . import *  # noqa: F403


class LaunchConfig(autoscaling.LaunchConfiguration):
    resource: autoscaling.LaunchConfiguration
    iam_instance_profile = InstanceProfile
    image_id = FindInMap("EC2RegionMap", AWS_REGION, '64')
    instance_type = InstanceType
    key_name = KeyName
    security_groups = [InstanceSecurityGroup.GroupId]
    user_data = Base64(Sub(""""#!/bin/bash -x\n",
"export LC_CTYPE=en_US.UTF-8\n",
"export LC_ALL=en_US.UTF-8\n",
"apt-get update\n",
"apt-get install -y curl nfs-common\n",
"EC2_REGION=${AWS::Region}\n",
"DIR_TGT=/mnt/efs/\n",
"EFS_FILE_SYSTEM_ID=${EFSFileSystem}\n"
"mkdir -p $DIR_TGT\n",
"DIR_SRC=$EFS_FILE_SYSTEM_ID.efs.$EC2_REGION.amazonaws.com\n",
"mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 $DIR_SRC:/ $DIR_TGT\n""""))


class AutoScalingGroup(autoscaling.AutoScalingGroup):
    resource: autoscaling.AutoScalingGroup
    launch_configuration_name = LaunchConfig
    load_balancer_names = [ElasticLoadBalancer]
    max_size = '3'
    min_size = '1'
    vpc_zone_identifier = Subnets


class ScaleDownPolicy(autoscaling.ScalingPolicy):
    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = AutoScalingGroup
    cooldown = '60'
    scaling_adjustment = '-1'


class ScaleUpPolicy(autoscaling.ScalingPolicy):
    resource: autoscaling.ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = AutoScalingGroup
    cooldown = '60'
    scaling_adjustment = '1'
