"""Compute resources: PrivateInstance, BastionInstance."""

from . import *  # noqa: F403


class PrivateInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'Private'


class PrivateInstance(ec2.Instance):
    key_name = KeyName
    instance_type = 't2.micro'
    security_group_ids = [PrivateSG]
    subnet_id = PrivateSubnet1
    image_id = LinuxAMI
    iam_instance_profile = PrivateProfile
    user_data = Base64(Sub("""#!/bin/bash -x
date > /tmp/datefile
cat /tmp/datefile
# Signal the status from instance
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource PrivateInstance --region ${AWS::Region}
"""))
    tags = [PrivateInstanceAssociationParameter]
    depends_on = [CfnEndpoint]


class BastionInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'Bastion'


class BastionInstance(ec2.Instance):
    key_name = KeyName
    instance_type = 't2.micro'
    security_group_ids = [BastionSG]
    subnet_id = PublicSubnet1
    image_id = LinuxAMI
    iam_instance_profile = BastionProfile
    tags = [BastionInstanceAssociationParameter]
