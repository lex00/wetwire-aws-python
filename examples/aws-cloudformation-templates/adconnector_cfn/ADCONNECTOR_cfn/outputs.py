"""Template outputs."""

from . import *  # noqa: F403


class ADConnectorDirectoryIdOutput(Output):
    """AD Connector Directory ID"""

    value = ADConnectorResource
    description = 'AD Connector Directory ID'
    export_name = Sub('${AWS::StackName}-ADConnectorDirectoryId')


class ADConnectorDirectoryNameOutput(Output):
    """AD Connector Directory Name"""

    value = DomainDNSName
    description = 'AD Connector Directory Name'
    export_name = Sub('${AWS::StackName}-ADConnectorDirectoryName')


class ADConnectorADConnectorDomainMembersSGOutput(Output):
    """ADConnector Domain Members Security Group"""

    value = ADConnectorDomainMembersSG
    description = 'ADConnector Domain Members Security Group'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorDomainMembersSG')
    condition = 'DomainMembersSGCondition'


class ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput(Output):
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector"""

    value = ADConnectorWindowsEC2DomainJoinInstanceProfile
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorWindowsEC2DomainJoinProfile')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


class ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput(Output):
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector"""

    value = ADConnectorWindowsEC2DomainJoinRole
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorWindowsEC2DomainJoinRole')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


class ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput(Output):
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector"""

    value = ADConnectorLinuxEC2DomainJoinInstanceProfile
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorLinuxEC2DomainJoinProfile')
    condition = 'LinuxEC2DomainJoinResourcesCondition'


class ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput(Output):
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector"""

    value = ADConnectorLinuxEC2DomainJoinRole
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorLinuxEC2DomainJoinRole')
    condition = 'LinuxEC2DomainJoinResourcesCondition'
