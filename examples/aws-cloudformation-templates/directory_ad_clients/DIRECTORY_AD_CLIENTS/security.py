"""Security resources: JoinDomainAssociationInstances, JoinDomainAssociationTags."""

from . import *  # noqa: F403


class JoinDomainAssociationInstancesInstanceAssociationOutputLocation:
    resource: ssm.Association.InstanceAssociationOutputLocation
    s3_location = If("SSMLogsBucketCondition", {
    'OutputS3BucketName': SSMLogsBucketName,
    'OutputS3KeyPrefix': Sub('ssm-association-logs/AWSLogs/${AWS::AccountId}/*'),
}, AWS_NO_VALUE)


class JoinDomainAssociationInstancesSsmParameter:
    resource: ssmincidents.ResponsePlan.SsmParameter
    key = 'InstanceIds'
    values = [DomainMember2WithSsmAssociationInstance, DomainMember4LinuxWithSsmAssociationInstance]


class JoinDomainAssociationInstances:
    resource: ssm.Association
    association_name = Sub('JoinDomain-Association-viaInstances-${AWS::StackName}')
    name = 'AWS-JoinDirectoryServiceDomain'
    output_location = JoinDomainAssociationInstancesInstanceAssociationOutputLocation
    targets = [JoinDomainAssociationInstancesSsmParameter]
    parameters = {
        'directoryId': [DirectoryID],
        'directoryName': [DirectoryName],
        'dnsIpAddresses': If("DomainDNSServersCondition", [
    If("DomainDNSServer1Condition", DomainDNSServer1, AWS_NO_VALUE),
    If("DomainDNSServer2Condition", DomainDNSServer2, AWS_NO_VALUE),
    If("DomainDNSServer3Condition", DomainDNSServer3, AWS_NO_VALUE),
    If("DomainDNSServer4Condition", DomainDNSServer4, AWS_NO_VALUE),
], AWS_NO_VALUE),
    }


class JoinDomainAssociationTagsInstanceAssociationOutputLocation:
    resource: ssm.Association.InstanceAssociationOutputLocation
    s3_location = If("SSMLogsBucketCondition", {
    'OutputS3BucketName': SSMLogsBucketName,
    'OutputS3KeyPrefix': Sub('ssm-association-logs/AWSLogs/${AWS::AccountId}/*'),
}, AWS_NO_VALUE)


class JoinDomainAssociationTagsSsmParameter:
    resource: ssmincidents.ResponsePlan.SsmParameter
    key = 'tag:DomainJoin'
    values = [DirectoryName]


class JoinDomainAssociationTags:
    resource: ssm.Association
    association_name = Sub('JoinDomain-Association-viaTags-${AWS::StackName}')
    name = 'AWS-JoinDirectoryServiceDomain'
    output_location = JoinDomainAssociationTagsInstanceAssociationOutputLocation
    targets = [JoinDomainAssociationTagsSsmParameter]
    parameters = {
        'directoryId': [DirectoryID],
        'directoryName': [DirectoryName],
        'dnsIpAddresses': If("DomainDNSServersCondition", [
    If("DomainDNSServer1Condition", DomainDNSServer1, AWS_NO_VALUE),
    If("DomainDNSServer2Condition", DomainDNSServer2, AWS_NO_VALUE),
    If("DomainDNSServer3Condition", DomainDNSServer3, AWS_NO_VALUE),
    If("DomainDNSServer4Condition", DomainDNSServer4, AWS_NO_VALUE),
], AWS_NO_VALUE),
    }
