"""Compute resources: EC2Instance1, EC2Instance2."""

from . import *  # noqa: F403


class EC2Instance1(ec2.Instance):
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    key_name = KeyName
    instance_type = InstanceType
    image_id = LatestAmiId
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region} 
"""))


class EC2Instance2(ec2.Instance):
    subnet_id = SubnetId
    security_group_ids = [InstanceSecurityGroup.GroupId]
    key_name = KeyName
    instance_type = InstanceType
    image_id = LatestAmiId
    user_data = Base64(Sub("""#!/bin/bash -xe          
yum update -y aws-cfn-bootstrap 
/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} \
         --resource EC2Instance1 \
         --region ${AWS::Region}

/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} \
         --resource EC2Instance2 \
         --region ${AWS::Region} 
"""))
