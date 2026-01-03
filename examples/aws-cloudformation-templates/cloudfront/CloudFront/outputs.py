"""Template outputs."""

from . import *  # noqa: F403


class AdministratorAccessIAMRoleOutput:
    """Administrator Access IAM Role"""

    resource: Output
    value = AdministratorAccessIAMRole
    description = 'Administrator Access IAM Role'
    export_name = Sub('${AppName}-iam-${Environment}-administrator-access-role')


class LoggingBucketOutput:
    """Name of S3 Logging bucket"""

    resource: Output
    value = LoggingBucket
    description = 'Name of S3 Logging bucket'
    export_name = LoggingBucket


class LoggingBucketKMSKeyOutput:
    """Logging Bucket KMS Key"""

    resource: Output
    value = LoggingBucketKMSKey
    description = 'Logging Bucket KMS Key'
    export_name = Sub('${AppName}-${Environment}-s3-logging-kms')


class OriginALBOutput:
    """The URL of the Origin ALB"""

    resource: Output
    value = OriginALB.DNSName
    description = 'The URL of the Origin ALB'
    export_name = Sub('${AppName}-${Environment}-origin-alb-dns')


class ALBExternalAccessSGIDOutput:
    """ALB External Access Security Group ID"""

    resource: Output
    value = ALBExternalAccessSG
    description = 'ALB External Access Security Group ID'
    export_name = Sub('${AppName}-${Environment}-alb-external-access-ingrees-sg')


class EC2InstanceSGIDOutput:
    """EC2 Instance Security Group ID"""

    resource: Output
    value = EC2InstanceSG
    description = 'EC2 Instance Security Group ID'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-sg')


class EC2InstanceDNSOutput:
    """EC2 Instance DNS Name"""

    resource: Output
    value = EC2Instance.PrivateDnsName
    description = 'EC2 Instance DNS Name'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-dns')


class EC2InstanceIPOutput:
    """EC2 Instance IP Address"""

    resource: Output
    value = EC2Instance.PrivateIp
    description = 'EC2 Instance IP Address'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-ip-address')


class EC2InstanceIDOutput:
    """EC2 Instance Instance ID"""

    resource: Output
    value = EC2Instance
    description = 'EC2 Instance Instance ID'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-id')


class CloudFrontEndpointOutput:
    """Endpoint for Cloudfront Distribution"""

    resource: Output
    value = CloudFrontDistribution
    description = 'Endpoint for Cloudfront Distribution'
    export_name = Sub('${AppName}-${Environment}-cloudfront-distribution')


class AlternateDomainNamesOutput:
    """Alternate Domain Names (CNAME)"""

    resource: Output
    value = AlternateDomainNames
    description = 'Alternate Domain Names (CNAME)'


class LambdaEdgeFunctionOutput:
    """The Name of the Lambda@Edge Function"""

    resource: Output
    value = 'LambdaEdgeFunction'
    description = 'The Name of the Lambda@Edge Function'
    export_name = Sub('${AppName}-${Environment}-lambda-edge-function-3')


class LambdaEdgeFunctionARNOutput:
    """The ARN of the Lambda@Edge Function"""

    resource: Output
    value = LambdaEdgeFunction.Arn
    description = 'The ARN of the Lambda@Edge Function'
    export_name = Sub('${AppName}-${Environment}-lambda-edge-function-arn-3')


class LambdaEdgeVersionOutput:
    """Lambda@Edge Version Function"""

    resource: Output
    value = LambdaEdgeVersion.Version
    description = 'Lambda@Edge Version Function'
