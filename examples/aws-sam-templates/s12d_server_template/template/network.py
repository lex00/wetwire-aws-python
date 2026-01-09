"""Network resources: CloudFrontCachePolicyAPI, CloudFrontCachePolicyDefault, CloudFrontLogDistro, CloudFrontCachePolicyClient, CloudFrontDistro."""

from . import *  # noqa: F403


class CloudFrontCachePolicyAPICookiesConfig(cloudfront.CachePolicy.CookiesConfig):
    cookie_behavior = 'none'


class CloudFrontCachePolicyAPIHeadersConfig(cloudfront.CachePolicy.HeadersConfig):
    header_behavior = 'whitelist'
    headers = ['Authorization']


class CloudFrontCachePolicyAPIQueryStringsConfig(cloudfront.CachePolicy.QueryStringsConfig):
    query_string_behavior = 'all'


class CloudFrontCachePolicyAPIParametersInCacheKeyAndForwardedToOrigin(cloudfront.CachePolicy.ParametersInCacheKeyAndForwardedToOrigin):
    cookies_config = CloudFrontCachePolicyAPICookiesConfig
    enable_accept_encoding_brotli = True
    enable_accept_encoding_gzip = True
    headers_config = CloudFrontCachePolicyAPIHeadersConfig
    query_strings_config = CloudFrontCachePolicyAPIQueryStringsConfig


class CloudFrontCachePolicyAPICachePolicyConfig(cloudfront.CachePolicy.CachePolicyConfig):
    default_ttl = 30
    min_ttl = 0
    max_ttl = 60
    name = Sub('${AppName}-API')
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyAPIParametersInCacheKeyAndForwardedToOrigin


class CloudFrontCachePolicyAPI(cloudfront.CachePolicy):
    cache_policy_config = CloudFrontCachePolicyAPICachePolicyConfig


class CloudFrontCachePolicyDefaultCookiesConfig(cloudfront.CachePolicy.CookiesConfig):
    cookie_behavior = 'none'


class CloudFrontCachePolicyDefaultHeadersConfig(cloudfront.CachePolicy.HeadersConfig):
    header_behavior = 'none'


class CloudFrontCachePolicyDefaultQueryStringsConfig(cloudfront.CachePolicy.QueryStringsConfig):
    query_string_behavior = 'none'


class CloudFrontCachePolicyDefaultParametersInCacheKeyAndForwardedToOrigin(cloudfront.CachePolicy.ParametersInCacheKeyAndForwardedToOrigin):
    cookies_config = CloudFrontCachePolicyDefaultCookiesConfig
    enable_accept_encoding_brotli = True
    enable_accept_encoding_gzip = True
    headers_config = CloudFrontCachePolicyDefaultHeadersConfig
    query_strings_config = CloudFrontCachePolicyDefaultQueryStringsConfig


class CloudFrontCachePolicyDefaultCachePolicyConfig(cloudfront.CachePolicy.CachePolicyConfig):
    default_ttl = 900
    min_ttl = 1
    max_ttl = 10800
    name = Sub('${AppName}-default')
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyDefaultParametersInCacheKeyAndForwardedToOrigin


class CloudFrontCachePolicyDefault(cloudfront.CachePolicy):
    cache_policy_config = CloudFrontCachePolicyDefaultCachePolicyConfig


class CloudFrontLogDistroKinesisStreamConfig(cloudfront.RealtimeLogConfig.KinesisStreamConfig):
    stream_arn = LoggingStream.Arn
    role_arn = LoggingRole.Arn


class CloudFrontLogDistroEndPoint(cloudfront.RealtimeLogConfig.EndPoint):
    kinesis_stream_config = CloudFrontLogDistroKinesisStreamConfig
    stream_type = 'Kinesis'


class CloudFrontLogDistro(cloudfront.RealtimeLogConfig):
    end_points = [CloudFrontLogDistroEndPoint]
    fields = ['timestamp', 'c-ip', 'sc-status', 'cs-uri-stem', 'c-country']
    name = Sub('LoggingConfig-${AppName}')
    sampling_rate = 100


class CloudFrontCachePolicyClientCookiesConfig(cloudfront.CachePolicy.CookiesConfig):
    cookie_behavior = 'none'


class CloudFrontCachePolicyClientHeadersConfig(cloudfront.CachePolicy.HeadersConfig):
    header_behavior = 'none'


class CloudFrontCachePolicyClientQueryStringsConfig(cloudfront.CachePolicy.QueryStringsConfig):
    query_string_behavior = 'all'


class CloudFrontCachePolicyClientParametersInCacheKeyAndForwardedToOrigin(cloudfront.CachePolicy.ParametersInCacheKeyAndForwardedToOrigin):
    cookies_config = CloudFrontCachePolicyClientCookiesConfig
    enable_accept_encoding_brotli = True
    enable_accept_encoding_gzip = True
    headers_config = CloudFrontCachePolicyClientHeadersConfig
    query_strings_config = CloudFrontCachePolicyClientQueryStringsConfig


class CloudFrontCachePolicyClientCachePolicyConfig(cloudfront.CachePolicy.CachePolicyConfig):
    default_ttl = 3600
    min_ttl = 1
    max_ttl = 31536000
    name = Sub('${AppName}-client')
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyClientParametersInCacheKeyAndForwardedToOrigin


class CloudFrontCachePolicyClient(cloudfront.CachePolicy):
    cache_policy_config = CloudFrontCachePolicyClientCachePolicyConfig


class CloudFrontDistroCacheBehavior(cloudfront.Distribution.CacheBehavior):
    allowed_methods = ['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']
    cached_methods = ['GET', 'HEAD', 'OPTIONS']
    cache_policy_id = CloudFrontCachePolicyAPI
    compress = True
    path_pattern = '/app/*'
    target_origin_id = 'URLShortenerAPIGW'
    viewer_protocol_policy = 'redirect-to-https'


class CloudFrontDistroCacheBehavior1(cloudfront.Distribution.CacheBehavior):
    allowed_methods = ['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']
    cached_methods = ['GET', 'HEAD', 'OPTIONS']
    cache_policy_id = CloudFrontCachePolicyAPI
    compress = True
    path_pattern = '/app/'
    target_origin_id = 'URLShortenerAPIGW'
    viewer_protocol_policy = 'redirect-to-https'


class CloudFrontDistroCacheBehavior2(cloudfront.Distribution.CacheBehavior):
    allowed_methods = ['GET', 'HEAD', 'OPTIONS']
    cached_methods = ['GET', 'HEAD', 'OPTIONS']
    cache_policy_id = CloudFrontCachePolicyClient
    compress = True
    path_pattern = '/s12dAssetsDirectory/*'
    target_origin_id = 'AmplifyClient'
    viewer_protocol_policy = 'redirect-to-https'


class CloudFrontDistroCacheBehavior3(cloudfront.Distribution.CacheBehavior):
    allowed_methods = ['GET', 'HEAD', 'OPTIONS']
    cached_methods = ['GET', 'HEAD', 'OPTIONS']
    cache_policy_id = CloudFrontCachePolicyClient
    compress = True
    path_pattern = '/client/*'
    target_origin_id = 'AmplifyClient'
    viewer_protocol_policy = 'redirect-to-https'


class CloudFrontDistroCacheBehavior4(cloudfront.Distribution.CacheBehavior):
    allowed_methods = ['GET', 'HEAD', 'OPTIONS']
    cached_methods = ['GET', 'HEAD', 'OPTIONS']
    cache_policy_id = CloudFrontCachePolicyClient
    compress = True
    path_pattern = '/*.ico'
    target_origin_id = 'AmplifyClient'
    viewer_protocol_policy = 'redirect-to-https'


class CloudFrontDistroCacheBehavior5(cloudfront.Distribution.CacheBehavior):
    allowed_methods = ['GET', 'HEAD', 'OPTIONS']
    cached_methods = ['GET', 'HEAD', 'OPTIONS']
    cache_policy_id = CloudFrontCachePolicyClient
    compress = True
    path_pattern = '/'
    target_origin_id = 'AmplifyClient'
    viewer_protocol_policy = 'redirect-to-https'


class CloudFrontDistroDefaultCacheBehavior(cloudfront.Distribution.DefaultCacheBehavior):
    allowed_methods = ['GET', 'HEAD']
    cached_methods = ['GET', 'HEAD']
    cache_policy_id = CloudFrontCachePolicyDefault
    compress = False
    realtime_log_config_arn = CloudFrontLogDistro.Arn
    target_origin_id = 'URLShortenerAPIGW'
    viewer_protocol_policy = 'redirect-to-https'


class CloudFrontDistroCustomErrorResponse(cloudfront.Distribution.CustomErrorResponse):
    error_caching_min_ttl = 0
    error_code = 400


class CloudFrontDistroCustomErrorResponse1(cloudfront.Distribution.CustomErrorResponse):
    error_caching_min_ttl = 1
    error_code = 403


class CloudFrontDistroCustomErrorResponse2(cloudfront.Distribution.CustomErrorResponse):
    error_caching_min_ttl = 5
    error_code = 500


class CloudFrontDistroLogging(cloudfront.Distribution.Logging):
    bucket = CloudFrontAccessLogsBucket.DomainName


class CloudFrontDistroLegacyCustomOrigin(cloudfront.Distribution.LegacyCustomOrigin):
    origin_protocol_policy = 'https-only'


class CloudFrontDistroOrigin(cloudfront.Distribution.Origin):
    custom_origin_config = CloudFrontDistroLegacyCustomOrigin
    domain_name = Sub('${SiteAPI}.execute-api.${AWS::Region}.amazonaws.com')
    id = 'URLShortenerAPIGW'
    origin_path = '/Prod'


class CloudFrontDistroLegacyCustomOrigin1(cloudfront.Distribution.LegacyCustomOrigin):
    origin_protocol_policy = 'https-only'


class CloudFrontDistroOrigin1(cloudfront.Distribution.Origin):
    custom_origin_config = CloudFrontDistroLegacyCustomOrigin1
    domain_name = ClientAddress
    id = 'AmplifyClient'


class CloudFrontDistroViewerCertificate(cloudfront.Distribution.ViewerCertificate):
    acm_certificate_arn = '{{resolve:ssm:/acm/cert/s12d-com:1}}'
    ssl_support_method = 'sni-only'


class CloudFrontDistroDistributionConfig(cloudfront.Distribution.DistributionConfig):
    aliases = [CustomDomain]
    comment = Sub('URL Shortener CDN - ${CustomDomain}')
    cache_behaviors = [CloudFrontDistroCacheBehavior, CloudFrontDistroCacheBehavior1, CloudFrontDistroCacheBehavior2, CloudFrontDistroCacheBehavior3, CloudFrontDistroCacheBehavior4, CloudFrontDistroCacheBehavior5]
    default_cache_behavior = CloudFrontDistroDefaultCacheBehavior
    custom_error_responses = [CloudFrontDistroCustomErrorResponse, CloudFrontDistroCustomErrorResponse1, CloudFrontDistroCustomErrorResponse2]
    logging = CloudFrontDistroLogging
    enabled = True
    origins = [CloudFrontDistroOrigin, CloudFrontDistroOrigin1]
    viewer_certificate = CloudFrontDistroViewerCertificate


class CloudFrontDistro(cloudfront.Distribution):
    distribution_config = CloudFrontDistroDistributionConfig
