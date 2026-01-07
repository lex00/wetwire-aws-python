"""Compute resources: PrivateInstance."""

from . import *  # noqa: F403


class PrivateInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'Private'


class PrivateInstance(ec2.Instance):
    instance_type = 't3.micro'
    security_group_ids = [PrivateSG]
    subnet_id = PrivateSubnet1
    image_id = LinuxAMI
    user_data = Base64(Sub("""#!/bin/bash -x
date > /tmp/datefile
cat /tmp/datefile
# Signal the status from instance
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource PrivateInstance --region ${AWS::Region}
"""))
    tags = [PrivateInstanceAssociationParameter]
    depends_on = [CfnEndpoint]
