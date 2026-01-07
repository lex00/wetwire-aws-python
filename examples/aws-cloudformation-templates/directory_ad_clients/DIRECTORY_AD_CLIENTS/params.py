"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AMAZONLINUX2(Parameter):
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-ebs'


class DirectoryID(Parameter):
    """Directory ID"""

    type = STRING
    description = 'Directory ID'
    allowed_pattern = '^d-[0-9a-f]{10}$'


class DirectoryName(Parameter):
    """Fully qualified name of the on-premises directory, such as corp.example.com"""

    type = STRING
    description = 'Fully qualified name of the on-premises directory, such as corp.example.com'
    allowed_pattern = '[a-zA-Z0-9-]+\\..+'
    min_length = 3
    max_length = 25


class DomainDNSServer1(Parameter):
    """(Optional) Domain DNS Server 1. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    type = STRING
    description = '(Optional) Domain DNS Server 1. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


class DomainDNSServer2(Parameter):
    """(Optional) Domain DNS Server 2. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    type = STRING
    description = '(Optional) Domain DNS Server 2. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


class DomainDNSServer3(Parameter):
    """(Optional) Domain DNS Server 3. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    type = STRING
    description = '(Optional) Domain DNS Server 3. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


class DomainDNSServer4(Parameter):
    """(Optional) Domain DNS Server 4. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain."""

    type = STRING
    description = '(Optional) Domain DNS Server 4. If DNS servers are not set, then you need to ensure the DNS servers the EC2 instances are using can resolve the AD domain.'
    allowed_pattern = '^$|^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'


class DomainMember1NetBIOSName(Parameter):
    """NetBIOS name of Domain Member 1 (using inline SSM association). Note, if computer name existed in AD before, delete from AD first."""

    type = STRING
    description = 'NetBIOS name of Domain Member 1 (using inline SSM association). Note, if computer name existed in AD before, delete from AD first.'
    default = 'SERVER1'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


class DomainMember2NetBIOSName(Parameter):
    """NetBIOS name of Domain Member 2 (using SSM association via instance id). Note, if computer name existed in AD before, delete from AD first."""

    type = STRING
    description = 'NetBIOS name of Domain Member 2 (using SSM association via instance id). Note, if computer name existed in AD before, delete from AD first.'
    default = 'SERVER2'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


class DomainMember3NetBIOSName(Parameter):
    """NetBIOS name of Domain Member 3 (using SSM association via tag). Note, if computer name existed in AD before, delete from AD first."""

    type = STRING
    description = 'NetBIOS name of Domain Member 3 (using SSM association via tag). Note, if computer name existed in AD before, delete from AD first.'
    default = 'SERVER3'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


class DomainMember4NetBIOSName(Parameter):
    """NetBIOS name of Domain Member 4 (AmazonLinux2)"""

    type = STRING
    description = 'NetBIOS name of Domain Member 4 (AmazonLinux2)'
    default = 'SERVER4'
    allowed_pattern = '[a-zA-Z0-9-]+'
    min_length = 1
    max_length = 15


class DomainMembersInstanceType(Parameter):
    """Amazon EC2 instance type for the AD Server instances"""

    type = STRING
    description = 'Amazon EC2 instance type for the AD Server instances'
    default = 't3.medium'
    allowed_values = [
    't3.medium',
    't3.large',
]


class DomainMembersLinuxInstanceProfile(Parameter):
    """Existing IAM InstanceProfile with Linux EC2 seamless join domain rights"""

    type = STRING
    description = 'Existing IAM InstanceProfile with Linux EC2 seamless join domain rights'
    allowed_pattern = '[\\w+=,.@-]+'


class DomainMembersWindowsInstanceProfile(Parameter):
    """Existing IAM InstanceProfile with Windows EC2 seamless join domain rights"""

    type = STRING
    description = 'Existing IAM InstanceProfile with Windows EC2 seamless join domain rights'
    allowed_pattern = '[\\w+=,.@-]+'


class DomainMembersSGID(Parameter):
    """Security Group ID for Domain Members Security Group"""

    type = SECURITY_GROUP_ID
    description = 'Security Group ID for Domain Members Security Group'


class EBSKMSKey(Parameter):
    """(Optional) KMS Alias, Key ID, Key ID ARN or Alias ARN to use for encrypting the EBS volumes. If empty, the default key for EBS encryption will be used of `alias/aws/ebs` or the CMK set as the default EBS encryption key."""

    type = STRING
    description = '(Optional) KMS Alias, Key ID, Key ID ARN or Alias ARN to use for encrypting the EBS volumes. If empty, the default key for EBS encryption will be used of `alias/aws/ebs` or the CMK set as the default EBS encryption key.'
    allowed_pattern = '^$|(^alias/[a-zA-Z0-9/-]{1,256}$)|(^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$)|(^arn:(aws[a-z-]*)?:kms:.*:\\d{12}:key/[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$)|(^arn:(aws[a-z-]*)?:kms:.*:\\d{12}:alias/[a-zA-Z0-9/-]{1,256}$)'


class KeyPairName(Parameter):
    """KeyPair for ONPREMISES INSTANCES"""

    type = KEY_PAIR
    description = 'KeyPair for ONPREMISES INSTANCES'


class PrivateSubnet1ID(Parameter):
    """ID of the private subnet 1 in Availability Zone 1 (e.g., subnet-a0246dcd)"""

    type = SUBNET_ID
    description = 'ID of the private subnet 1 in Availability Zone 1 (e.g., subnet-a0246dcd)'


class PrivateSubnet2ID(Parameter):
    """ID of the private subnet 2 in Availability Zone 2 (e.g., subnet-a0246dcd)"""

    type = SUBNET_ID
    description = 'ID of the private subnet 2 in Availability Zone 2 (e.g., subnet-a0246dcd)'


class SSMLogsBucketName(Parameter):
    """(Optional) SSM Logs bucket name for where Systems Manager logs should store log files. SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    type = STRING
    description = '(Optional) SSM Logs bucket name for where Systems Manager logs should store log files. SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '^$|(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'SSM Logs bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


class WINFULLBASE(Parameter):
    type = 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    default = '/aws/service/ami-windows-latest/Windows_Server-2019-English-Full-Base'


class DomainDNSServer1ConditionCondition(TemplateCondition):
    logical_id = 'DomainDNSServer1Condition'
    expression = Not(Equals(DomainDNSServer1, ''))


class DomainDNSServer2ConditionCondition(TemplateCondition):
    logical_id = 'DomainDNSServer2Condition'
    expression = Not(Equals(DomainDNSServer2, ''))


class DomainDNSServer3ConditionCondition(TemplateCondition):
    logical_id = 'DomainDNSServer3Condition'
    expression = Not(Equals(DomainDNSServer3, ''))


class DomainDNSServer4ConditionCondition(TemplateCondition):
    logical_id = 'DomainDNSServer4Condition'
    expression = Not(Equals(DomainDNSServer4, ''))


class DomainDNSServersConditionCondition(TemplateCondition):
    logical_id = 'DomainDNSServersCondition'
    expression = Or(conditions=[Condition("DomainDNSServer1Condition"), Condition("DomainDNSServer2Condition"), Condition("DomainDNSServer3Condition"), Condition("DomainDNSServer4Condition")])


class EBSKMSKeyConditionCondition(TemplateCondition):
    logical_id = 'EBSKMSKeyCondition'
    expression = Not(Equals(EBSKMSKey, ''))


class SSMLogsBucketConditionCondition(TemplateCondition):
    logical_id = 'SSMLogsBucketCondition'
    expression = Not(Equals(SSMLogsBucketName, ''))
