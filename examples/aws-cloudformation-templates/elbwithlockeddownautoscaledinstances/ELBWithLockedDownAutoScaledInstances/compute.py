"""Compute resources: LaunchConfig, WebServerGroup."""

from . import *  # noqa: F403


class LaunchConfig(autoscaling.LaunchConfiguration):
    image_id = LatestAmiId
    security_groups = [InstanceSecurityGroup]
    instance_type = InstanceType
    key_name = KeyName
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource LaunchConfig \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource WebServerGroup \
         --region ${AWS::Region} 
"""))


class WebServerGroup(autoscaling.AutoScalingGroup):
    availability_zones = GetAZs()
    launch_configuration_name = LaunchConfig
    min_size = '2'
    max_size = '2'
    load_balancer_names = [ElasticLoadBalancer]
