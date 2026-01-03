"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance:
    resource: ec2.Instance
    instance_type = InstanceType
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    key_name = KeyName
    image_id = FindInMap("AWSRegionArch2AMI", AWS_REGION, FindInMap("AWSInstanceType2Arch", InstanceType, 'Arch'))
    user_data = Base64(Sub("""#!/bin/bash -xe

sudo yum update -y
sudo yum -y install python3-pip
sudo pip3 install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz
/usr/local/bin/cfn-init -v --stack ${AWS::StackName} --resource EC2Instance --configsets full_install --region ${AWS::Region} 
/usr/local/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource EC2Instance --region ${AWS::Region}
"""))
