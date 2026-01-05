"""Infra resources: VPCPeeringRequesterSetupStack, VPCPeeringUpdatesStack."""

from . import *  # noqa: F403


class VPCPeeringRequesterSetupStack(cloudformation.Stack):
    template_url = Sub('https://${S3Bucket}.s3.${S3Region}.${AWS::URLSuffix}/${S3KeyPrefix}templates/VPCPeering-Requester-Setup.cfn.yaml', {
    'S3Bucket': TemplatesS3BucketName,
    'S3KeyPrefix': TemplatesS3KeyPrefix,
    'S3Region': TemplatesS3BucketRegion,
})
    parameters = {
        'PeerName': PeerName,
        'PeerOwnerId': PeerOwnerId,
        'PeerRoleARN': PeerRoleARN,
        'PeerVPCID': PeerVPCID,
        'VPCID': VPCID,
    }


class VPCPeeringUpdatesStack(cloudformation.Stack):
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
        'VPCPeeringConnectionId': GetAtt("VPCPeeringRequesterSetupStack", "Outputs.VPCPeeringConnectionId"),
    }
