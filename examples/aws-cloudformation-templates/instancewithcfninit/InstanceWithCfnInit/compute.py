"""Compute resources: Instance."""

from . import *  # noqa: F403


class InstanceEbs(ec2.Instance.Ebs):
    volume_size = 32


class InstanceBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sda1'
    ebs = InstanceEbs


class Instance(ec2.Instance):
    resource: ec2.Instance
    image_id = '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-arm64}}'
    instance_type = 't4g.nano'
    key_name = 'sample'
    block_device_mappings = [InstanceBlockDeviceMapping]
    user_data = Base64(Sub("""#!/bin/bash
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource Instance --region ${AWS::Region}"""))
