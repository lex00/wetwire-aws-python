"""Storage resources: StorageLogBucket, StorageLogBucketPolicyPolicy, StorageReplicaBucket, StorageBucket, StorageReplicaBucketPolicyPolicy, StorageBucketPolicyPolicy."""

from . import *  # noqa: F403


class StorageLogBucketServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AES256


class StorageLogBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = StorageLogBucketServerSideEncryptionByDefault


class StorageLogBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [StorageLogBucketServerSideEncryptionRule]


class StorageLogBucketDefaultRetention(s3.Bucket.DefaultRetention):
    mode = 'COMPLIANCE'
    years = 1


class StorageLogBucketObjectLockRule(s3.Bucket.ObjectLockRule):
    default_retention = StorageLogBucketDefaultRetention


class StorageLogBucketObjectLockConfiguration(s3.Bucket.ObjectLockConfiguration):
    object_lock_enabled = 'Enabled'
    rule = StorageLogBucketObjectLockRule


class StorageLogBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class StorageLogBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class StorageLogBucket(s3.Bucket):
    resource: s3.Bucket
    bucket_encryption = StorageLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = StorageLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = StorageLogBucketPublicAccessBlockConfiguration
    versioning_configuration = StorageLogBucketDeleteMarkerReplication


class StorageLogBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class StorageLogBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class StorageLogBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [StorageLogBucketPolicyPolicyDenyStatement0, StorageLogBucketPolicyPolicyAllowStatement1]


class StorageLogBucketPolicyPolicy(s3.BucketPolicy):
    resource: s3.BucketPolicy
    bucket = StorageLogBucket
    policy_document = StorageLogBucketPolicyPolicyPolicyDocument


class StorageReplicaBucketServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AES256


class StorageReplicaBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = StorageReplicaBucketServerSideEncryptionByDefault


class StorageReplicaBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [StorageReplicaBucketServerSideEncryptionRule]


class StorageReplicaBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class StorageReplicaBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class StorageReplicaBucket(s3.Bucket):
    resource: s3.Bucket
    bucket_encryption = StorageReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = StorageReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = StorageReplicaBucketDeleteMarkerReplication


class StorageBucketServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AES256


class StorageBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = StorageBucketServerSideEncryptionByDefault


class StorageBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [StorageBucketServerSideEncryptionRule]


class StorageBucketLoggingConfiguration(s3.Bucket.LoggingConfiguration):
    destination_bucket_name = StorageLogBucket


class StorageBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class StorageBucketReplicationDestination(s3.Bucket.ReplicationDestination):
    bucket = StorageReplicaBucket.Arn


class StorageBucketReplicationRule(s3.Bucket.ReplicationRule):
    destination = StorageBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class StorageBucketReplicationConfiguration(s3.Bucket.ReplicationConfiguration):
    role = StorageReplicationRole.Arn
    rules = [StorageBucketReplicationRule]


class StorageBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class StorageBucket(s3.Bucket):
    resource: s3.Bucket
    bucket_encryption = StorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = StorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = StorageBucketPublicAccessBlockConfiguration
    replication_configuration = StorageBucketReplicationConfiguration
    versioning_configuration = StorageBucketDeleteMarkerReplication


class StorageReplicaBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class StorageReplicaBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class StorageReplicaBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [StorageReplicaBucketPolicyPolicyDenyStatement0, StorageReplicaBucketPolicyPolicyAllowStatement1]


class StorageReplicaBucketPolicyPolicy(s3.BucketPolicy):
    resource: s3.BucketPolicy
    bucket = StorageReplicaBucket
    policy_document = StorageReplicaBucketPolicyPolicyPolicyDocument


class StorageBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class StorageBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class StorageBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [StorageBucketPolicyPolicyDenyStatement0, StorageBucketPolicyPolicyAllowStatement1]


class StorageBucketPolicyPolicy(s3.BucketPolicy):
    resource: s3.BucketPolicy
    bucket = StorageBucket
    policy_document = StorageBucketPolicyPolicyPolicyDocument
