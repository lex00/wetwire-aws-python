"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Environment:
    """Please specify the target environment."""

    resource: Parameter
    type = STRING
    description = 'Please specify the target environment.'
    default = 'dev'
    allowed_values = [
    'prod',
    'staging',
    'dev',
    'qa',
]


class VpcId:
    """Please specify the VPC ID."""

    resource: Parameter
    type = VPC_ID
    description = 'Please specify the VPC ID.'
    constraint_description = 'Must be a valid VPC ID'


class PublicSubnetId1:
    """Please specify first public subnet ID."""

    resource: Parameter
    type = SUBNET_ID
    description = 'Please specify first public subnet ID.'
    constraint_description = 'Must be a valid subnet ID in the selected VPC'


class PublicSubnetId2:
    """Please specify second public subnet ID."""

    resource: Parameter
    type = SUBNET_ID
    description = 'Please specify second public subnet ID.'
    constraint_description = 'Must be a valid subnet ID in the selected VPC'


class AppName:
    """Application environment name."""

    resource: Parameter
    type = STRING
    description = 'Application environment name.'
    default = 'example'


class AlternateDomainNames:
    """CNAMEs (alternate domain names), if any, for the distribution. Example. mydomain.com"""

    resource: Parameter
    type = STRING
    description = 'CNAMEs (alternate domain names), if any, for the distribution. Example. mydomain.com'
    default = 'name.domain.com'


class ACMCertificateIdentifier:
    """The AWS Certificate Manager (ACM) certificate identifier."""

    resource: Parameter
    type = STRING
    description = 'The AWS Certificate Manager (ACM) certificate identifier.'
    default = '1234567890abcdefgh'


class LambdaEventType:
    """Please specify the event type that triggers a Lambda function invocation."""

    resource: Parameter
    type = STRING
    description = 'Please specify the event type that triggers a Lambda function invocation.'
    default = 'viewer-response'
    allowed_values = [
    'viewer-request',
    'origin-request',
    'origin-response',
    'viewer-response',
]


class IPV6Enabled:
    """Should CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution."""

    resource: Parameter
    type = STRING
    description = 'Should CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution.'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class EC2ImageId:
    """EC2 AMI Id"""

    resource: Parameter
    type = AMI_ID
    description = 'EC2 AMI Id'
    default = 'ami-0d85a662720db9789'


class EC2InstanceType:
    """Amazon EC2 instance type."""

    resource: Parameter
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


class KeyPairName:
    """EC2 KeyPair."""

    resource: Parameter
    type = KEY_PAIR
    description = 'EC2 KeyPair.'
    constraint_description = 'Must be the name of an existing EC2 KeyPair'


class BootVolSize:
    """EC2 Instance Boot volume size."""

    resource: Parameter
    type = STRING
    description = 'EC2 Instance Boot volume size.'
    default = '100'


class BootVolType:
    """EC2 Instance Boot volume type."""

    resource: Parameter
    type = STRING
    description = 'EC2 Instance Boot volume type.'
    default = 'gp2'
    allowed_values = [
    'gp2',
    'io1',
    'sc1',
    'st1',
]


class ALBType:
    """AWS Load Balancer Type."""

    resource: Parameter
    type = STRING
    description = 'AWS Load Balancer Type.'
    default = 'application'
    allowed_values = [
    'application',
    'network',
]


class OriginALBTGPort:
    """Port number the application is running on, for Origin ALB Target Group and Health Check port."""

    resource: Parameter
    type = STRING
    description = 'Port number the application is running on, for Origin ALB Target Group and Health Check port.'
    default = '8080'


class OriginProtocolPolicy:
    """CloudFront Origin Protocol Policy to apply to your origin."""

    resource: Parameter
    type = STRING
    description = 'CloudFront Origin Protocol Policy to apply to your origin.'
    default = 'http-only'
    allowed_values = [
    'http-only',
    'match-viewer',
    'https-only',
]


class Compress:
    """CloudFront should support gzip compression requests: Accept-Encoding: gzip."""

    resource: Parameter
    type = STRING
    description = 'CloudFront should support gzip compression requests: Accept-Encoding: gzip.'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class DefaultTTL:
    """The default time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 86400 seconds (one day)."""

    resource: Parameter
    type = STRING
    description = 'The default time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 86400 seconds (one day).'
    default = '0'


class MaxTTL:
    """The maximum time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 31536000 seconds (one year)."""

    resource: Parameter
    type = STRING
    description = 'The maximum time in seconds that objects stay in CloudFront caches before CloudFront forwards another request to your custom origin. By default, AWS CloudFormation specifies 31536000 seconds (one year).'
    default = '0'


class MinTTL:
    """The minimum amount of time that you want objects to stay in the cache before CloudFront queries your origin to see whether the object has been updated."""

    resource: Parameter
    type = STRING
    description = 'The minimum amount of time that you want objects to stay in the cache before CloudFront queries your origin to see whether the object has been updated.'
    default = '0'


class QueryString:
    """CIndicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior."""

    resource: Parameter
    type = STRING
    description = 'CIndicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior.'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class ForwardCookies:
    """Forwards specified cookies to the origin of the cache behavior."""

    resource: Parameter
    type = STRING
    description = 'Forwards specified cookies to the origin of the cache behavior.'
    default = 'all'
    allowed_values = [
    'all',
    'whitelist',
    'none',
]


class ViewerProtocolPolicy:
    """The protocol that users can use to access the files in the origin that you specified in the TargetOriginId property when the default cache behavior is applied to a request."""

    resource: Parameter
    type = STRING
    description = 'The protocol that users can use to access the files in the origin that you specified in the TargetOriginId property when the default cache behavior is applied to a request.'
    default = 'redirect-to-https'
    allowed_values = [
    'redirect-to-https',
    'allow-all',
    'https-only',
]


class PriceClass:
    """The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations."""

    resource: Parameter
    type = STRING
    description = 'The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify PriceClass_All, CloudFront responds to requests for your objects from all CloudFront edge locations.'
    default = 'PriceClass_All'
    allowed_values = [
    'PriceClass_All',
    'PriceClass_100',
    'PriceClass_200',
]


class SslSupportMethod:
    """Specifies how CloudFront serves HTTPS requests."""

    resource: Parameter
    type = STRING
    description = 'Specifies how CloudFront serves HTTPS requests.'
    default = 'sni-only'
    allowed_values = [
    'sni-only',
    'vip',
]


class MinimumProtocolVersion:
    """The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections."""

    resource: Parameter
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


class OriginKeepaliveTimeout:
    """You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths. The minimum timeout length is 1 second; the maximum is 60 seconds."""

    resource: Parameter
    type = STRING
    description = 'You can create a custom keep-alive timeout. All timeout units are in seconds. The default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths. The minimum timeout length is 1 second; the maximum is 60 seconds.'
    default = '60'


class OriginReadTimeout:
    """You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths. The minimum timeout length is 4 seconds; the maximum is 60 seconds."""

    resource: Parameter
    type = STRING
    description = 'You can create a custom origin read timeout. All timeout units are in seconds. The default origin read timeout is 30 seconds, but you can configure custom timeout lengths. The minimum timeout length is 4 seconds; the maximum is 60 seconds.'
    default = '30'


class ALBScheme:
    """Origin ALB scheme."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB scheme.'
    default = 'internet-facing'
    allowed_values = [
    'internet-facing',
    'internal',
]


class ALBTargetGroupHealthCheckIntervalSeconds:
    """Origin ALB Target Group Health Check Interval in Seconds."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Health Check Interval in Seconds.'
    default = '30'


class ALBTargetGroupHealthCheckTimeoutSeconds:
    """Origin ALB Target Group Health Check Timeout in Seconds."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Health Check Timeout in Seconds.'
    default = '5'


class ALBTargetGroupHealthyThresholdCount:
    """Origin ALB Target Group Healthy Threshold Count."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Healthy Threshold Count.'
    default = '5'


class ALBTargetGroupUnhealthyThresholdCount:
    """Origin ALB Target Group Unhealthy Threshold Count."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = '2'


class ALBAttributeIdleTimeOut:
    """Origin ALB Target Group Unhealthy Threshold Count."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = '60'


class ALBAttributeDeletionProtection:
    """Origin ALB Target Group Unhealthy Threshold Count."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class ALBAttributeRoutingHttp2:
    """Origin ALB Target Group Unhealthy Threshold Count."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Unhealthy Threshold Count.'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class ALBTargetGroupAttributeDeregistration:
    """Origin ALB Target Group Deregistration Timeout."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Deregistration Timeout.'
    default = '300'


class HealthCheckProtocol:
    """Origin ALB Target Group Health Check Protocol."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Health Check Protocol.'
    default = 'HTTP'
    allowed_values = [
    'HTTPS',
    'HTTP',
]


class HealthCheckPath:
    """Origin ALB Target Group Health Check Path."""

    resource: Parameter
    type = STRING
    description = 'Origin ALB Target Group Health Check Path.'
    default = '/health.html'


class LoggingBucketVersioning:
    """The versioning state of an Amazon S3 bucket. If you enable versioning, you must suspend versioning to disable it."""

    resource: Parameter
    type = STRING
    description = 'The versioning state of an Amazon S3 bucket. If you enable versioning, you must suspend versioning to disable it.'
    default = 'Suspended'
    allowed_values = [
    'Enabled',
    'Suspended',
]
