"""Storage resources: S3BucketDestination, S3BucketDestinationPolicy."""

from . import *  # noqa: F403


class S3BucketDestinationServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AWSKMS
    kms_master_key_id = KmsKey


class S3BucketDestinationServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = S3BucketDestinationServerSideEncryptionByDefault
    bucket_key_enabled = True


class S3BucketDestinationBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [S3BucketDestinationServerSideEncryptionRule]


class S3BucketDestinationPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class S3BucketDestinationDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class S3BucketDestination(s3.Bucket):
    resource: s3.Bucket
    bucket_name = Sub('${AWS::StackName}-${AWS::AccountId}-bucket')
    bucket_encryption = S3BucketDestinationBucketEncryption
    public_access_block_configuration = S3BucketDestinationPublicAccessBlockConfiguration
    versioning_configuration = S3BucketDestinationDeleteMarkerReplication
    deletion_policy = 'Delete'


class S3BucketDestinationPolicyAllowStatement0(PolicyStatement):
    sid = 'Allow source account access to destination bucket'
    principal = {
        'AWS': AccountIdSource,
    }
    action = [
        's3:ReplicateDelete',
        's3:ReplicateObject',
        's3:ReplicateTags',
        's3:GetObjectVersionTagging',
        's3:ObjectOwnerOverrideToBucketOwner',
    ]
    resource_arn = Sub('${varBucketArn}/*', {
    'varBucketArn': S3BucketDestination.Arn,
})


class S3BucketDestinationPolicyDenyStatement1(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = Sub('${varBucketArn}/*', {
    'varBucketArn': S3BucketDestination.Arn,
})
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class S3BucketDestinationPolicyPolicyDocument(PolicyDocument):
    statement = [S3BucketDestinationPolicyAllowStatement0, S3BucketDestinationPolicyDenyStatement1]


class S3BucketDestinationPolicy(s3.BucketPolicy):
    resource: s3.BucketPolicy
    bucket = S3BucketDestination
    policy_document = S3BucketDestinationPolicyPolicyDocument
