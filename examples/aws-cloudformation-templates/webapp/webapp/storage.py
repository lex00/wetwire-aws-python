"""Storage resources: SiteCloudFrontLogsReplicaBucket, SiteCloudFrontLogsLogBucket, SiteContentLogBucket, SiteContentReplicaBucket, SiteContentLogBucketAccessPolicy, SiteContentReplicaBucketAccessPolicy, SiteCloudFrontLogsLogBucketAccessPolicy, SiteCloudFrontLogsReplicaBucketAccessPolicy."""

from . import *  # noqa: F403


class SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault


class SiteCloudFrontLogsReplicaBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule]


class SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsReplicaBucket:
    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication


class SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteCloudFrontLogsLogBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault


class SiteCloudFrontLogsLogBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsLogBucketServerSideEncryptionRule]


class SiteCloudFrontLogsLogBucketDefaultRetention:
    resource: s3.Bucket.DefaultRetention
    mode = 'COMPLIANCE'
    years = 1


class SiteCloudFrontLogsLogBucketObjectLockRule:
    resource: s3.Bucket.ObjectLockRule
    default_retention = SiteCloudFrontLogsLogBucketDefaultRetention


class SiteCloudFrontLogsLogBucketObjectLockConfiguration:
    resource: s3.Bucket.ObjectLockConfiguration
    object_lock_enabled = 'Enabled'
    rule = SiteCloudFrontLogsLogBucketObjectLockRule


class SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteCloudFrontLogsLogBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsLogBucket:
    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteCloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsLogBucketDeleteMarkerReplication


class SiteContentLogBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteContentLogBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentLogBucketServerSideEncryptionByDefault


class SiteContentLogBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentLogBucketServerSideEncryptionRule]


class SiteContentLogBucketDefaultRetention:
    resource: s3.Bucket.DefaultRetention
    mode = 'COMPLIANCE'
    years = 1


class SiteContentLogBucketObjectLockRule:
    resource: s3.Bucket.ObjectLockRule
    default_retention = SiteContentLogBucketDefaultRetention


class SiteContentLogBucketObjectLockConfiguration:
    resource: s3.Bucket.ObjectLockConfiguration
    object_lock_enabled = 'Enabled'
    rule = SiteContentLogBucketObjectLockRule


class SiteContentLogBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteContentLogBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentLogBucket:
    resource: s3.Bucket
    bucket_encryption = SiteContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentLogBucketDeleteMarkerReplication


class SiteContentReplicaBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteContentReplicaBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentReplicaBucketServerSideEncryptionByDefault


class SiteContentReplicaBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentReplicaBucketServerSideEncryptionRule]


class SiteContentReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteContentReplicaBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentReplicaBucket:
    resource: s3.Bucket
    bucket_encryption = SiteContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentReplicaBucketDeleteMarkerReplication


class SiteContentLogBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class SiteContentLogBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class SiteContentLogBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentLogBucketAccessPolicyDenyStatement0, SiteContentLogBucketAccessPolicyAllowStatement1]


class SiteContentLogBucketAccessPolicy:
    resource: s3.BucketPolicy
    bucket = SiteContentLogBucket
    policy_document = SiteContentLogBucketAccessPolicyPolicyDocument


class SiteContentReplicaBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class SiteContentReplicaBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class SiteContentReplicaBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicaBucketAccessPolicyDenyStatement0, SiteContentReplicaBucketAccessPolicyAllowStatement1]


class SiteContentReplicaBucketAccessPolicy:
    resource: s3.BucketPolicy
    bucket = SiteContentReplicaBucket
    policy_document = SiteContentReplicaBucketAccessPolicyPolicyDocument


class SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1]


class SiteCloudFrontLogsLogBucketAccessPolicy:
    resource: s3.BucketPolicy
    bucket = SiteCloudFrontLogsLogBucket
    policy_document = SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument


class SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0:
    resource: DenyStatement
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1:
    resource: PolicyStatement
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1]


class SiteCloudFrontLogsReplicaBucketAccessPolicy:
    resource: s3.BucketPolicy
    bucket = SiteCloudFrontLogsReplicaBucket
    policy_document = SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument
