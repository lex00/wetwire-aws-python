"""Compute resources: LaunchConfig, WebServerGroup."""

from . import *  # noqa: F403


class LaunchConfig(autoscaling.LaunchConfiguration):
    resource: autoscaling.LaunchConfiguration
    key_name = KeyName
    image_id = LatestAmiId
    instance_type = InstanceType
    security_groups = [InstanceSecurityGroup]
    iam_instance_profile = WebServerInstanceProfile
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource LaunchConfig \
         --configsets full_install \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource WebServerGroup \
         --region ${AWS::Region} 
"""))


class WebServerGroup(autoscaling.AutoScalingGroup):
    resource: autoscaling.AutoScalingGroup
    availability_zones = GetAZs()
    launch_configuration_name = LaunchConfig
    min_size = '2'
    max_size = '4'
    load_balancer_names = [ElasticLoadBalancer]
