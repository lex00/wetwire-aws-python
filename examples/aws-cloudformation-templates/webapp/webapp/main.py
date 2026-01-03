"""Stack resources."""

from . import *  # noqa: F403


class RestApi:
    resource: apigateway.RestApi
    name = AppName


class JwtResourceResource:
    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'jwt'
    rest_api_id = RestApi


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


class RestApiDeployment:
    resource: apigateway.Deployment
    rest_api_id = RestApi
    depends_on = [TestResourceGet, TestResourceOptions, JwtResourceGet, JwtResourceOptions]


class RestApiStage:
    resource: apigateway.Stage
    rest_api_id = RestApi
    deployment_id = RestApiDeployment
    stage_name = 'prod'
