"""Template outputs."""

from . import *  # noqa: F403


class VPCIdOutput:
    """VPCId of VPC"""

    resource: Output
    value = VPC
    description = 'VPCId of VPC'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-VPC')


class PublicSubnet0Output:
    """SubnetId of public subnet 0"""

    resource: Output
    value = PublicSubnet0
    description = 'SubnetId of public subnet 0'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PublicSubnet0')


class PublicSubnet1Output:
    """SubnetId of public subnet 1"""

    resource: Output
    value = PublicSubnet1
    description = 'SubnetId of public subnet 1'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PublicSubnet1')


class PrivateSubnet0Output:
    """SubnetId of private subnet 0"""

    resource: Output
    value = PrivateSubnet0
    description = 'SubnetId of private subnet 0'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PrivateSubnet0')


class PrivateSubnet1Output:
    """SubnetId of private subnet 1"""

    resource: Output
    value = PrivateSubnet1
    description = 'SubnetId of private subnet 1'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-PrivateSubnet1')


class DefaultSecurityGroupOutput:
    """DefaultSecurityGroup Id"""

    resource: Output
    value = VPC.DefaultSecurityGroup
    description = 'DefaultSecurityGroup Id'
    export_name = Sub('${AWS::Region}-${AWS::StackName}-DefaultSecurityGroup')
