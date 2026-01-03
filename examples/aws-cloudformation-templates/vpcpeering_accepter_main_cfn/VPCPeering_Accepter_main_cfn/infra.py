"""Infra resources: VPCPeeringAccepterTagStack, VPCPeeringUpdatesStack."""

from . import *  # noqa: F403


class VPCPeeringAccepterTagStack:
    resource: cloudformation.Stack
    template_url = Sub('https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${S3KeyPrefix}templates/VPCPeering-Accepter-Tag.cfn.yaml', {
    'S3Bucket': TemplatesS3BucketName,
    'S3KeyPrefix': TemplatesS3KeyPrefix,
    'S3Region': TemplatesS3BucketRegion,
})
    parameters = {
        'LambdaFunctionName': LambdaFunctionName,
        'LambdaLogLevel': LambdaLogLevel,
        'LambdaLogsCloudWatchKMSKey': LambdaLogsCloudWatchKMSKey,
        'LambdaLogsLogGroupRetention': LambdaLogsLogGroupRetention,
        'LambdaRoleName': LambdaRoleName,
        'PeerName': PeerName,
        'VPCPeeringConnectionId': VPCPeeringConnectionId,
    }


class VPCPeeringUpdatesStack:
    resource: cloudformation.Stack
    template_url = Sub('https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${S3KeyPrefix}templates/VPCPeering-Updates.cfn.yaml', {
    'S3Bucket': TemplatesS3BucketName,
    'S3KeyPrefix': TemplatesS3KeyPrefix,
    'S3Region': TemplatesS3BucketRegion,
})
    parameters = {
        'NumberOfRouteTables': NumberOfRouteTables,
        'NumberOfSecurityGroups': NumberOfSecurityGroups,
        'PeerName': PeerName,
        'PeerVPCCIDR': PeerVPCCIDR,
        'RouteTableIds': RouteTableIds,
        'SecurityGroupIds': Join(',', SecurityGroupIds),
        'VPCPeeringConnectionId': VPCPeeringConnectionId,
    }
    depends_on = [VPCPeeringAccepterTagStack]
