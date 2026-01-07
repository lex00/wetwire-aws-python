"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Environment(Parameter):
    """Please specify the target environment."""

    type = STRING
    description = 'Please specify the target environment.'
    default = 'dev'
    allowed_values = [
    'prod',
    'staging',
    'dev',
    'qa',
]


class VpcId(Parameter):
    """Please specify the VPC ID."""

    type = VPC_ID
    description = 'Please specify the VPC ID.'
    constraint_description = 'Must be a valid VPC ID'


class PublicSubnetId1(Parameter):
    """Please specify first public subnet ID."""

    type = SUBNET_ID
    description = 'Please specify first public subnet ID.'
    constraint_description = 'Must be a valid subnet ID in the selected VPC'


class PublicSubnetId2(Parameter):
    """Please specify second public subnet ID."""

    type = SUBNET_ID
    description = 'Please specify second public subnet ID.'
    constraint_description = 'Must be a valid subnet ID in the selected VPC'


class AppName(Parameter):
    """Application environment name."""

    type = STRING
    description = 'Application environment name.'
    default = 'example'


class AlternateDomainNames(Parameter):
    """CNAMEs (alternate domain names), if any, for the distribution. Example. mydomain.com"""

    type = STRING
    description = 'CNAMEs (alternate domain names), if any, for the distribution. Example. mydomain.com'
    default = 'name.domain.com'


class ACMCertificateIdentifier(Parameter):
    """The AWS Certificate Manager (ACM) certificate identifier."""

    type = STRING
    description = 'The AWS Certificate Manager (ACM) certificate identifier.'
    default = '1234567890abcdefgh'


class LambdaEventType(Parameter):
    """Please specify the event type that triggers a Lambda function invocation."""

    type = STRING
    description = 'Please specify the event type that triggers a Lambda function invocation.'
    default = 'viewer-response'
    allowed_values = [
    'viewer-request',
    'origin-request',
    'origin-response',
    'viewer-response',
]


class IPV6Enabled(Parameter):
    """Should CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution."""

    type = STRING
    description = 'Should CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution.'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class EC2ImageId(Parameter):
    """EC2 AMI Id"""

    type = AMI_ID
    description = 'EC2 AMI Id'
    default = 'ami-0d85a662720db9789'


class EC2InstanceType(Parameter):
    """Amazon EC2 instance type."""

    type = STRING
    description = 'Amazon EC2 instance type.'
    default = 't2.small'
    allowed_values = [
    't2.small',
    't2.medium',
    't2.large',
    't2.xlarge',
    't2.2xlarge',
    'm4.large',
    'm4.xlarge',
    'm4.2xlarge',
    'm4.4xlarge',
    'm4.10xlarge',
    'm4.16xlarge',
    'm5.large',
    'm5.xlarge',
    'm5.2xlarge',
    'm5.4xlarge',
    'm5.12xlarge',
    'm5.24xlarge',
    'm5d.large',
    'm5d.xlarge',
    'm5d.2xlarge',
    'm5d.4xlarge',
    'm5d.12xlarge',
    'm5d.24xlarge',
]


class KeyPairName(Parameter):
    """EC2 KeyPair."""

    type = KEY_PAIR
    description = 'EC2 KeyPair.'
    constraint_description = 'Must be the name of an existing EC2 KeyPair'


class BootVolSize(Parameter):
    """EC2 Instance Boot volume size."""

    type = STRING
    description = 'EC2 Instance Boot volume size.'
    default = '100'


class BootVolType(Parameter):
    """EC2 Instance Boot volume type."""

    type = STRING
    description = 'EC2 Instance Boot volume type.'
    default = 'gp2'
    allowed_values = [
    'gp2',
    'io1',
    'sc1',
    'st1',
]


class ALBType(Parameter):
    """AWS Load Balancer Type."""

    type = STRING
    description = 'AWS Load Balancer Type.'
    default = 'application'
    allowed_values = [
    'application',
    'network',
]


class OriginALBTGPort(Parameter):
    """Port number the application is running on, for Origin ALB Target Group and Health Check port."""

    type = STRING
    description = 'Port number the application is running on, for Origin ALB Target Group and Health Check port.'
    default = '8080'


class OriginProtocolPolicy(Parameter):
    """CloudFront Origin Protocol Policy to apply to your origin."""

    type = STRING
    description = 'CloudFront Origin Protocol Policy to apply to your origin.'
    default = 'http-only'
    allowed_values = [
    'http-only',
    'match-viewer',
    'https-only',
]


class Compress(Parameter):
    """CloudFront should support gzip compression requests: Accept-Encoding: gzip."""

    type = STRING
    description = 'CloudFront should support gzip compression requests: Accept-Encoding: gzip.'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class DefaultTTL(Parameter):
    """The default time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 86400 seconds (one day)."""

    type = STRING
    description = 'The default time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 86400 seconds (one day).'
    default = '0'


class MaxTTL(Parameter):
    """The maximum time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 31536000 seconds (one year)."""

    type = STRING
    description = 'The maximum time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 31536000 seconds (one year).'
    default = '0'


class MinTTL(Parameter):
    """The minimum amount of time that you want objects to stay in the cache before CloudFront queries your origin to see whether the object has been updated."""

    type = STRING
    description = 'The minimum amount of time that you want objects to stay in the cache before CloudFront queries your origin to see whether the object has been updated.'
    default = '0'


class QueryString(Parameter):
    """CIndicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior."""

    type = STRING
    description = 'CIndicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior.'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class ForwardCookies(Parameter):
    """Forwards specified cookies to the origin of the cache behavior."""

    type = STRING
    description = 'Forwards specified cookies to the origin of the cache behavior.'
    default = 'all'
    allowed_values = [
    'all',
    'whitelist',
    'none',
]


class ViewerProtocolPolicy(Parameter):
    """The protocol that users can use to access the files in the origin that you specified in the TargetOriginId property when the default cache behavior is applied to a request."""

    type = STRING
    description = 'The protocol that users can use to access the files in the origin that you specified in the TargetOriginId property when the default cache behavior is applied to a request.'
    default = 'redirect-to-https'
    allowed_values = [
    'redirect-to-https',
    'allow-all',
    'https-only',
]


class PriceClass(Parameter):
    """The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations."""

    type = STRING
    description = 'The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.'
    default = 'PriceClass_All'
    allowed_values = [
    'PriceClass_All',
    'PriceClass_100',
    'PriceClass_200',
]


class SslSupportMethod(Parameter):
    """Specifies how CloudFront serves HTTPS requests."""

    type = STRING
    description = 'Specifies how CloudFront serves HTTPS requests.'
    default = 'sni-only'
    allowed_values = [
    'sni-only',
    'vip',
]


class MinimumProtocolVersion(Parameter):
    """The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections."""

    type = STRING
    description = 'The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.'
    default = 'TLSv1'
    allowed_values = [
    'TLSv1',
    'TLSv1.2_2018',
    'TLSv1.1_2016',
    'TLSv1_2016',
    'SSLv3',
]


class OriginKeepaliveTimeout(Parameter):
    """You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths. The minimum timeout length is 1 second; the maximum is 60 seconds."""

    type = STRING
    description = 'You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths. The minimum timeout length is 1 second; the maximum is 60 seconds.'
    default = '60'


class OriginReadTimeout(Parameter):
    """You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths. The minimum timeout length is 4 seconds; the maximum is 60 seconds."""

    type = STRING
    description = 'You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths. The minimum timeout length is 4 seconds; the maximum is 60 seconds.'
    default = '30'


class ALBScheme(Parameter):
    """Origin ALB scheme."""

    type = STRING
    description = 'Origin ALB scheme.'
    default = 'internet-facing'
    allowed_values = [
    'internet-facing',
    'internal',
]


class ALBTargetGroupHealthCheckIntervalSeconds(Parameter):
    """Origin ALB Target Group Health Check Interval in Seconds."""

    type = STRING
    description = 'Origin ALB Target Group Health Check Interval in Seconds.'
    default = '30'


class ALBTargetGroupHealthCheckTimeoutSeconds(Parameter):
    """Origin ALB Target Group Health Check Timeout in Seconds."""

    type = STRING
    description = 'Origin ALB Target Group Health Check Timeout in Seconds.'
    default = '5'


class ALBTargetGroupHealthyThresholdCount(Parameter):
    """Origin ALB Target Group Healthy Threshold Count."""

    type = STRING
    description = 'Origin ALB Target Group Healthy Threshold Count.'
    default = '5'


class ALBTargetGroupUnhealthyThresholdCount(Parameter):
    """Origin ALB Target Group Unhealthy Threshold Count."""

    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = '2'


class ALBAttributeIdleTimeOut(Parameter):
    """Origin ALB Target Group Unhealthy Threshold Count."""

    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = '60'


class ALBAttributeDeletionProtection(Parameter):
    """Origin ALB Target Group Unhealthy Threshold Count."""

    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class ALBAttributeRoutingHttp2(Parameter):
    """Origin ALB Target Group Unhealthy Threshold Count."""

    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class ALBTargetGroupAttributeDeregistration(Parameter):
    """Origin ALB Target Group Deregistration Timeout."""

    type = STRING
    description = 'Origin ALB Target Group Deregistration Timeout.'
    default = '300'


class HealthCheckProtocol(Parameter):
    """Origin ALB Target Group Health Check Protocol."""

    type = STRING
    description = 'Origin ALB Target Group Health Check Protocol.'
    default = 'HTTP'
    allowed_values = [
    'HTTPS',
    'HTTP',
]


class HealthCheckPath(Parameter):
    """Origin ALB Target Group Health Check Path."""

    type = STRING
    description = 'Origin ALB Target Group Health Check Path.'
    default = '/health.html'


class LoggingBucketVersioning(Parameter):
    """The versioning state of an Amazon S3 bucket. If you enable versioning, you must suspend versioning to disable it."""

    type = STRING
    description = 'The versioning state of an Amazon S3 bucket. If you enable versioning, you must suspend versioning to disable it.'
    default = 'Suspended'
    allowed_values = [
    'Enabled',
    'Suspended',
]
