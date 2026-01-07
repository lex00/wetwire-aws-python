"""Template outputs."""

from . import *  # noqa: F403


class AdministratorAccessIAMRoleOutput(Output):
    """Administrator Access IAM Role"""

    value = AdministratorAccessIAMRole
    description = 'Administrator Access IAM Role'
    export_name = Sub('${AppName}-iam-${Environment}-administrator-access-role')


class LoggingBucketOutput(Output):
    """Name of S3 Logging bucket"""

    value = LoggingBucket
    description = 'Name of S3 Logging bucket'
    export_name = LoggingBucket


class LoggingBucketKMSKeyOutput(Output):
    """Logging Bucket KMS Key"""

    value = LoggingBucketKMSKey
    description = 'Logging Bucket KMS Key'
    export_name = Sub('${AppName}-${Environment}-s3-logging-kms')


class OriginALBOutput(Output):
    """The URL of the Origin ALB"""

    value = OriginALB.DNSName
    description = 'The URL of the Origin ALB'
    export_name = Sub('${AppName}-${Environment}-origin-alb-dns')


class ALBExternalAccessSGIDOutput(Output):
    """ALB External Access Security Group ID"""

    value = ALBExternalAccessSG
    description = 'ALB External Access Security Group ID'
    export_name = Sub('${AppName}-${Environment}-alb-external-access-ingrees-sg')


class EC2InstanceSGIDOutput(Output):
    """EC2 Instance Security Group ID"""

    value = EC2InstanceSG
    description = 'EC2 Instance Security Group ID'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-sg')


class EC2InstanceDNSOutput(Output):
    """EC2 Instance DNS Name"""

    value = EC2Instance.PrivateDnsName
    description = 'EC2 Instance DNS Name'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-dns')


class EC2InstanceIPOutput(Output):
    """EC2 Instance IP Address"""

    value = EC2Instance.PrivateIp
    description = 'EC2 Instance IP Address'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-ip-address')


class EC2InstanceIDOutput(Output):
    """EC2 Instance Instance ID"""

    value = EC2Instance
    description = 'EC2 Instance Instance ID'
    export_name = Sub('${AppName}-${Environment}-ec2-instance-id')


class CloudFrontEndpointOutput(Output):
    """Endpoint for Cloudfront Distribution"""

    value = CloudFrontDistribution
    description = 'Endpoint for Cloudfront Distribution'
    export_name = Sub('${AppName}-${Environment}-cloudfront-distribution')


class AlternateDomainNamesOutput(Output):
    """Alternate Domain Names (CNAME)"""

    value = AlternateDomainNames
    description = 'Alternate Domain Names (CNAME)'


class LambdaEdgeFunctionOutput(Output):
    """The Name of the Lambda@Edge Function"""

    value = 'LambdaEdgeFunction'
    description = 'The Name of the Lambda@Edge Function'
    export_name = Sub('${AppName}-${Environment}-lambda-edge-function-3')


class LambdaEdgeFunctionARNOutput(Output):
    """The ARN of the Lambda@Edge Function"""

    value = LambdaEdgeFunction.Arn
    description = 'The ARN of the Lambda@Edge Function'
    export_name = Sub('${AppName}-${Environment}-lambda-edge-function-arn-3')


class LambdaEdgeVersionOutput(Output):
    """Lambda@Edge Version Function"""

    value = LambdaEdgeVersion.Version
    description = 'Lambda@Edge Version Function'
