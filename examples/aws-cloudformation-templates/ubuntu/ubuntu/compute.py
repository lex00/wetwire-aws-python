"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance(ec2.Instance):
    instance_type = InstanceType
    iam_instance_profile = IAMRole
    key_name = KeyName
    image_id = InstanceAMI
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    user_data = Base64(Sub("""#!/bin/bash
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb -O /tmp/amazon-cloudwatch-agent.deb
dpkg -i /tmp/amazon-cloudwatch-agent.deb
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:${ssmkey} -s
apt-get update -y
apt-get install -y python3 python3-pip
pip3 install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz
cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
""", {
    'ssmkey': SSMKey,
}))
