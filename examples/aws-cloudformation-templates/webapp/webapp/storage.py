"""Storage resources: SiteCloudFrontLogsReplicaBucket, SiteCloudFrontLogsLogBucket, SiteCloudFrontLogsBucket, SiteContentLogBucket, SiteContentReplicaBucket, SiteContentBucket, SiteCloudFrontLogsLogBucketAccessPolicy, SiteContentLogBucketAccessPolicy, SiteCloudFrontLogsBucketAccessPolicy, SiteContentBucketAccessPolicy, SiteCloudFrontLogsReplicaBucketAccessPolicy, SiteContentReplicaBucketAccessPolicy."""

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


class SiteCloudFrontLogsReplicaBucket(s3.Bucket):
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


class SiteCloudFrontLogsLogBucket(s3.Bucket):
    bucket_encryption = SiteCloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteCloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsLogBucketDeleteMarkerReplication


class SiteCloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteCloudFrontLogsBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsBucketServerSideEncryptionByDefault


class SiteCloudFrontLogsBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsBucketServerSideEncryptionRule]


class SiteCloudFrontLogsBucketLoggingConfiguration:
    resource: s3.Bucket.LoggingConfiguration
    destination_bucket_name = SiteCloudFrontLogsLogBucket


class SiteCloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteCloudFrontLogsBucketReplicationDestination:
    resource: s3.Bucket.ReplicationDestination
    bucket = SiteCloudFrontLogsReplicaBucket.Arn


class SiteCloudFrontLogsBucketReplicationRule:
    resource: s3.Bucket.ReplicationRule
    destination = SiteCloudFrontLogsBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsBucketReplicationConfiguration:
    resource: s3.Bucket.ReplicationConfiguration
    role = SiteCloudFrontLogsReplicationRole.Arn
    rules = [SiteCloudFrontLogsBucketReplicationRule]


class SiteCloudFrontLogsBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class SiteCloudFrontLogsBucketOwnershipControlsRule:
    resource: s3.Bucket.OwnershipControlsRule
    object_ownership = 'BucketOwnerPreferred'


class SiteCloudFrontLogsBucketOwnershipControls:
    resource: s3.Bucket.OwnershipControls
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


class SiteContentLogBucket(s3.Bucket):
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


class SiteContentReplicaBucket(s3.Bucket):
    bucket_encryption = SiteContentReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteContentReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentReplicaBucketDeleteMarkerReplication


class SiteContentBucketServerSideEncryptionByDefault:
    resource: s3.Bucket.ServerSideEncryptionByDefault
    sse_algorithm = s3.ServerSideEncryption.AES256


class SiteContentBucketServerSideEncryptionRule:
    resource: s3.Bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentBucketServerSideEncryptionByDefault


class SiteContentBucketBucketEncryption:
    resource: s3.Bucket.BucketEncryption
    server_side_encryption_configuration = [SiteContentBucketServerSideEncryptionRule]


class SiteContentBucketLoggingConfiguration:
    resource: s3.Bucket.LoggingConfiguration
    destination_bucket_name = SiteContentLogBucket


class SiteContentBucketPublicAccessBlockConfiguration:
    resource: s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class SiteContentBucketReplicationDestination:
    resource: s3.Bucket.ReplicationDestination
    bucket = SiteContentReplicaBucket.Arn


class SiteContentBucketReplicationRule:
    resource: s3.Bucket.ReplicationRule
    destination = SiteContentBucketReplicationDestination
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentBucketReplicationConfiguration:
    resource: s3.Bucket.ReplicationConfiguration
    role = SiteContentReplicationRole.Arn
    rules = [SiteContentBucketReplicationRule]


class SiteContentBucketDeleteMarkerReplication:
    resource: s3.Bucket.DeleteMarkerReplication
    status = s3.BucketVersioningStatus.ENABLED


class SiteContentBucket(s3.Bucket):
    bucket_encryption = SiteContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteContentBucketPublicAccessBlockConfiguration
    replication_configuration = SiteContentBucketReplicationConfiguration
    versioning_configuration = SiteContentBucketDeleteMarkerReplication


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


class SiteCloudFrontLogsLogBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteCloudFrontLogsLogBucket
    policy_document = SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument


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


class SiteContentLogBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteContentLogBucket
    policy_document = SiteContentLogBucketAccessPolicyPolicyDocument


class SiteCloudFrontLogsBucketAccessPolicyDenyStatement0:
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


class SiteCloudFrontLogsBucketAccessPolicyAllowStatement1:
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


class SiteCloudFrontLogsBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsBucketAccessPolicyDenyStatement0, SiteCloudFrontLogsBucketAccessPolicyAllowStatement1]


class SiteCloudFrontLogsBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteCloudFrontLogsBucket
    policy_document = SiteCloudFrontLogsBucketAccessPolicyPolicyDocument


class SiteContentBucketAccessPolicyAllowStatement0:
    resource: PolicyStatement
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


class SiteContentBucketAccessPolicyDenyStatement1:
    resource: DenyStatement
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


class SiteContentBucketAccessPolicyAllowStatement2:
    resource: PolicyStatement
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


class SiteContentBucketAccessPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentBucketAccessPolicyAllowStatement0, SiteContentBucketAccessPolicyDenyStatement1, SiteContentBucketAccessPolicyAllowStatement2]


class SiteContentBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteContentBucket
    policy_document = SiteContentBucketAccessPolicyPolicyDocument


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


class SiteCloudFrontLogsReplicaBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteCloudFrontLogsReplicaBucket
    policy_document = SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument


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


class SiteContentReplicaBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteContentReplicaBucket
    policy_document = SiteContentReplicaBucketAccessPolicyPolicyDocument
