"""Network resources: OriginAccessControl, Distribution."""

from . import *  # noqa: F403


class OriginAccessControlOriginAccessControlConfig(cloudfront.OriginAccessControl.OriginAccessControlConfig):
    name = Join('', [
    'rain-build-website-',
    Select(2, Split('/', AWS_STACK_ID)),
])
    origin_access_control_origin_type = 's3'
    signing_behavior = 'always'
    signing_protocol = 'sigv4'


class OriginAccessControl(cloudfront.OriginAccessControl):
    origin_access_control_config = OriginAccessControlOriginAccessControlConfig


class DistributionDefaultCacheBehavior(cloudfront.Distribution.DefaultCacheBehavior):
    cache_policy_id = 'rain-build-cache-policy-1'
    compress = True
    target_origin_id = 'rain-build-origin-1'
    viewer_protocol_policy = 'redirect-to-https'


class DistributionLogging(cloudfront.Distribution.Logging):
    bucket = CloudFrontLogsBucket.RegionalDomainName


class DistributionLegacyS3Origin(cloudfront.Distribution.LegacyS3Origin):
    origin_access_identity = ''


class DistributionOrigin(cloudfront.Distribution.Origin):
    domain_name = ContentBucket.RegionalDomainName
    id = 'rain-build-origin-1'
    origin_access_control_id = OriginAccessControl.Id
    s3_origin_config = DistributionLegacyS3Origin


class DistributionViewerCertificate(cloudfront.Distribution.ViewerCertificate):
    cloud_front_default_certificate = True


class DistributionDistributionConfig(cloudfront.Distribution.DistributionConfig):
    default_cache_behavior = DistributionDefaultCacheBehavior
    default_root_object = 'index.html'
    enabled = True
    http_version = 'http2'
    ipv6_enabled = True
    logging = DistributionLogging
    origins = [DistributionOrigin]
    viewer_certificate = DistributionViewerCertificate
    web_acl_id = WebACL


class Distribution(cloudfront.Distribution):
    distribution_config = DistributionDistributionConfig
