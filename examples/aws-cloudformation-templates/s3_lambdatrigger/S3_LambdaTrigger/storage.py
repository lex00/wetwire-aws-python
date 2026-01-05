"""Storage resources: S3BucketNotification."""

from . import *  # noqa: F403


class S3BucketNotificationServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AES256


class S3BucketNotificationServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = S3BucketNotificationServerSideEncryptionByDefault


class S3BucketNotificationBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [S3BucketNotificationServerSideEncryptionRule]


class S3BucketNotificationPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class S3BucketNotificationLambdaConfiguration(s3.Bucket.LambdaConfiguration):
    event = 's3:ObjectCreated:Put'
    function = S3TriggerLambdaFunction.Arn


class S3BucketNotificationNotificationConfiguration(s3.Bucket.NotificationConfiguration):
    lambda_configurations = [S3BucketNotificationLambdaConfiguration]


class S3BucketNotification(s3.Bucket):
    bucket_name = NotificationBucket
    bucket_encryption = S3BucketNotificationBucketEncryption
    public_access_block_configuration = S3BucketNotificationPublicAccessBlockConfiguration
    notification_configuration = S3BucketNotificationNotificationConfiguration
    depends_on = [LambdaInvokePermission]
