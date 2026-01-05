"""Network resources: NeptuneDBSG."""

from . import *  # noqa: F403


class NeptuneDBSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-neptune-sg')


class NeptuneDBSG(ec2.SecurityGroup):
    group_description = 'SG of Neptune DB'
    vpc_id = ImportValue(Sub('${VPCStack}-VPCID'))
    tags = [NeptuneDBSGAssociationParameter]
