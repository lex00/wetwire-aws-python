"""Compute resources: DomainMember2WithSsmAssociationInstance, DomainMember4LinuxWithSsmAssociationInstance, DomainMember1WithInlineSsmAssociation, DomainMember3WithSsmAssociationTag."""

from . import *  # noqa: F403


class DomainMember2WithSsmAssociationInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = DomainMember2NetBIOSName


class DomainMember2WithSsmAssociationInstanceEbs(ec2.Instance.Ebs):
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", EBSKMSKey, AWS_NO_VALUE)


class DomainMember2WithSsmAssociationInstanceBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sda1'
    ebs = DomainMember2WithSsmAssociationInstanceEbs


class DomainMember2WithSsmAssociationInstance(ec2.Instance):
    image_id = WINFULLBASE
    iam_instance_profile = DomainMembersWindowsInstanceProfile
    instance_type = DomainMembersInstanceType
    subnet_id = PrivateSubnet2ID
    tags = [DomainMember2WithSsmAssociationInstanceAssociationParameter]
    block_device_mappings = [DomainMember2WithSsmAssociationInstanceBlockDeviceMapping]
    security_group_ids = [DomainMembersSGID]
    key_name = KeyPairName
    user_data = Base64(Sub("""<powershell>
$instanceId = "null"
while ($instanceId -NotLike "i-*") {
Start-Sleep -s 3
$instanceId = Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/instance-id
}
Rename-Computer -NewName ${DomainMember2NetBIOSName} -Force
# Set-TimeZone -Name "US Eastern Standard Time"

Install-WindowsFeature -IncludeAllSubFeature RSAT
Restart-Computer -Force
</powershell>
"""))


class DomainMember4LinuxWithSsmAssociationInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = DomainMember4NetBIOSName


class DomainMember4LinuxWithSsmAssociationInstanceEbs(ec2.Instance.Ebs):
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", EBSKMSKey, AWS_NO_VALUE)


class DomainMember4LinuxWithSsmAssociationInstanceBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sda1'
    ebs = DomainMember4LinuxWithSsmAssociationInstanceEbs


class DomainMember4LinuxWithSsmAssociationInstance(ec2.Instance):
    image_id = AMAZONLINUX2
    iam_instance_profile = DomainMembersLinuxInstanceProfile
    instance_type = DomainMembersInstanceType
    subnet_id = PrivateSubnet2ID
    tags = [DomainMember4LinuxWithSsmAssociationInstanceAssociationParameter]
    block_device_mappings = [DomainMember4LinuxWithSsmAssociationInstanceBlockDeviceMapping]
    security_group_ids = [DomainMembersSGID]
    key_name = KeyPairName
    user_data = Base64(Sub("""# Set HostName
LowerEc2Name=$(echo ${DomainMember4NetBIOSName} | tr '[:upper:]' '[:lower:]')
hostnamectl set-hostname $LowerEc2Name
# Set TimeZone
# sed -i 's|^ZONE=.*|ZONE="America/New_York"|' /etc/sysconfig/clock
# ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime
# Patch System Up
yum update -y
# Reboot
reboot
"""))


class DomainMember1WithInlineSsmAssociationAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'directoryId'
    value = [DirectoryID]


class DomainMember1WithInlineSsmAssociationAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'directoryName'
    value = [DirectoryName]


class DomainMember1WithInlineSsmAssociationSsmAssociation(ec2.Instance.SsmAssociation):
    document_name = 'AWS-JoinDirectoryServiceDomain'
    association_parameters = [DomainMember1WithInlineSsmAssociationAssociationParameter, DomainMember1WithInlineSsmAssociationAssociationParameter1, If("DomainDNSServersCondition", {
    'Key': 'dnsIpAddresses',
    'Value': [
        If("DomainDNSServer1Condition", DomainDNSServer1, AWS_NO_VALUE),
        If("DomainDNSServer2Condition", DomainDNSServer2, AWS_NO_VALUE),
        If("DomainDNSServer3Condition", DomainDNSServer3, AWS_NO_VALUE),
        If("DomainDNSServer4Condition", DomainDNSServer4, AWS_NO_VALUE),
    ],
}, AWS_NO_VALUE)]


class DomainMember1WithInlineSsmAssociationAssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = DomainMember1NetBIOSName


class DomainMember1WithInlineSsmAssociationEbs(ec2.Instance.Ebs):
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", EBSKMSKey, AWS_NO_VALUE)


class DomainMember1WithInlineSsmAssociationBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sda1'
    ebs = DomainMember1WithInlineSsmAssociationEbs


class DomainMember1WithInlineSsmAssociation(ec2.Instance):
    image_id = WINFULLBASE
    iam_instance_profile = DomainMembersWindowsInstanceProfile
    ssm_associations = [DomainMember1WithInlineSsmAssociationSsmAssociation]
    instance_type = DomainMembersInstanceType
    subnet_id = PrivateSubnet1ID
    tags = [DomainMember1WithInlineSsmAssociationAssociationParameter2]
    block_device_mappings = [DomainMember1WithInlineSsmAssociationBlockDeviceMapping]
    security_group_ids = [DomainMembersSGID]
    key_name = KeyPairName
    user_data = Base64(Sub("""<powershell>
$instanceId = "null"
while ($instanceId -NotLike "i-*") {
Start-Sleep -s 3
$instanceId = Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/instance-id
}
Rename-Computer -NewName ${DomainMember1NetBIOSName} -Force
# Set-TimeZone -Name "US Eastern Standard Time"

Install-WindowsFeature -IncludeAllSubFeature RSAT
Restart-Computer -Force
</powershell>
"""))


class DomainMember3WithSsmAssociationTagAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = DomainMember3NetBIOSName


class DomainMember3WithSsmAssociationTagAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'DomainJoin'
    value = DirectoryName


class DomainMember3WithSsmAssociationTagEbs(ec2.Instance.Ebs):
    encrypted = True
    volume_type = 'gp3'
    delete_on_termination = True
    volume_size = 100
    kms_key_id = If("EBSKMSKeyCondition", EBSKMSKey, AWS_NO_VALUE)


class DomainMember3WithSsmAssociationTagBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sda1'
    ebs = DomainMember3WithSsmAssociationTagEbs


class DomainMember3WithSsmAssociationTag(ec2.Instance):
    image_id = WINFULLBASE
    iam_instance_profile = DomainMembersWindowsInstanceProfile
    instance_type = DomainMembersInstanceType
    subnet_id = PrivateSubnet1ID
    tags = [DomainMember3WithSsmAssociationTagAssociationParameter, DomainMember3WithSsmAssociationTagAssociationParameter1]
    block_device_mappings = [DomainMember3WithSsmAssociationTagBlockDeviceMapping]
    security_group_ids = [DomainMembersSGID]
    key_name = KeyPairName
    user_data = Base64(Sub("""<powershell>
$instanceId = "null"
while ($instanceId -NotLike "i-*") {
Start-Sleep -s 3
$instanceId = Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/instance-id
}
Rename-Computer -NewName ${DomainMember3NetBIOSName} -Force
# Set-TimeZone -Name "US Eastern Standard Time"

Install-WindowsFeature -IncludeAllSubFeature RSAT
Restart-Computer -Force
</powershell>
"""))
