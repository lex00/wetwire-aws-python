"""Stack resources."""

from . import *  # noqa: F403


class RestApi:
    resource: apigateway.RestApi
    name = AppName


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


class SiteCloudFrontLogsBucket:
    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteCloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = SiteCloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = SiteCloudFrontLogsBucketDeleteMarkerReplication
    ownership_controls = SiteCloudFrontLogsBucketOwnershipControls


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


class SiteContentBucket:
    resource: s3.Bucket
    bucket_encryption = SiteContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteContentBucketPublicAccessBlockConfiguration
    replication_configuration = SiteContentBucketReplicationConfiguration
    versioning_configuration = SiteContentBucketDeleteMarkerReplication


class SiteDistributionDefaultCacheBehavior:
    resource: cloudfront.Distribution.DefaultCacheBehavior
    cache_policy_id = '658327ea-f89d-4fab-a63d-7e88639e58f6'
    compress = True
    target_origin_id = Sub('${AppName}-origin-1')
    viewer_protocol_policy = 'redirect-to-https'


class SiteDistributionLogging:
    resource: cloudfront.Distribution.Logging
    bucket = SiteCloudFrontLogsBucket.RegionalDomainName


class SiteDistributionS3OriginConfig:
    resource: cloudfront.Distribution.S3OriginConfig
    origin_access_identity = ''


class SiteDistributionOrigin:
    resource: cloudfront.Distribution.Origin
    domain_name = SiteContentBucket.RegionalDomainName
    id = Sub('${AppName}-origin-1')
    origin_access_control_id = SiteOriginAccessControl.Id
    s3_origin_config = SiteDistributionS3OriginConfig


class SiteDistributionViewerCertificate:
    resource: cloudfront.Distribution.ViewerCertificate
    cloud_front_default_certificate = True


class SiteDistributionDistributionConfig:
    resource: cloudfront.Distribution.DistributionConfig
    default_cache_behavior = SiteDistributionDefaultCacheBehavior
    default_root_object = 'index.html'
    enabled = True
    http_version = 'http2'
    ipv6_enabled = True
    logging = SiteDistributionLogging
    origins = [SiteDistributionOrigin]
    viewer_certificate = SiteDistributionViewerCertificate
    web_acl_id = SiteWebACL.Arn


class SiteDistribution:
    resource: cloudfront.Distribution
    distribution_config = SiteDistributionDistributionConfig


class RestApiAuthorizer:
    resource: apigateway.Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [CognitoUserPool.Arn]
    rest_api_id = RestApi
    type_ = 'COGNITO_USER_POOLS'


class TestResourceResource:
    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'test'
    rest_api_id = RestApi


class TestResourceOptionsIntegration:
    resource: apigateway.Method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


class TestResourceOptions:
    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = TestResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    integration = TestResourceOptionsIntegration


class JwtResourceResource:
    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'jwt'
    rest_api_id = RestApi


class JwtResourceGetIntegration:
    resource: apigateway.Method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


class JwtResourceGet:
    resource: apigateway.Method
    http_method = 'GET'
    resource_id = JwtResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    authorizer_id = 'AWS::NoValue'
    integration = JwtResourceGetIntegration


class JwtResourceOptionsIntegration:
    resource: apigateway.Method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


class JwtResourceOptions:
    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = JwtResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    integration = JwtResourceOptionsIntegration


class TestResourceGetIntegration:
    resource: apigateway.Method.Integration
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


class TestResourceGet:
    resource: apigateway.Method
    http_method = 'GET'
    resource_id = TestResourceResource
    rest_api_id = RestApi
    authorization_type = 'COGNITO_USER_POOLS'
    authorizer_id = RestApiAuthorizer
    integration = TestResourceGetIntegration


class RestApiDeployment:
    resource: apigateway.Deployment
    rest_api_id = RestApi
    depends_on = [TestResourceGet, TestResourceOptions, JwtResourceGet, JwtResourceOptions]


class RestApiStage:
    resource: apigateway.Stage
    rest_api_id = RestApi
    deployment_id = RestApiDeployment
    stage_name = 'prod'


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


class SiteCloudFrontLogsBucketAccessPolicy:
    resource: s3.BucketPolicy
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


class SiteContentBucketAccessPolicy:
    resource: s3.BucketPolicy
    bucket = SiteContentBucket
    policy_document = SiteContentBucketAccessPolicyPolicyDocument
