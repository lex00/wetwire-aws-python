"""Storage resources: VPCFlowLogsBucket, VPCFlowLogsBucketPolicy."""

from . import *  # noqa: F403


class VPCFlowLogsBucketPublicAccessBlockConfiguration:
    resource: s3objectlambda.AccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class VPCFlowLogsBucketServerSideEncryptionByDefault:
    resource: s3express.DirectoryBucket.ServerSideEncryptionByDefault
    sse_algorithm = If("VPCFlowLogsBucketKMSKeyCondition", 'aws:kms', 'AES256')
    kms_master_key_id = If("VPCFlowLogsBucketKMSKeyCondition", VPCFlowLogsBucketKMSKey, AWS_NO_VALUE)


class VPCFlowLogsBucketServerSideEncryptionRule:
    resource: s3express.DirectoryBucket.ServerSideEncryptionRule
    server_side_encryption_by_default = VPCFlowLogsBucketServerSideEncryptionByDefault
    bucket_key_enabled = If("VPCFlowLogsBucketKMSKeyCondition", VPCFlowLogsBucketKeyEnabled, AWS_NO_VALUE)


class VPCFlowLogsBucketBucketEncryption:
    resource: s3express.DirectoryBucket.BucketEncryption
    server_side_encryption_configuration = [VPCFlowLogsBucketServerSideEncryptionRule]


class VPCFlowLogsBucketMetricsConfiguration:
    resource: s3tables.TableBucket.MetricsConfiguration
    status = s3.BucketVersioningStatus.ENABLED


class VPCFlowLogsBucket:
    resource: s3.Bucket
    bucket_name = Sub('aws-vpcflowlogs-${AWS::AccountId}-${AWS::Region}')
    public_access_block_configuration = VPCFlowLogsBucketPublicAccessBlockConfiguration
    bucket_encryption = VPCFlowLogsBucketBucketEncryption
    logging_configuration = If("S3AccessLogsCondition", {
    'DestinationBucketName': S3AccessLogsBucketName,
}, AWS_NO_VALUE)
    versioning_configuration = VPCFlowLogsBucketMetricsConfiguration
    condition = 'VPCFlowLogsNewBucketCondition'


class VPCFlowLogsBucketPolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AWSLogDeliveryWrite'
    principal = {
        'Service': 'delivery.logs.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}/*')
    condition = {
        STRING_EQUALS: {
            's3:x-amz-acl': 'bucket-owner-full-control',
        },
    }


class VPCFlowLogsBucketPolicyAllowStatement1:
    resource: PolicyStatement
    sid = 'AWSLogDeliveryAclCheck'
    principal = {
        'Service': 'delivery.logs.amazonaws.com',
    }
    action = 's3:GetBucketAcl'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}')


class VPCFlowLogsBucketPolicyDenyStatement2:
    resource: DenyStatement
    sid = 'DenyNonSSLRequests'
    principal = '*'
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}'),
        Sub('arn:${AWS::Partition}:s3:::${VPCFlowLogsBucket}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class VPCFlowLogsBucketPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [VPCFlowLogsBucketPolicyAllowStatement0, VPCFlowLogsBucketPolicyAllowStatement1, VPCFlowLogsBucketPolicyDenyStatement2]


class VPCFlowLogsBucketPolicy:
    resource: s3.BucketPolicy
    bucket = VPCFlowLogsBucket
    policy_document = VPCFlowLogsBucketPolicyPolicyDocument
    condition = 'VPCFlowLogsNewBucketCondition'
