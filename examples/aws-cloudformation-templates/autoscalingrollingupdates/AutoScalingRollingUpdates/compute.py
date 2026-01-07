"""Compute resources: LaunchConfig, WebServerGroup."""

from . import *  # noqa: F403


class LaunchConfig(autoscaling.LaunchConfiguration):
    key_name = KeyName
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", InstanceType, 'Arch'))
    instance_type = InstanceType
    security_groups = [InstanceSecurityGroup]
    iam_instance_profile = WebServerInstanceProfile
    user_data = Base64(Sub("""#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource LaunchConfig --configsets full_install --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource WebServerGroup --region ${AWS::Region}
"""))


class WebServerGroup(autoscaling.AutoScalingGroup):
    availability_zones = GetAZs()
    launch_configuration_name = LaunchConfig
    min_size = 2
    max_size = 4
    load_balancer_names = [ElasticLoadBalancer]
