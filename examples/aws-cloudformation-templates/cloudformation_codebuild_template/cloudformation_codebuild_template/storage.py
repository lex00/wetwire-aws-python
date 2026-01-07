"""Storage resources: PipelineS3Bucket."""

from . import *  # noqa: F403


class PipelineS3BucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class PipelineS3BucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = PipelineS3BucketMetadataTableEncryptionConfiguration


class PipelineS3BucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [PipelineS3BucketServerSideEncryptionRule]


class PipelineS3BucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class PipelineS3Bucket(s3.Bucket):
    bucket_name = Sub('${AWS::StackName}-bucket')
    bucket_encryption = PipelineS3BucketBucketEncryption
    public_access_block_configuration = PipelineS3BucketPublicAccessBlockConfiguration
