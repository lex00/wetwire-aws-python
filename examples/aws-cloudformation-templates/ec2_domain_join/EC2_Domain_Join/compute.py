"""Compute resources: myEC2InstanceSSM."""

from . import *  # noqa: F403


class myEC2InstanceSSMAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'directoryId'
    value = [ADDirectoryId]


class myEC2InstanceSSMAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'directoryName'
    value = [ADDirectoryName]


class myEC2InstanceSSMAssociationParameter2(ec2.Instance.AssociationParameter):
    key = 'dnsIpAddresses'
    value = [ADDnsIpAddresses1, ADDnsIpAddresses2]


class myEC2InstanceSSMSsmAssociation(ec2.Instance.SsmAssociation):
    document_name = myssmdocument
    association_parameters = [myEC2InstanceSSMAssociationParameter, myEC2InstanceSSMAssociationParameter1, myEC2InstanceSSMAssociationParameter2]


class myEC2InstanceSSMAssociationParameter3(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'myEC2InstanceSSM'


class myEC2InstanceSSM(ec2.Instance):
    iam_instance_profile = myInstanceProfile
    ssm_associations = [myEC2InstanceSSMSsmAssociation]
    key_name = KeyPair
    image_id = AMI
    instance_type = InstanceType
    tags = [myEC2InstanceSSMAssociationParameter3]
    subnet_id = PublicSubnet
    security_group_ids = [InstanceSecurityGroup.GroupId]
