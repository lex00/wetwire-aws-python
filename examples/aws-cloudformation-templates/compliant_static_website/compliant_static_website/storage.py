"""Storage resources: CloudFrontLogsReplicaBucket, CloudFrontLogsLogBucket, CloudFrontLogsBucket, ContentReplicaBucket, ContentLogBucket, ContentBucket, ContentBucketPolicyPolicy, ContentLogBucketPolicyPolicy, ContentReplicaBucketPolicyPolicy, CloudFrontLogsBucketPolicyPolicy, CloudFrontLogsReplicaBucketPolicyPolicy, CloudFrontLogsLogBucketPolicyPolicy."""

from . import *  # noqa: F403


class CloudFrontLogsReplicaBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class CloudFrontLogsReplicaBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = CloudFrontLogsReplicaBucketMetadataTableEncryptionConfiguration


class CloudFrontLogsReplicaBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [CloudFrontLogsReplicaBucketServerSideEncryptionRule]


class CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class CloudFrontLogsReplicaBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsReplicaBucket(s3.Bucket):
    bucket_encryption = CloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsReplicaBucketDeleteMarkerReplication


class CloudFrontLogsLogBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class CloudFrontLogsLogBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = CloudFrontLogsLogBucketMetadataTableEncryptionConfiguration


class CloudFrontLogsLogBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [CloudFrontLogsLogBucketServerSideEncryptionRule]


class CloudFrontLogsLogBucketDefaultRetention(s3.Bucket.DefaultRetention):
    mode = 'COMPLIANCE'
    years = 1


class CloudFrontLogsLogBucketObjectLockRule(s3.Bucket.ObjectLockRule):
    default_retention = CloudFrontLogsLogBucketDefaultRetention


class CloudFrontLogsLogBucketObjectLockConfiguration(s3.Bucket.ObjectLockConfiguration):
    object_lock_enabled = 'Enabled'
    rule = CloudFrontLogsLogBucketObjectLockRule


class CloudFrontLogsLogBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class CloudFrontLogsLogBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsLogBucket(s3.Bucket):
    bucket_encryption = CloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = CloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = CloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsLogBucketDeleteMarkerReplication


class CloudFrontLogsBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class CloudFrontLogsBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = CloudFrontLogsBucketMetadataTableEncryptionConfiguration


class CloudFrontLogsBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [CloudFrontLogsBucketServerSideEncryptionRule]


class CloudFrontLogsBucketLoggingConfiguration(s3.Bucket.LoggingConfiguration):
    destination_bucket_name = CloudFrontLogsLogBucket


class CloudFrontLogsBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class CloudFrontLogsBucketReplicationDestination(s3.Bucket.ReplicationDestination):
    bucket = CloudFrontLogsReplicaBucket.Arn


class CloudFrontLogsBucketReplicationRule(s3.Bucket.ReplicationRule):
    destination = CloudFrontLogsBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsBucketReplicationConfiguration(s3.Bucket.ReplicationConfiguration):
    role = CloudFrontLogsReplicationRole.Arn
    rules = [CloudFrontLogsBucketReplicationRule]


class CloudFrontLogsBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsBucket(s3.Bucket):
    bucket_encryption = CloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = CloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = CloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = CloudFrontLogsBucketDeleteMarkerReplication


class ContentReplicaBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class ContentReplicaBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = ContentReplicaBucketMetadataTableEncryptionConfiguration


class ContentReplicaBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [ContentReplicaBucketServerSideEncryptionRule]


class ContentReplicaBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ContentReplicaBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class ContentReplicaBucket(s3.Bucket):
    bucket_encryption = ContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = ContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentReplicaBucketDeleteMarkerReplication


class ContentLogBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class ContentLogBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = ContentLogBucketMetadataTableEncryptionConfiguration


class ContentLogBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [ContentLogBucketServerSideEncryptionRule]


class ContentLogBucketDefaultRetention(s3.Bucket.DefaultRetention):
    mode = 'COMPLIANCE'
    years = 1


class ContentLogBucketObjectLockRule(s3.Bucket.ObjectLockRule):
    default_retention = ContentLogBucketDefaultRetention


class ContentLogBucketObjectLockConfiguration(s3.Bucket.ObjectLockConfiguration):
    object_lock_enabled = 'Enabled'
    rule = ContentLogBucketObjectLockRule


class ContentLogBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ContentLogBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class ContentLogBucket(s3.Bucket):
    bucket_encryption = ContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = ContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = ContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentLogBucketDeleteMarkerReplication


class ContentBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class ContentBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = ContentBucketMetadataTableEncryptionConfiguration


class ContentBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [ContentBucketServerSideEncryptionRule]


class ContentBucketLoggingConfiguration(s3.Bucket.LoggingConfiguration):
    destination_bucket_name = ContentLogBucket


class ContentBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ContentBucketReplicationDestination(s3.Bucket.ReplicationDestination):
    bucket = ContentReplicaBucket.Arn


class ContentBucketReplicationRule(s3.Bucket.ReplicationRule):
    destination = ContentBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class ContentBucketReplicationConfiguration(s3.Bucket.ReplicationConfiguration):
    role = ContentReplicationRole.Arn
    rules = [ContentBucketReplicationRule]


class ContentBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class ContentBucket(s3.Bucket):
    bucket_encryption = ContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ContentBucketPublicAccessBlockConfiguration
    replication_configuration = ContentBucketReplicationConfiguration
    versioning_configuration = ContentBucketDeleteMarkerReplication


class ContentBucketPolicyPolicyDenyStatement0(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class ContentBucketPolicyPolicyAllowStatement1(PolicyStatement):
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class ContentBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [ContentBucketPolicyPolicyDenyStatement0, ContentBucketPolicyPolicyAllowStatement1]


class ContentBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ContentBucket
    policy_document = ContentBucketPolicyPolicyPolicyDocument


class ContentLogBucketPolicyPolicyDenyStatement0(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class ContentLogBucketPolicyPolicyAllowStatement1(PolicyStatement):
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-logs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class ContentLogBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [ContentLogBucketPolicyPolicyDenyStatement0, ContentLogBucketPolicyPolicyAllowStatement1]


class ContentLogBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ContentLogBucket
    policy_document = ContentLogBucketPolicyPolicyPolicyDocument


class ContentReplicaBucketPolicyPolicyDenyStatement0(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class ContentReplicaBucketPolicyPolicyAllowStatement1(PolicyStatement):
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class ContentReplicaBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [ContentReplicaBucketPolicyPolicyDenyStatement0, ContentReplicaBucketPolicyPolicyAllowStatement1]


class ContentReplicaBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ContentReplicaBucket
    policy_document = ContentReplicaBucketPolicyPolicyPolicyDocument


class CloudFrontLogsBucketPolicyPolicyDenyStatement0(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class CloudFrontLogsBucketPolicyPolicyAllowStatement1(PolicyStatement):
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class CloudFrontLogsBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [CloudFrontLogsBucketPolicyPolicyDenyStatement0, CloudFrontLogsBucketPolicyPolicyAllowStatement1]


class CloudFrontLogsBucketPolicyPolicy(s3.BucketPolicy):
    bucket = CloudFrontLogsBucket
    policy_document = CloudFrontLogsBucketPolicyPolicyPolicyDocument


class CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0, CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1]


class CloudFrontLogsReplicaBucketPolicyPolicy(s3.BucketPolicy):
    bucket = CloudFrontLogsReplicaBucket
    policy_document = CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument


class CloudFrontLogsLogBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class CloudFrontLogsLogBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class CloudFrontLogsLogBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [CloudFrontLogsLogBucketPolicyPolicyDenyStatement0, CloudFrontLogsLogBucketPolicyPolicyAllowStatement1]


class CloudFrontLogsLogBucketPolicyPolicy(s3.BucketPolicy):
    bucket = CloudFrontLogsLogBucket
    policy_document = CloudFrontLogsLogBucketPolicyPolicyPolicyDocument
