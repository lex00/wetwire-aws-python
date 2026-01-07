"""Template outputs."""

from . import *  # noqa: F403


class VPCIdOutput(Output):
    """VPCId of VPC"""

    value = VPC
    description = 'VPCId of VPC'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-VPC')


class PublicSubnet0Output(Output):
    """SubnetId of public subnet 0"""

    value = PublicSubnet0
    description = 'SubnetId of public subnet 0'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PublicSubnet0')


class PublicSubnet1Output(Output):
    """SubnetId of public subnet 1"""

    value = PublicSubnet1
    description = 'SubnetId of public subnet 1'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PublicSubnet1')


class PrivateSubnet0Output(Output):
    """SubnetId of private subnet 0"""

    value = PrivateSubnet0
    description = 'SubnetId of private subnet 0'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PrivateSubnet0')


class PrivateSubnet1Output(Output):
    """SubnetId of private subnet 1"""

    value = PrivateSubnet1
    description = 'SubnetId of private subnet 1'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PrivateSubnet1')


class DefaultSecurityGroupOutput(Output):
    """DefaultSecurityGroup Id"""

    value = VPC.DefaultSecurityGroup
    description = 'DefaultSecurityGroup Id'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-DefaultSecurityGroup')
