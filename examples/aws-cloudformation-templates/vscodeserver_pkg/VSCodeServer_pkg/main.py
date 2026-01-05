"""Stack resources."""

from . import *  # noqa: F403


class CloudFrontDistributionCacheBehavior:
    resource: cloudfront.Distribution.CacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = '4135ea2d-6df8-44a3-9df3-4b5a84be39ad'
    compress = False
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'
    path_pattern = '/proxy/*'


class CloudFrontDistributionDefaultCacheBehavior:
    resource: cloudfront.Distribution.DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'POST', 'DELETE']
    cache_policy_id = CloudFrontCachePolicy
    origin_request_policy_id = '216adef6-5c7f-47e4-b989-5492eafa07d3'
    target_origin_id = Sub('CloudFront-${AWS::StackName}')
    viewer_protocol_policy = 'allow-all'


class CloudFrontDistributionCustomOriginConfig:
    resource: cloudfront.Distribution.CustomOriginConfig
    http_port = 8080
    origin_protocol_policy = 'http-only'


class CloudFrontDistributionOrigin:
    resource: cloudfront.Distribution.Origin
    domain_name = Server.PublicDnsName
    id = Sub('CloudFront-${AWS::StackName}')
    custom_origin_config = CloudFrontDistributionCustomOriginConfig


class CloudFrontDistributionDistributionConfig:
    resource: cloudfront.Distribution.DistributionConfig
    enabled = True
    http_version = 'http2'
    cache_behaviors = [CloudFrontDistributionCacheBehavior]
    default_cache_behavior = CloudFrontDistributionDefaultCacheBehavior
    origins = [CloudFrontDistributionOrigin]


class CloudFrontDistribution(cloudfront.Distribution):
    tags = [{
        'Key': 'Name',
        'Value': 'vscode-server',
    }, {
        'Key': 'Description',
        'Value': 'vscode-server',
    }]
    distribution_config = CloudFrontDistributionDistributionConfig
    depends_on = [Server]
