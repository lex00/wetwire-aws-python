"""Security resources: JoinDomainAssociationTags, JoinDomainAssociationInstances."""

from . import *  # noqa: F403


class JoinDomainAssociationTagsInstanceAssociationOutputLocation(ssm.Association.InstanceAssociationOutputLocation):
    s3_location = If("SSMLogsBucketCondition", {
    'OutputS3BucketName': SSMLogsBucketName,
    'OutputS3KeyPrefix': Sub('ssm-association-logs/AWSLogs/${AWS::AccountId}/*'),
}, AWS_NO_VALUE)


class JoinDomainAssociationTagsTargets(ssm.MaintenanceWindowTarget.Targets):
    key = 'tag:DomainJoin'
    values = [DirectoryName]


class JoinDomainAssociationTags(ssm.Association):
    association_name = Sub('JoinDomain-Association-viaTags-${AWS::StackName}')
    name = 'AWS-JoinDirectoryServiceDomain'
    output_location = JoinDomainAssociationTagsInstanceAssociationOutputLocation
    targets = [JoinDomainAssociationTagsTargets]
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


class JoinDomainAssociationInstancesInstanceAssociationOutputLocation(ssm.Association.InstanceAssociationOutputLocation):
    s3_location = If("SSMLogsBucketCondition", {
    'OutputS3BucketName': SSMLogsBucketName,
    'OutputS3KeyPrefix': Sub('ssm-association-logs/AWSLogs/${AWS::AccountId}/*'),
}, AWS_NO_VALUE)


class JoinDomainAssociationInstancesTargets(ssm.MaintenanceWindowTarget.Targets):
    key = 'InstanceIds'
    values = [DomainMember2WithSsmAssociationInstance, DomainMember4LinuxWithSsmAssociationInstance]


class JoinDomainAssociationInstances(ssm.Association):
    association_name = Sub('JoinDomain-Association-viaInstances-${AWS::StackName}')
    name = 'AWS-JoinDirectoryServiceDomain'
    output_location = JoinDomainAssociationInstancesInstanceAssociationOutputLocation
    targets = [JoinDomainAssociationInstancesTargets]
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
