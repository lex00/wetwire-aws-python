"""Storage resources: CloudFrontLogsBucketPolicyPolicy, ContentReplicaBucket, ContentLogBucket, ContentBucket, ContentReplicaBucketPolicyPolicy, CloudFrontLogsLogBucketPolicyPolicy, ContentLogBucketPolicyPolicy, CloudFrontLogsLogBucket, CloudFrontLogsReplicaBucket, CloudFrontLogsBucket, ContentBucketPolicyPolicy, CloudFrontLogsReplicaBucketPolicyPolicy."""

from . import *  # noqa: F403


class CloudFrontLogsBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
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


class CloudFrontLogsBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
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


class CloudFrontLogsBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsBucketPolicyPolicyDenyStatement0, CloudFrontLogsBucketPolicyPolicyAllowStatement1]


class CloudFrontLogsBucketPolicyPolicy(s3.BucketPolicy):
    bucket = CloudFrontLogsBucket
    policy_document = CloudFrontLogsBucketPolicyPolicyPolicyDocument


class ContentReplicaBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class ContentReplicaBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentReplicaBucketServerSideEncryptionByDefault


class ContentReplicaBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [ContentReplicaBucketServerSideEncryptionRule]


class ContentReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ContentReplicaBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class ContentReplicaBucket(s3.Bucket):
    bucket_encryption = ContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = ContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentReplicaBucketDeleteMarkerReplication


class ContentLogBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class ContentLogBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentLogBucketServerSideEncryptionByDefault


class ContentLogBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [ContentLogBucketServerSideEncryptionRule]


class ContentLogBucketDefaultRetention:
    resource: s3.Bucket.DefaultRetention
    mode = 'COMPLIANCE'
    years = 1


class ContentLogBucketObjectLockRule:
    resource: s3.Bucket.ObjectLockRule
    default_retention = ContentLogBucketDefaultRetention


class ContentLogBucketObjectLockConfiguration:
    resource: s3.Bucket.ObjectLockConfiguration
    object_lock_enabled = 'Enabled'
    rule = ContentLogBucketObjectLockRule


class ContentLogBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ContentLogBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class ContentLogBucket(s3.Bucket):
    bucket_encryption = ContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = ContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = ContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentLogBucketDeleteMarkerReplication


class ContentBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class ContentBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentBucketServerSideEncryptionByDefault


class ContentBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [ContentBucketServerSideEncryptionRule]


class ContentBucketLoggingConfiguration:
    resource: s3.Bucket.LoggingConfiguration
    destination_bucket_name = ContentLogBucket


class ContentBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ContentBucketReplicationDestination:
    resource: s3.Bucket.ReplicationDestination
    bucket = ContentReplicaBucket.Arn


class ContentBucketReplicationRule:
    resource: s3.Bucket.ReplicationRule
    destination = ContentBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class ContentBucketReplicationConfiguration:
    resource: s3.Bucket.ReplicationConfiguration
    role = ContentReplicationRole.Arn
    rules = [ContentBucketReplicationRule]


class ContentBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class ContentBucket(s3.Bucket):
    bucket_encryption = ContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ContentBucketPublicAccessBlockConfiguration
    replication_configuration = ContentBucketReplicationConfiguration
    versioning_configuration = ContentBucketDeleteMarkerReplication


class ContentReplicaBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
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


class ContentReplicaBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
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


class ContentReplicaBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentReplicaBucketPolicyPolicyDenyStatement0, ContentReplicaBucketPolicyPolicyAllowStatement1]


class ContentReplicaBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ContentReplicaBucket
    policy_document = ContentReplicaBucketPolicyPolicyPolicyDocument


class CloudFrontLogsLogBucketPolicyPolicyDenyStatement0:
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


class CloudFrontLogsLogBucketPolicyPolicyAllowStatement1:
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


class CloudFrontLogsLogBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsLogBucketPolicyPolicyDenyStatement0, CloudFrontLogsLogBucketPolicyPolicyAllowStatement1]


class CloudFrontLogsLogBucketPolicyPolicy(s3.BucketPolicy):
    bucket = CloudFrontLogsLogBucket
    policy_document = CloudFrontLogsLogBucketPolicyPolicyPolicyDocument


class ContentLogBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
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


class ContentLogBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
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


class ContentLogBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentLogBucketPolicyPolicyDenyStatement0, ContentLogBucketPolicyPolicyAllowStatement1]


class ContentLogBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ContentLogBucket
    policy_document = ContentLogBucketPolicyPolicyPolicyDocument


class CloudFrontLogsLogBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class CloudFrontLogsLogBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsLogBucketServerSideEncryptionByDefault


class CloudFrontLogsLogBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsLogBucketServerSideEncryptionRule]


class CloudFrontLogsLogBucketDefaultRetention:
    resource: s3.Bucket.DefaultRetention
    mode = 'COMPLIANCE'
    years = 1


class CloudFrontLogsLogBucketObjectLockRule:
    resource: s3.Bucket.ObjectLockRule
    default_retention = CloudFrontLogsLogBucketDefaultRetention


class CloudFrontLogsLogBucketObjectLockConfiguration:
    resource: s3.Bucket.ObjectLockConfiguration
    object_lock_enabled = 'Enabled'
    rule = CloudFrontLogsLogBucketObjectLockRule


class CloudFrontLogsLogBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class CloudFrontLogsLogBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsLogBucket(s3.Bucket):
    bucket_encryption = CloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = CloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = CloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsLogBucketDeleteMarkerReplication


class CloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class CloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsReplicaBucketServerSideEncryptionByDefault


class CloudFrontLogsReplicaBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsReplicaBucketServerSideEncryptionRule]


class CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class CloudFrontLogsReplicaBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsReplicaBucket(s3.Bucket):
    bucket_encryption = CloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsReplicaBucketDeleteMarkerReplication


class CloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class CloudFrontLogsBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsBucketServerSideEncryptionByDefault


class CloudFrontLogsBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsBucketServerSideEncryptionRule]


class CloudFrontLogsBucketLoggingConfiguration:
    resource: s3.Bucket.LoggingConfiguration
    destination_bucket_name = CloudFrontLogsLogBucket


class CloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class CloudFrontLogsBucketReplicationDestination:
    resource: s3.Bucket.ReplicationDestination
    bucket = CloudFrontLogsReplicaBucket.Arn


class CloudFrontLogsBucketReplicationRule:
    resource: s3.Bucket.ReplicationRule
    destination = CloudFrontLogsBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsBucketReplicationConfiguration:
    resource: s3.Bucket.ReplicationConfiguration
    role = CloudFrontLogsReplicationRole.Arn
    rules = [CloudFrontLogsBucketReplicationRule]


class CloudFrontLogsBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class CloudFrontLogsBucket(s3.Bucket):
    bucket_encryption = CloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = CloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = CloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = CloudFrontLogsBucketDeleteMarkerReplication


class ContentBucketPolicyPolicyDenyStatement0:
    resource: DenyStatement
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


class ContentBucketPolicyPolicyAllowStatement1:
    resource: PolicyStatement
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


class ContentBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentBucketPolicyPolicyDenyStatement0, ContentBucketPolicyPolicyAllowStatement1]


class ContentBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ContentBucket
    policy_document = ContentBucketPolicyPolicyPolicyDocument


class CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0:
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


class CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1:
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


class CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0, CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1]


class CloudFrontLogsReplicaBucketPolicyPolicy(s3.BucketPolicy):
    bucket = CloudFrontLogsReplicaBucket
    policy_document = CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument
