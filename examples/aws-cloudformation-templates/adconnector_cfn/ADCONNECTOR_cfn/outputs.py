"""Template outputs."""

from . import *  # noqa: F403


class ADConnectorDirectoryIdOutput:
    """AD Connector Directory ID"""

    resource: Output
    value = ADConnectorResource
    description = 'AD Connector Directory ID'
    export_name = Sub('${AWS::StackName}-ADConnectorDirectoryId')


class ADConnectorDirectoryNameOutput:
    """AD Connector Directory Name"""

    resource: Output
    value = DomainDNSName
    description = 'AD Connector Directory Name'
    export_name = Sub('${AWS::StackName}-ADConnectorDirectoryName')


class ADConnectorADConnectorDomainMembersSGOutput:
    """ADConnector Domain Members Security Group"""

    resource: Output
    value = ADConnectorDomainMembersSG
    description = 'ADConnector Domain Members Security Group'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorDomainMembersSG')
    condition = 'DomainMembersSGCondition'


class ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput:
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector"""

    resource: Output
    value = ADConnectorWindowsEC2DomainJoinInstanceProfile
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorWindowsEC2DomainJoinProfile')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


class ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput:
    """IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector"""

    resource: Output
    value = ADConnectorWindowsEC2DomainJoinRole
    description = 'IAM Instance Profile with SSM Document Rights to Join Windows Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorWindowsEC2DomainJoinRole')
    condition = 'WindowsEC2DomainJoinResourcesCondition'


class ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput:
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector"""

    resource: Output
    value = ADConnectorLinuxEC2DomainJoinInstanceProfile
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorLinuxEC2DomainJoinProfile')
    condition = 'LinuxEC2DomainJoinResourcesCondition'


class ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput:
    """IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector"""

    resource: Output
    value = ADConnectorLinuxEC2DomainJoinRole
    description = 'IAM Instance Profile with SSM Document Rights to Join Linux Computers via AD Connector'
    export_name = Sub('${AWS::StackName}-${DomainNetBiosName}-ADConnectorLinuxEC2DomainJoinRole')
    condition = 'LinuxEC2DomainJoinResourcesCondition'
