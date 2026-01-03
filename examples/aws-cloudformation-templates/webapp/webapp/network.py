"""Network resources: SiteOriginAccessControl."""

from . import *  # noqa: F403


class SiteOriginAccessControlOriginAccessControlConfig:
    resource: cloudfront.OriginAccessControl.OriginAccessControlConfig
    name = Join('', [
    AppName,
    Select(2, Split('/', AWS_STACK_ID)),
])
    origin_access_control_origin_type = 's3'
    signing_behavior = 'always'
    signing_protocol = 'sigv4'


class SiteOriginAccessControl:
    resource: cloudfront.OriginAccessControl
    origin_access_control_config = SiteOriginAccessControlOriginAccessControlConfig
