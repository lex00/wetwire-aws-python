"""Storage resources: PipelineS3Bucket."""

from . import *  # noqa: F403


class PipelineS3BucketServerSideEncryptionByDefault:
    resource: s3express.DirectoryBucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class PipelineS3BucketServerSideEncryptionRule:
    resource: s3express.DirectoryBucket.ServerSideEncryptionRule
    server_side_encryption_by_default = PipelineS3BucketServerSideEncryptionByDefault


class PipelineS3BucketBucketEncryption:
    resource: s3express.DirectoryBucket.BucketEncryption
    server_side_encryption_configuration = [PipelineS3BucketServerSideEncryptionRule]


class PipelineS3BucketPublicAccessBlockConfiguration:
    resource: s3objectlambda.AccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class PipelineS3Bucket:
    resource: s3.Bucket
    bucket_name = Sub('${AWS::StackName}-bucket')
    bucket_encryption = PipelineS3BucketBucketEncryption
    public_access_block_configuration = PipelineS3BucketPublicAccessBlockConfiguration
