"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance:
    resource: ec2.Instance
    instance_type = InstanceType
    iam_instance_profile = IAMRole
    key_name = KeyName
    image_id = FindInMap("RegionMap", AWS_REGION, SUSEVersion)
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    user_data = Base64(Sub("""#!/bin/bash
rpm -Uvh https://s3.amazonaws.com/amazoncloudwatch-agent/suse/amd64/latest/amazon-cloudwatch-agent.rpm
curl -O https://bootstrap.pypa.io/pip/3.6/get-pip.py
# Install pip using python3
python3 get-pip.py
export PATH=$PATH:/usr/local/bin
pip3 install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz
cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
"""))
