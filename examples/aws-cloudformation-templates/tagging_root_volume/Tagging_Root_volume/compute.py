"""Compute resources: WindowsInstance, LinuxInstance."""

from . import *  # noqa: F403


class WindowsInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = AWS_STACK_NAME


class WindowsInstanceEbs(ec2.Instance.Ebs):
    volume_type = 'io1'
    iops = '200'
    delete_on_termination = 'true'
    volume_size = '10'


class WindowsInstanceBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sdm'
    ebs = WindowsInstanceEbs


class WindowsInstance(ec2.Instance):
    resource: ec2.Instance
    image_id = WindowsAMIID
    subnet_id = SubnetId
    instance_type = InstanceType
    availability_zone = InstanceAZ
    iam_instance_profile = InstanceProfile
    key_name = KeyName
    user_data = Base64("""<powershell>
  $AWS_AVAIL_ZONE=(curl http://169.254.169.254/latest/meta-data/placement/availability-zone).Content
  $AWS_REGION=$AWS_AVAIL_ZONE.Substring(0,$AWS_AVAIL_ZONE.length-1)
  $AWS_INSTANCE_ID=(curl http://169.254.169.254/latest/meta-data/instance-id).Content
  $ROOT_VOLUME_IDS=((Get-EC2Instance -Region $AWS_REGION -InstanceId $AWS_INSTANCE_ID).Instances.BlockDeviceMappings | where-object DeviceName -match '/dev/sda1').Ebs.VolumeId
  $tag = New-Object Amazon.EC2.Model.Tag
  $tag.key = "MyRootTag"
  $tag.value = "MyRootVolumesValue"
  New-EC2Tag -Resource $ROOT_VOLUME_IDS -Region $AWS_REGION -Tag $tag
</powershell>
""")
    tags = [WindowsInstanceAssociationParameter]
    block_device_mappings = [WindowsInstanceBlockDeviceMapping]


class LinuxInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = AWS_STACK_NAME


class LinuxInstanceEbs(ec2.Instance.Ebs):
    volume_type = 'io1'
    iops = '200'
    delete_on_termination = 'true'
    volume_size = '10'


class LinuxInstanceBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sdm'
    ebs = LinuxInstanceEbs


class LinuxInstance(ec2.Instance):
    resource: ec2.Instance
    image_id = LinuxAMIID
    subnet_id = SubnetId
    instance_type = InstanceType
    availability_zone = InstanceAZ
    iam_instance_profile = InstanceProfile
    key_name = KeyName
    user_data = Base64("""AWS_AVAIL_ZONE=$(curl http://169.254.169.254/latest/meta-data/placement/availability-zone)
AWS_REGION="`echo \"$AWS_AVAIL_ZONE\" | sed 's/[a-z]$//'`"
AWS_INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id)
ROOT_VOLUME_IDS=$(aws ec2 describe-instances --region $AWS_REGION --instance-id $AWS_INSTANCE_ID --output text --query Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId)
aws ec2 create-tags --resources $ROOT_VOLUME_IDS --region $AWS_REGION --tags Key=MyRootTag,Value=MyRootVolumesValue
""")
    tags = [LinuxInstanceAssociationParameter]
    block_device_mappings = [LinuxInstanceBlockDeviceMapping]
