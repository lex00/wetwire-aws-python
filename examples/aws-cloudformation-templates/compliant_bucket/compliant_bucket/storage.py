"""Storage resources: ObjectStorageLogBucket, ObjectStorageReplicaBucket, ObjectStorageReplicaBucketPolicyPolicy, ObjectStorageLogBucketPolicyPolicy, ObjectStorageBucket, ObjectStorageBucketPolicyPolicy."""

from . import *  # noqa: F403


class ObjectStorageLogBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class ObjectStorageLogBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = ObjectStorageLogBucketMetadataTableEncryptionConfiguration


class ObjectStorageLogBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [ObjectStorageLogBucketServerSideEncryptionRule]


class ObjectStorageLogBucketDefaultRetention(s3.Bucket.DefaultRetention):
    mode = 'COMPLIANCE'
    years = 1


class ObjectStorageLogBucketObjectLockRule(s3.Bucket.ObjectLockRule):
    default_retention = ObjectStorageLogBucketDefaultRetention


class ObjectStorageLogBucketObjectLockConfiguration(s3.Bucket.ObjectLockConfiguration):
    object_lock_enabled = 'Enabled'
    rule = ObjectStorageLogBucketObjectLockRule


class ObjectStorageLogBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ObjectStorageLogBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class ObjectStorageLogBucket(s3.Bucket):
    bucket_encryption = ObjectStorageLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = ObjectStorageLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = ObjectStorageLogBucketPublicAccessBlockConfiguration
    versioning_configuration = ObjectStorageLogBucketDeleteMarkerReplication


class ObjectStorageReplicaBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class ObjectStorageReplicaBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = ObjectStorageReplicaBucketMetadataTableEncryptionConfiguration


class ObjectStorageReplicaBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [ObjectStorageReplicaBucketServerSideEncryptionRule]


class ObjectStorageReplicaBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ObjectStorageReplicaBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class ObjectStorageReplicaBucket(s3.Bucket):
    bucket_encryption = ObjectStorageReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = ObjectStorageReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = ObjectStorageReplicaBucketDeleteMarkerReplication


class ObjectStorageReplicaBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class ObjectStorageReplicaBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class ObjectStorageReplicaBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [ObjectStorageReplicaBucketPolicyPolicyDenyStatement0, ObjectStorageReplicaBucketPolicyPolicyAllowStatement1]


class ObjectStorageReplicaBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ObjectStorageReplicaBucket
    policy_document = ObjectStorageReplicaBucketPolicyPolicyPolicyDocument


class ObjectStorageLogBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class ObjectStorageLogBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class ObjectStorageLogBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [ObjectStorageLogBucketPolicyPolicyDenyStatement0, ObjectStorageLogBucketPolicyPolicyAllowStatement1]


class ObjectStorageLogBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ObjectStorageLogBucket
    policy_document = ObjectStorageLogBucketPolicyPolicyPolicyDocument


class ObjectStorageBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class ObjectStorageBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = ObjectStorageBucketMetadataTableEncryptionConfiguration


class ObjectStorageBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [ObjectStorageBucketServerSideEncryptionRule]


class ObjectStorageBucketLoggingConfiguration(s3.Bucket.LoggingConfiguration):
    destination_bucket_name = ObjectStorageLogBucket


class ObjectStorageBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class ObjectStorageBucketReplicationDestination(s3.Bucket.ReplicationDestination):
    bucket = ObjectStorageReplicaBucket.Arn


class ObjectStorageBucketReplicationRule(s3.Bucket.ReplicationRule):
    destination = ObjectStorageBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class ObjectStorageBucketReplicationConfiguration(s3.Bucket.ReplicationConfiguration):
    role = ObjectStorageReplicationRole.Arn
    rules = [ObjectStorageBucketReplicationRule]


class ObjectStorageBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class ObjectStorageBucket(s3.Bucket):
    bucket_encryption = ObjectStorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ObjectStorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ObjectStorageBucketPublicAccessBlockConfiguration
    replication_configuration = ObjectStorageBucketReplicationConfiguration
    versioning_configuration = ObjectStorageBucketDeleteMarkerReplication


class ObjectStorageBucketPolicyPolicyDenyStatement0(DenyStatement):
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


class ObjectStorageBucketPolicyPolicyAllowStatement1(PolicyStatement):
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


class ObjectStorageBucketPolicyPolicyPolicyDocument(PolicyDocument):
    statement = [ObjectStorageBucketPolicyPolicyDenyStatement0, ObjectStorageBucketPolicyPolicyAllowStatement1]


class ObjectStorageBucketPolicyPolicy(s3.BucketPolicy):
    bucket = ObjectStorageBucket
    policy_document = ObjectStorageBucketPolicyPolicyPolicyDocument
