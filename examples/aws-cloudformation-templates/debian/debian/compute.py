"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance:
    resource: ec2.Instance
    instance_type = InstanceType
    iam_instance_profile = IAMRole
    key_name = KeyName
    image_id = InstanceAMI
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    user_data = Base64(Sub("""#!/bin/bash
wget https://s3.amazonaws.com/amazoncloudwatch-agent/debian/amd64/latest/amazon-cloudwatch-agent.deb -O /tmp/amazon-cloudwatch-agent.deb
sudo dpkg -i /tmp/amazon-cloudwatch-agent.deb
wget https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz -O /tmp/aws-cfn-bootstrap-py3-latest.tar.gz
sudo apt-get update -y
sudo apt-get install -y python3-pip python3-venv

# Create and activate a virtual environment
python3 -m venv /opt/aws/virtualenv
source /opt/aws/virtualenv/bin/activate

# Install the bootstrap package
pip install /tmp/aws-cfn-bootstrap-py3-latest.tar.gz

# Create necessary symlinks
sudo mkdir -p /opt/aws/bin
sudo ln -s /opt/aws/virtualenv/bin/cfn-* /opt/aws/bin/

# Run cfn-init
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
"""))
