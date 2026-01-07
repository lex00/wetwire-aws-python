"""PropertyTypes for AWS::CloudFront::Distribution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CacheBehavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ttl": "DefaultTTL",
        "max_ttl": "MaxTTL",
        "min_ttl": "MinTTL",
    }

    path_pattern: DslValue[str] | None = None
    target_origin_id: DslValue[str] | None = None
    viewer_protocol_policy: DslValue[str] | None = None
    allowed_methods: list[DslValue[str]] = field(default_factory=list)
    cache_policy_id: DslValue[str] | None = None
    cached_methods: list[DslValue[str]] = field(default_factory=list)
    compress: DslValue[bool] | None = None
    default_ttl: DslValue[float] | None = None
    field_level_encryption_id: DslValue[str] | None = None
    forwarded_values: DslValue[ForwardedValues] | None = None
    function_associations: list[DslValue[FunctionAssociation]] = field(
        default_factory=list
    )
    grpc_config: DslValue[GrpcConfig] | None = None
    lambda_function_associations: list[DslValue[LambdaFunctionAssociation]] = field(
        default_factory=list
    )
    max_ttl: DslValue[float] | None = None
    min_ttl: DslValue[float] | None = None
    origin_request_policy_id: DslValue[str] | None = None
    realtime_log_config_arn: DslValue[str] | None = None
    response_headers_policy_id: DslValue[str] | None = None
    smooth_streaming: DslValue[bool] | None = None
    trusted_key_groups: list[DslValue[str]] = field(default_factory=list)
    trusted_signers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ConnectionFunctionAssociation(PropertyType):
    id: DslValue[str] | None = None


@dataclass
class Cookies(PropertyType):
    forward: DslValue[str] | None = None
    whitelisted_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CustomErrorResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "error_caching_min_ttl": "ErrorCachingMinTTL",
    }

    error_code: DslValue[int] | None = None
    error_caching_min_ttl: DslValue[float] | None = None
    response_code: DslValue[int] | None = None
    response_page_path: DslValue[str] | None = None


@dataclass
class CustomOriginConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_port": "HTTPPort",
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
    }

    origin_protocol_policy: DslValue[str] | None = None
    http_port: DslValue[int] | None = None
    https_port: DslValue[int] | None = None
    ip_address_type: DslValue[str] | None = None
    origin_keepalive_timeout: DslValue[int] | None = None
    origin_mtls_config: DslValue[OriginMtlsConfig] | None = None
    origin_read_timeout: DslValue[int] | None = None
    origin_ssl_protocols: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DefaultCacheBehavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ttl": "DefaultTTL",
        "max_ttl": "MaxTTL",
        "min_ttl": "MinTTL",
    }

    target_origin_id: DslValue[str] | None = None
    viewer_protocol_policy: DslValue[str] | None = None
    allowed_methods: list[DslValue[str]] = field(default_factory=list)
    cache_policy_id: DslValue[str] | None = None
    cached_methods: list[DslValue[str]] = field(default_factory=list)
    compress: DslValue[bool] | None = None
    default_ttl: DslValue[float] | None = None
    field_level_encryption_id: DslValue[str] | None = None
    forwarded_values: DslValue[ForwardedValues] | None = None
    function_associations: list[DslValue[FunctionAssociation]] = field(
        default_factory=list
    )
    grpc_config: DslValue[GrpcConfig] | None = None
    lambda_function_associations: list[DslValue[LambdaFunctionAssociation]] = field(
        default_factory=list
    )
    max_ttl: DslValue[float] | None = None
    min_ttl: DslValue[float] | None = None
    origin_request_policy_id: DslValue[str] | None = None
    realtime_log_config_arn: DslValue[str] | None = None
    response_headers_policy_id: DslValue[str] | None = None
    smooth_streaming: DslValue[bool] | None = None
    trusted_key_groups: list[DslValue[str]] = field(default_factory=list)
    trusted_signers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Definition(PropertyType):
    string_schema: DslValue[StringSchema] | None = None


@dataclass
class DistributionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cnam_es": "CNAMEs",
        "ipv6_enabled": "IPV6Enabled",
        "web_acl_id": "WebACLId",
    }

    default_cache_behavior: DslValue[DefaultCacheBehavior] | None = None
    enabled: DslValue[bool] | None = None
    aliases: list[DslValue[str]] = field(default_factory=list)
    anycast_ip_list_id: DslValue[str] | None = None
    cache_behaviors: list[DslValue[CacheBehavior]] = field(default_factory=list)
    cnam_es: list[DslValue[str]] = field(default_factory=list)
    comment: DslValue[str] | None = None
    connection_function_association: DslValue[ConnectionFunctionAssociation] | None = (
        None
    )
    connection_mode: DslValue[str] | None = None
    continuous_deployment_policy_id: DslValue[str] | None = None
    custom_error_responses: list[DslValue[CustomErrorResponse]] = field(
        default_factory=list
    )
    custom_origin: DslValue[LegacyCustomOrigin] | None = None
    default_root_object: DslValue[str] | None = None
    http_version: DslValue[str] | None = None
    ipv6_enabled: DslValue[bool] | None = None
    logging: DslValue[Logging] | None = None
    origin_groups: DslValue[OriginGroups] | None = None
    origins: list[DslValue[Origin]] = field(default_factory=list)
    price_class: DslValue[str] | None = None
    restrictions: DslValue[Restrictions] | None = None
    s3_origin: DslValue[LegacyS3Origin] | None = None
    staging: DslValue[bool] | None = None
    tenant_config: DslValue[TenantConfig] | None = None
    viewer_certificate: DslValue[ViewerCertificate] | None = None
    viewer_mtls_config: DslValue[ViewerMtlsConfig] | None = None
    web_acl_id: DslValue[str] | None = None


@dataclass
class ForwardedValues(PropertyType):
    query_string: DslValue[bool] | None = None
    cookies: DslValue[Cookies] | None = None
    headers: list[DslValue[str]] = field(default_factory=list)
    query_string_cache_keys: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FunctionAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionARN",
    }

    event_type: DslValue[str] | None = None
    function_arn: DslValue[str] | None = None


@dataclass
class GeoRestriction(PropertyType):
    restriction_type: DslValue[str] | None = None
    locations: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GrpcConfig(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class LambdaFunctionAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_function_arn": "LambdaFunctionARN",
    }

    event_type: DslValue[str] | None = None
    include_body: DslValue[bool] | None = None
    lambda_function_arn: DslValue[str] | None = None


@dataclass
class LegacyCustomOrigin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DNSName",
        "http_port": "HTTPPort",
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
    }

    dns_name: DslValue[str] | None = None
    origin_protocol_policy: DslValue[str] | None = None
    origin_ssl_protocols: list[DslValue[str]] = field(default_factory=list)
    http_port: DslValue[int] | None = None
    https_port: DslValue[int] | None = None


@dataclass
class LegacyS3Origin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DNSName",
    }

    dns_name: DslValue[str] | None = None
    origin_access_identity: DslValue[str] | None = None


@dataclass
class Logging(PropertyType):
    bucket: DslValue[str] | None = None
    include_cookies: DslValue[bool] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class Origin(PropertyType):
    domain_name: DslValue[str] | None = None
    id: DslValue[str] | None = None
    connection_attempts: DslValue[int] | None = None
    connection_timeout: DslValue[int] | None = None
    custom_origin_config: DslValue[CustomOriginConfig] | None = None
    origin_access_control_id: DslValue[str] | None = None
    origin_custom_headers: list[DslValue[OriginCustomHeader]] = field(
        default_factory=list
    )
    origin_path: DslValue[str] | None = None
    origin_shield: DslValue[OriginShield] | None = None
    response_completion_timeout: DslValue[int] | None = None
    s3_origin_config: DslValue[S3OriginConfig] | None = None
    vpc_origin_config: DslValue[VpcOriginConfig] | None = None


@dataclass
class OriginCustomHeader(PropertyType):
    header_name: DslValue[str] | None = None
    header_value: DslValue[str] | None = None


@dataclass
class OriginGroup(PropertyType):
    failover_criteria: DslValue[OriginGroupFailoverCriteria] | None = None
    id: DslValue[str] | None = None
    members: DslValue[OriginGroupMembers] | None = None
    selection_criteria: DslValue[str] | None = None


@dataclass
class OriginGroupFailoverCriteria(PropertyType):
    status_codes: DslValue[StatusCodes] | None = None


@dataclass
class OriginGroupMember(PropertyType):
    origin_id: DslValue[str] | None = None


@dataclass
class OriginGroupMembers(PropertyType):
    items: list[DslValue[OriginGroupMember]] = field(default_factory=list)
    quantity: DslValue[int] | None = None


@dataclass
class OriginGroups(PropertyType):
    quantity: DslValue[int] | None = None
    items: list[DslValue[OriginGroup]] = field(default_factory=list)


@dataclass
class OriginMtlsConfig(PropertyType):
    client_certificate_arn: DslValue[str] | None = None


@dataclass
class OriginShield(PropertyType):
    enabled: DslValue[bool] | None = None
    origin_shield_region: DslValue[str] | None = None


@dataclass
class ParameterDefinition(PropertyType):
    definition: DslValue[Definition] | None = None
    name: DslValue[str] | None = None


@dataclass
class Restrictions(PropertyType):
    geo_restriction: DslValue[GeoRestriction] | None = None


@dataclass
class S3OriginConfig(PropertyType):
    origin_access_identity: DslValue[str] | None = None
    origin_read_timeout: DslValue[int] | None = None


@dataclass
class StatusCodes(PropertyType):
    items: list[DslValue[int]] = field(default_factory=list)
    quantity: DslValue[int] | None = None


@dataclass
class StringSchema(PropertyType):
    required: DslValue[bool] | None = None
    comment: DslValue[str] | None = None
    default_value: DslValue[str] | None = None


@dataclass
class TenantConfig(PropertyType):
    parameter_definitions: list[DslValue[ParameterDefinition]] = field(
        default_factory=list
    )


@dataclass
class TrustStoreConfig(PropertyType):
    trust_store_id: DslValue[str] | None = None
    advertise_trust_store_ca_names: DslValue[bool] | None = None
    ignore_certificate_expiry: DslValue[bool] | None = None


@dataclass
class ViewerCertificate(PropertyType):
    acm_certificate_arn: DslValue[str] | None = None
    cloud_front_default_certificate: DslValue[bool] | None = None
    iam_certificate_id: DslValue[str] | None = None
    minimum_protocol_version: DslValue[str] | None = None
    ssl_support_method: DslValue[str] | None = None


@dataclass
class ViewerMtlsConfig(PropertyType):
    mode: DslValue[str] | None = None
    trust_store_config: DslValue[TrustStoreConfig] | None = None


@dataclass
class VpcOriginConfig(PropertyType):
    vpc_origin_id: DslValue[str] | None = None
    origin_keepalive_timeout: DslValue[int] | None = None
    origin_read_timeout: DslValue[int] | None = None
    owner_account_id: DslValue[str] | None = None
