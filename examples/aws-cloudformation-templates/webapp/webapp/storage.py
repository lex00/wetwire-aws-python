"""Storage resources: SiteContentReplicaBucket, SiteContentLogBucket, SiteContentBucket, SiteCloudFrontLogsLogBucket, SiteCloudFrontLogsReplicaBucket, SiteCloudFrontLogsBucket, SiteContentLogBucketAccessPolicy, SiteCloudFrontLogsLogBucketAccessPolicy, SiteContentReplicaBucketAccessPolicy, SiteContentBucketAccessPolicy, SiteCloudFrontLogsReplicaBucketAccessPolicy, SiteCloudFrontLogsBucketAccessPolicy."""

from . import *  # noqa: F403


class SiteContentReplicaBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteContentReplicaBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = SiteContentReplicaBucketMetadataTableEncryptionConfiguration


class SiteContentReplicaBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [SiteContentReplicaBucketServerSideEncryptionRule]


class SiteContentReplicaBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteContentReplicaBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentReplicaBucket(s3.Bucket):
    bucket_encryption = SiteContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentReplicaBucketDeleteMarkerReplication


class SiteContentLogBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteContentLogBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = SiteContentLogBucketMetadataTableEncryptionConfiguration


class SiteContentLogBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [SiteContentLogBucketServerSideEncryptionRule]


class SiteContentLogBucketDefaultRetention(s3.Bucket.DefaultRetention):
    mode = 'COMPLIANCE'
    years = 1


class SiteContentLogBucketObjectLockRule(s3.Bucket.ObjectLockRule):
    default_retention = SiteContentLogBucketDefaultRetention


class SiteContentLogBucketObjectLockConfiguration(s3.Bucket.ObjectLockConfiguration):
    object_lock_enabled = 'Enabled'
    rule = SiteContentLogBucketObjectLockRule


class SiteContentLogBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteContentLogBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentLogBucket(s3.Bucket):
    bucket_encryption = SiteContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentLogBucketDeleteMarkerReplication


class SiteContentBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteContentBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = SiteContentBucketMetadataTableEncryptionConfiguration


class SiteContentBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [SiteContentBucketServerSideEncryptionRule]


class SiteContentBucketLoggingConfiguration(s3.Bucket.LoggingConfiguration):
    destination_bucket_name = SiteContentLogBucket


class SiteContentBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteContentBucketReplicationDestination(s3.Bucket.ReplicationDestination):
    bucket = SiteContentReplicaBucket.Arn


class SiteContentBucketReplicationRule(s3.Bucket.ReplicationRule):
    destination = SiteContentBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentBucketReplicationConfiguration(s3.Bucket.ReplicationConfiguration):
    role = SiteContentReplicationRole.Arn
    rules = [SiteContentBucketReplicationRule]


class SiteContentBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentBucket(s3.Bucket):
    bucket_encryption = SiteContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteContentBucketPublicAccessBlockConfiguration
    replication_configuration = SiteContentBucketReplicationConfiguration
    versioning_configuration = SiteContentBucketDeleteMarkerReplication


class SiteCloudFrontLogsLogBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteCloudFrontLogsLogBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = SiteCloudFrontLogsLogBucketMetadataTableEncryptionConfiguration


class SiteCloudFrontLogsLogBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [SiteCloudFrontLogsLogBucketServerSideEncryptionRule]


class SiteCloudFrontLogsLogBucketDefaultRetention(s3.Bucket.DefaultRetention):
    mode = 'COMPLIANCE'
    years = 1


class SiteCloudFrontLogsLogBucketObjectLockRule(s3.Bucket.ObjectLockRule):
    default_retention = SiteCloudFrontLogsLogBucketDefaultRetention


class SiteCloudFrontLogsLogBucketObjectLockConfiguration(s3.Bucket.ObjectLockConfiguration):
    object_lock_enabled = 'Enabled'
    rule = SiteCloudFrontLogsLogBucketObjectLockRule


class SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteCloudFrontLogsLogBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsLogBucket(s3.Bucket):
    bucket_encryption = SiteCloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteCloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsLogBucketDeleteMarkerReplication


class SiteCloudFrontLogsReplicaBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = SiteCloudFrontLogsReplicaBucketMetadataTableEncryptionConfiguration


class SiteCloudFrontLogsReplicaBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule]


class SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsReplicaBucket(s3.Bucket):
    bucket_encryption = SiteCloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication


class SiteCloudFrontLogsBucketMetadataTableEncryptionConfiguration(s3.Bucket.MetadataTableEncryptionConfiguration):
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteCloudFrontLogsBucketServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = SiteCloudFrontLogsBucketMetadataTableEncryptionConfiguration


class SiteCloudFrontLogsBucketBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [SiteCloudFrontLogsBucketServerSideEncryptionRule]


class SiteCloudFrontLogsBucketLoggingConfiguration(s3.Bucket.LoggingConfiguration):
    destination_bucket_name = SiteCloudFrontLogsLogBucket


class SiteCloudFrontLogsBucketPublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteCloudFrontLogsBucketReplicationDestination(s3.Bucket.ReplicationDestination):
    bucket = SiteCloudFrontLogsReplicaBucket.Arn


class SiteCloudFrontLogsBucketReplicationRule(s3.Bucket.ReplicationRule):
    destination = SiteCloudFrontLogsBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsBucketReplicationConfiguration(s3.Bucket.ReplicationConfiguration):
    role = SiteCloudFrontLogsReplicationRole.Arn
    rules = [SiteCloudFrontLogsBucketReplicationRule]


class SiteCloudFrontLogsBucketDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsBucketOwnershipControlsRule(s3.Bucket.OwnershipControlsRule):
    object_ownership = 'BucketOwnerPreferred'


class SiteCloudFrontLogsBucketOwnershipControls(s3.Bucket.OwnershipControls):
    rules = [SiteCloudFrontLogsBucketOwnershipControlsRule]


class SiteCloudFrontLogsBucket(s3.Bucket):
    bucket_encryption = SiteCloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteCloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = SiteCloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = SiteCloudFrontLogsBucketDeleteMarkerReplication
    ownership_controls = SiteCloudFrontLogsBucketOwnershipControls


class SiteContentLogBucketAccessPolicyDenyStatement0(DenyStatement):
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


class SiteContentLogBucketAccessPolicyAllowStatement1(PolicyStatement):
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


class SiteContentLogBucketAccessPolicyPolicyDocument(PolicyDocument):
    statement = [SiteContentLogBucketAccessPolicyDenyStatement0, SiteContentLogBucketAccessPolicyAllowStatement1]


class SiteContentLogBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteContentLogBucket
    policy_document = SiteContentLogBucketAccessPolicyPolicyDocument


class SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0(DenyStatement):
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


class SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1(PolicyStatement):
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


class SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument(PolicyDocument):
    statement = [SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1]


class SiteCloudFrontLogsLogBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteCloudFrontLogsLogBucket
    policy_document = SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument


class SiteContentReplicaBucketAccessPolicyDenyStatement0(DenyStatement):
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


class SiteContentReplicaBucketAccessPolicyAllowStatement1(PolicyStatement):
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


class SiteContentReplicaBucketAccessPolicyPolicyDocument(PolicyDocument):
    statement = [SiteContentReplicaBucketAccessPolicyDenyStatement0, SiteContentReplicaBucketAccessPolicyAllowStatement1]


class SiteContentReplicaBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteContentReplicaBucket
    policy_document = SiteContentReplicaBucketAccessPolicyPolicyDocument


class SiteContentBucketAccessPolicyAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'cloudfront.amazonaws.com',
    }
    action = 's3:GetObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')
    condition = {
        STRING_EQUALS: {
            'AWS:SourceArn': Sub('arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SiteDistribution.Id}'),
        },
    }


class SiteContentBucketAccessPolicyDenyStatement1(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class SiteContentBucketAccessPolicyAllowStatement2(PolicyStatement):
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class SiteContentBucketAccessPolicyPolicyDocument(PolicyDocument):
    statement = [SiteContentBucketAccessPolicyAllowStatement0, SiteContentBucketAccessPolicyDenyStatement1, SiteContentBucketAccessPolicyAllowStatement2]


class SiteContentBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteContentBucket
    policy_document = SiteContentBucketAccessPolicyPolicyDocument


class SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0(DenyStatement):
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


class SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1(PolicyStatement):
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


class SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument(PolicyDocument):
    statement = [SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1]


class SiteCloudFrontLogsReplicaBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteCloudFrontLogsReplicaBucket
    policy_document = SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument


class SiteCloudFrontLogsBucketAccessPolicyDenyStatement0(DenyStatement):
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


class SiteCloudFrontLogsBucketAccessPolicyAllowStatement1(PolicyStatement):
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


class SiteCloudFrontLogsBucketAccessPolicyPolicyDocument(PolicyDocument):
    statement = [SiteCloudFrontLogsBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsBucketAccessPolicyAllowStatement1]


class SiteCloudFrontLogsBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteCloudFrontLogsBucket
    policy_document = SiteCloudFrontLogsBucketAccessPolicyPolicyDocument
