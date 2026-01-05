"""Compute resources: LaunchTemplate, WebServerGroup."""

from . import *  # noqa: F403


class LaunchTemplateIamInstanceProfileSpecification:
    resource: ec2.SpotFleet.IamInstanceProfileSpecification
    # Unknown CF key: Name = WebServerInstanceProfile


class LaunchTemplateSpotFleetLaunchSpecification:
    resource: ec2.SpotFleet.SpotFleetLaunchSpecification
    key_name = KeyName
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", InstanceType, 'Arch'))
    instance_type = InstanceType
    security_groups = [InstanceSecurityGroup]
    iam_instance_profile = LaunchTemplateIamInstanceProfileSpecification
    user_data = Base64(Sub("""#!/bin/bash -xe
yum install -y aws-cfn-bootstrap
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource LaunchTemplate --configsets full_install --region ${AWS::Region}
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource WebServerGroup --region ${AWS::Region}
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
    max_size = 4
    load_balancer_names = [ElasticLoadBalancer]
