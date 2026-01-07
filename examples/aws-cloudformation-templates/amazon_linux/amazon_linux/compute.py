"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance(ec2.Instance):
    resource: ec2.Instance
    instance_type = InstanceType
    iam_instance_profile = IAMRole
    key_name = KeyName
    image_id = InstanceAMI
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    user_data = Base64(Sub("""#!/bin/bash
rpm -Uvh https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:${ssmkey} -s
/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
""", {
    'ssmkey': SSMKey,
}))
