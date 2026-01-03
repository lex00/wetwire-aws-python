"""Network resources: CachePolicy, Distribution."""

from . import *  # noqa: F403


class CachePolicyCookiesConfig:
    resource: cloudfront.CachePolicy.CookiesConfig
    cookie_behavior = 'all'


class CachePolicyHeadersConfig:
    resource: cloudfront.CachePolicy.HeadersConfig
    header_behavior = 'whitelist'
    headers = ['Accept-Charset', 'Authorization', 'Origin', 'Accept', 'Referer', 'Host', 'Accept-Language', 'Accept-Encoding', 'Accept-Datetime']


class CachePolicyQueryStringsConfig:
    resource: cloudfront.CachePolicy.QueryStringsConfig
    query_string_behavior = 'all'


class CachePolicyParametersInCacheKeyAndForwardedToOrigin:
    resource: cloudfront.CachePolicy.ParametersInCacheKeyAndForwardedToOrigin
    cookies_config = CachePolicyCookiesConfig
    enable_accept_encoding_gzip = False
    headers_config = CachePolicyHeadersConfig
    query_strings_config = CachePolicyQueryStringsConfig


class CachePolicyCachePolicyConfig:
    resource: cloudfront.CachePolicy.CachePolicyConfig
    default_ttl = 86400
    max_ttl = 31536000
    min_ttl = 1
    name = Name
    parameters_in_cache_key_and_forwarded_to_origin = CachePolicyParametersInCacheKeyAndForwardedToOrigin


class CachePolicy:
    resource: cloudfront.CachePolicy
    cache_policy_config = CachePolicyCachePolicyConfig


class DistributionCacheBehavior:
    resource: cloudfront.Distribution.CacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = '4135ea2d-6df8-44a3-9df3-4b5a84be39ad'
    compress = False
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'
    path_pattern = '/proxy/*'


class DistributionDefaultCacheBehavior:
    resource: cloudfront.Distribution.DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = CachePolicy
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'


class DistributionCustomOriginConfig:
    resource: cloudfront.Distribution.CustomOriginConfig
    http_port = Port
    origin_protocol_policy = 'http-only'


class DistributionOrigin:
    resource: cloudfront.Distribution.Origin
    domain_name = DomainName
    id = Sub('CloudFront-${AWS::StackName}')
    custom_origin_config = DistributionCustomOriginConfig


class DistributionDistributionConfig:
    resource: cloudfront.Distribution.DistributionConfig
    enabled = True
    http_version = 'http2'
    cache_behaviors = [DistributionCacheBehavior]
    default_cache_behavior = DistributionDefaultCacheBehavior
    origins = [DistributionOrigin]


class Distribution:
    resource: cloudfront.Distribution
    tags = [{
        'Key': 'Name',
        'Value': Name,
    }, {
        'Key': 'Description',
        'Value': Name,
    }]
    distribution_config = DistributionDistributionConfig
