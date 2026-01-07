"""Storage resources: S3BucketSource."""

from . import *  # noqa: F403


class S3BucketSourceServerSideEncryptionByDefault(s3.Bucket.ServerSideEncryptionByDefault):
    sse_algorithm = s3.ServerSideEncryption.AWSKMS
    kms_master_key_id = KmsKey


class S3BucketSourceServerSideEncryptionRule(s3.Bucket.ServerSideEncryptionRule):
    server_side_encryption_by_default = S3BucketSourceServerSideEncryptionByDefault
    bucket_key_enabled = True


class S3BucketSourceBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [S3BucketSourceServerSideEncryptionRule]


class S3BucketSourcePublicAccessBlockConfiguration(s3.MultiRegionAccessPoint.PublicAccessBlockConfiguration):
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


class S3BucketSourceDeleteMarkerReplication(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class S3BucketSourceEncryptionConfiguration(s3.Bucket.EncryptionConfiguration):
    replica_kms_key_id = Sub('arn:${AWS::Partition}:kms:${AWS::Region}:${AccountIdDestination}:alias/${AWS::StackName}-${AccountIdDestination}-kms-key')


class S3BucketSourceAccessControlTranslation(s3.Bucket.AccessControlTranslation):
    owner = 'Destination'


class S3BucketSourceReplicationDestination(s3.Bucket.ReplicationDestination):
    account = AccountIdDestination
    bucket = Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AccountIdDestination}-bucket')
    encryption_configuration = S3BucketSourceEncryptionConfiguration
    access_control_translation = S3BucketSourceAccessControlTranslation


class S3BucketSourceReplicationRuleAndOperator(s3.Bucket.ReplicationRuleAndOperator):
    prefix = ''


class S3BucketSourceDeleteMarkerReplication1(s3.Bucket.DeleteMarkerReplication):
    status = 'Disabled'


class S3BucketSourceDeleteMarkerReplication2(s3.Bucket.DeleteMarkerReplication):
    status = s3.BucketVersioningStatus.ENABLED


class S3BucketSourceSourceSelectionCriteria(s3.Bucket.SourceSelectionCriteria):
    sse_kms_encrypted_objects = S3BucketSourceDeleteMarkerReplication2


class S3BucketSourceReplicationRule(s3.Bucket.ReplicationRule):
    id = 'Rule1'
    priority = 0
    status = s3.BucketVersioningStatus.ENABLED
    destination = S3BucketSourceReplicationDestination
    filter = S3BucketSourceReplicationRuleAndOperator
    delete_marker_replication = S3BucketSourceDeleteMarkerReplication1
    source_selection_criteria = S3BucketSourceSourceSelectionCriteria


class S3BucketSourceReplicationConfiguration(s3.Bucket.ReplicationConfiguration):
    role = ReplicationRole.Arn
    rules = [S3BucketSourceReplicationRule]


class S3BucketSource(s3.Bucket):
    bucket_name = Sub('${AWS::StackName}-${AWS::AccountId}-bucket')
    bucket_encryption = S3BucketSourceBucketEncryption
    public_access_block_configuration = S3BucketSourcePublicAccessBlockConfiguration
    versioning_configuration = S3BucketSourceDeleteMarkerReplication
    replication_configuration = S3BucketSourceReplicationConfiguration
    deletion_policy = 'Delete'
