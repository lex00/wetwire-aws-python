"""Compute resources: LaunchTemplate, WebServerGroup, ScheduledActionDown, ScheduledActionUp."""

from . import *  # noqa: F403


class LaunchTemplateSpotFleetLaunchSpecification:
    resource: ec2.SpotFleet.SpotFleetLaunchSpecification
    key_name = KeyName
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", InstanceType, 'Arch'))
    security_groups = [InstanceSecurityGroup]
    instance_type = InstanceType
    user_data = Base64(Sub("""#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource LaunchTemplate  --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerGroup --region ${AWS::Region}
"""))


class LaunchTemplate:
    resource: ec2.LaunchTemplate
    launch_template_data = LaunchTemplateSpotFleetLaunchSpecification


class WebServerGroupLaunchTemplateSpecification:
    resource: autoscaling.AutoScalingGroup.LaunchTemplateSpecification
    launch_template_id = LaunchTemplate
    version = LaunchTemplate.LatestVersionNumber


class WebServerGroup:
    resource: autoscaling.AutoScalingGroup
    availability_zones = GetAZs()
    launch_template = WebServerGroupLaunchTemplateSpecification
    min_size = 2
    max_size = 5
    load_balancer_names = [ElasticLoadBalancer]


class ScheduledActionDown:
    resource: autoscaling.ScheduledAction
    auto_scaling_group_name = WebServerGroup
    max_size = '1'
    min_size = '1'
    recurrence = '0 19 * * *'


class ScheduledActionUp:
    resource: autoscaling.ScheduledAction
    auto_scaling_group_name = WebServerGroup
    max_size = '10'
    min_size = '5'
    recurrence = '0 7 * * *'
