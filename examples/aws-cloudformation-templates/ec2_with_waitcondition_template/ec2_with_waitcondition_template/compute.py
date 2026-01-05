"""Compute resources: KWOSInstance."""

from . import *  # noqa: F403


class KWOSInstanceAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'LaunchPlatform'
    value = LaunchPlatform


class KWOSInstanceAssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'LaunchUser'
    value = LaunchUser


class KWOSInstanceAssociationParameter2:
    resource: ec2.Instance.AssociationParameter
    key = 'TestID'
    value = TestID


class KWOSInstanceAssociationParameter3:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = InstanceName


class KWOSInstanceAssociationParameter4:
    resource: ec2.Instance.AssociationParameter
    key = 'BudgetCode'
    value = BudgetCode


class KWOSInstanceAssociationParameter5:
    resource: ec2.Instance.AssociationParameter
    key = 'TestTarget'
    value = TestTarget


class KWOSInstanceAssociationParameter6:
    resource: ec2.Instance.AssociationParameter
    key = 'AgentID'
    value = AgentID


class KWOSInstanceAssociationParameter7:
    resource: ec2.Instance.AssociationParameter
    key = 'IsMaster'
    value = IsMaster


class KWOSInstanceAssociationParameter8:
    resource: ec2.Instance.AssociationParameter
    key = 'MasterID'
    value = MasterID


class KWOSInstance(ec2.Instance):
    image_id = ImageId
    instance_type = InstanceType
    subnet_id = SubnetId
    security_group_ids = [KWOSSecurityGroup]
    key_name = KeyName
    tags = [KWOSInstanceAssociationParameter, KWOSInstanceAssociationParameter1, KWOSInstanceAssociationParameter2, KWOSInstanceAssociationParameter3, KWOSInstanceAssociationParameter4, KWOSInstanceAssociationParameter5, KWOSInstanceAssociationParameter6, KWOSInstanceAssociationParameter7, KWOSInstanceAssociationParameter8]
    monitoring = False
    user_data = Base64(Join('', [
    """#!/bin/bash
""",
    """apt-get -y install python-pip
""",
    """pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-latest.tar.gz
""",
    """# Helper function
""",
    """function error_exit
""",
    """{
""",
    '  /usr/local/bin/cfn-signal -e 1 -r "$1" \'',
    KWOSWaitHandle,
    """'
""",
    """  exit 1
""",
    """}
""",
    """# Install the basic system configuration
""",
    '/usr/local/bin/cfn-init -s ',
    AWS_STACK_ID,
    ' -r KWOSInstance ',
    '         --region ',
    AWS_REGION,
    """ || error_exit 'Failed to run cfn-init'
""",
    """# All done so signal success
""",
    '/usr/local/bin/cfn-signal -e 0 -r "KWOS setup complete" \'',
    KWOSWaitHandle,
    """'
""",
]))
