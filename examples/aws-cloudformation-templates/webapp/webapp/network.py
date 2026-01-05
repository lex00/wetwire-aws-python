"""Network resources: SiteOriginAccessControl, SiteDistribution."""

from . import *  # noqa: F403


class SiteOriginAccessControlOriginAccessControlConfig(cloudfront.OriginAccessControl.OriginAccessControlConfig):
    name = Join('', [
    AppName,
    Select(2, Split('/', AWS_STACK_ID)),
])
    origin_access_control_origin_type = 's3'
    signing_behavior = 'always'
    signing_protocol = 'sigv4'


class SiteOriginAccessControl(cloudfront.OriginAccessControl):
    origin_access_control_config = SiteOriginAccessControlOriginAccessControlConfig


class SiteDistributionDefaultCacheBehavior(cloudfront.Distribution.DefaultCacheBehavior):
    cache_policy_id = '658327ea-f89d-4fab-a63d-7e88639e58f6'
    compress = True
    target_origin_id = Sub('${AppName}-origin-1')
    viewer_protocol_policy = 'redirect-to-https'


class SiteDistributionLogging(cloudfront.Distribution.Logging):
    bucket = SiteCloudFrontLogsBucket.RegionalDomainName


class SiteDistributionS3OriginConfig(cloudfront.Distribution.S3OriginConfig):
    origin_access_identity = ''


class SiteDistributionOrigin(cloudfront.Distribution.Origin):
    domain_name = SiteContentBucket.RegionalDomainName
    id = Sub('${AppName}-origin-1')
    origin_access_control_id = SiteOriginAccessControl.Id
    s3_origin_config = SiteDistributionS3OriginConfig


class SiteDistributionViewerCertificate(cloudfront.Distribution.ViewerCertificate):
    cloud_front_default_certificate = True


class SiteDistributionDistributionConfig(cloudfront.Distribution.DistributionConfig):
    default_cache_behavior = SiteDistributionDefaultCacheBehavior
    default_root_object = 'index.html'
    enabled = True
    http_version = 'http2'
    ipv6_enabled = True
    logging = SiteDistributionLogging
    origins = [SiteDistributionOrigin]
    viewer_certificate = SiteDistributionViewerCertificate
    web_acl_id = SiteWebACL.Arn


class SiteDistribution(cloudfront.Distribution):
    distribution_config = SiteDistributionDistributionConfig
