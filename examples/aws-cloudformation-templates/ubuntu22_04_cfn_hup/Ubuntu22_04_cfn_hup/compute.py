"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance(ec2.Instance):
    instance_type = InstanceType
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    key_name = KeyName
    image_id = InstanceAMI
    user_data = Base64(Sub("""#!/bin/bash -xe
sudo apt-get update -y
sudo apt-get -y install python3-pip
mkdir -p /opt/aws/
sudo pip3 install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-py3-latest.tar.gz
sudo ln -s /usr/local/init/ubuntu/cfn-hup /etc/init.d/cfn-hup
/usr/local/bin/cfn-init -v --stack ${AWS::StackName} --resource EC2Instance --configsets full_install --region ${AWS::Region}
/usr/local/bin/cfn-signal -e $?  --stack ${AWS::StackName} --resource EC2Instance --region ${AWS::Region}
"""))
