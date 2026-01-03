"""Network resources: ALBExternalAccessSG, HTTPTcpIn, EC2InstanceSG, OriginALB, Tcp8080Out, Tcp8080In, CloudFrontDistribution, HTTPSTcpIn."""

from . import *  # noqa: F403


class ALBExternalAccessSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb-external-access-ingrees-SG')


class ALBExternalAccessSGAssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'Environment'
    value = Environment


class ALBExternalAccessSG:
    resource: ec2.SecurityGroup
    group_description = 'Allow external access to ALB'
    vpc_id = VpcId
    tags = [ALBExternalAccessSGAssociationParameter, ALBExternalAccessSGAssociationParameter1]


class HTTPTcpIn:
    resource: ec2.SecurityGroupIngress
    group_id = ALBExternalAccessSG
    to_port = 80
    ip_protocol = 'tcp'
    from_port = 80
    cidr_ip = '0.0.0.0/0'


class EC2InstanceSGAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = Sub('${AppName}-${Environment}-ec2-instance-SG')


class EC2InstanceSGAssociationParameter1:
    resource: ec2.Instance.AssociationParameter
    key = 'Environment'
    value = Environment


class EC2InstanceSG:
    resource: ec2.SecurityGroup
    group_description = 'EC2 Instance Security Group'
    vpc_id = VpcId
    tags = [EC2InstanceSGAssociationParameter, EC2InstanceSGAssociationParameter1]


class OriginALBListenerAttribute:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = ALBAttributeIdleTimeOut


class OriginALBListenerAttribute1:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'deletion_protection.enabled'
    value = ALBAttributeDeletionProtection


class OriginALBListenerAttribute2:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'routing.http2.enabled'
    value = ALBAttributeRoutingHttp2


class OriginALBListenerAttribute3:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb')


class OriginALBListenerAttribute4:
    resource: elasticloadbalancingv2.Listener.ListenerAttribute
    key = 'Environment'
    value = Environment


class OriginALB:
    resource: elasticloadbalancingv2.LoadBalancer
    name = Sub('${AppName}-${Environment}-alb')
    scheme = ALBScheme
    type_ = ALBType
    load_balancer_attributes = [OriginALBListenerAttribute, OriginALBListenerAttribute1, OriginALBListenerAttribute2]
    subnets = [PublicSubnetId1, PublicSubnetId2]
    security_groups = [ALBExternalAccessSG]
    tags = [OriginALBListenerAttribute3, OriginALBListenerAttribute4]


class Tcp8080Out:
    resource: ec2.SecurityGroupEgress
    group_id = ALBExternalAccessSG
    to_port = 8080
    ip_protocol = 'tcp'
    from_port = 8080
    destination_security_group_id = EC2InstanceSG


class Tcp8080In:
    resource: ec2.SecurityGroupIngress
    group_id = EC2InstanceSG
    to_port = '8080'
    ip_protocol = 'tcp'
    from_port = '8080'
    source_security_group_id = ALBExternalAccessSG


class CloudFrontDistributionCustomOriginConfig:
    resource: cloudfront.Distribution.CustomOriginConfig
    http_port = 80
    https_port = 443
    origin_protocol_policy = OriginProtocolPolicy
    origin_keepalive_timeout = OriginKeepaliveTimeout
    origin_read_timeout = OriginReadTimeout
    origin_ssl_protocols = ['TLSv1', 'TLSv1.1', 'TLSv1.2', 'SSLv3']


class CloudFrontDistributionOrigin:
    resource: cloudfront.Distribution.Origin
    domain_name = OriginALB.DNSName
    id = OriginALB
    custom_origin_config = CloudFrontDistributionCustomOriginConfig


class CloudFrontDistributionCookies:
    resource: cloudfront.Distribution.Cookies
    forward = ForwardCookies


class CloudFrontDistributionForwardedValues:
    resource: cloudfront.Distribution.ForwardedValues
    query_string = QueryString
    cookies = CloudFrontDistributionCookies


class CloudFrontDistributionLambdaFunctionAssociation:
    resource: cloudfront.Distribution.LambdaFunctionAssociation
    event_type = LambdaEventType
    lambda_function_arn = LambdaEdgeVersion


class CloudFrontDistributionDefaultCacheBehavior:
    resource: cloudfront.Distribution.DefaultCacheBehavior
    allowed_methods = ['GET', 'HEAD', 'DELETE', 'OPTIONS', 'PATCH', 'POST', 'PUT']
    compress = Compress
    default_ttl = DefaultTTL
    max_ttl = MaxTTL
    min_ttl = MinTTL
    smooth_streaming = 'false'
    target_origin_id = OriginALB
    forwarded_values = CloudFrontDistributionForwardedValues
    viewer_protocol_policy = ViewerProtocolPolicy
    lambda_function_associations = [CloudFrontDistributionLambdaFunctionAssociation]


class CloudFrontDistributionViewerCertificate:
    resource: cloudfront.Distribution.ViewerCertificate
    acm_certificate_arn = Sub('arn:${AWS::Partition}:acm:${AWS::Region}:${AWS::AccountId}:certificate/${ACMCertificateIdentifier}')
    ssl_support_method = SslSupportMethod
    minimum_protocol_version = MinimumProtocolVersion


class CloudFrontDistributionLogging:
    resource: cloudfront.Distribution.Logging
    bucket = Sub('${LoggingBucket}.s3.amazonaws.com')


class CloudFrontDistributionDistributionConfig:
    resource: cloudfront.Distribution.DistributionConfig
    comment = 'Cloudfront Distribution pointing ALB Origin'
    origins = [CloudFrontDistributionOrigin]
    enabled = True
    http_version = 'http2'
    aliases = [AlternateDomainNames]
    default_cache_behavior = CloudFrontDistributionDefaultCacheBehavior
    price_class = PriceClass
    viewer_certificate = CloudFrontDistributionViewerCertificate
    ipv6_enabled = IPV6Enabled
    logging = CloudFrontDistributionLogging


class CloudFrontDistribution:
    resource: cloudfront.Distribution
    distribution_config = CloudFrontDistributionDistributionConfig
    depends_on = [LoggingBucket, LambdaEdgeFunction]


class HTTPSTcpIn:
    resource: ec2.SecurityGroupIngress
    group_id = ALBExternalAccessSG
    to_port = 443
    ip_protocol = 'tcp'
    from_port = 443
    cidr_ip = '0.0.0.0/0'
