"""PropertyTypes for AWS::CloudFront::Distribution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CacheBehavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ttl": "DefaultTTL",
        "max_ttl": "MaxTTL",
        "min_ttl": "MinTTL",
    }

    path_pattern: str | None = None
    target_origin_id: str | None = None
    viewer_protocol_policy: str | None = None
    allowed_methods: list[String] = field(default_factory=list)
    cache_policy_id: str | None = None
    cached_methods: list[String] = field(default_factory=list)
    compress: bool | None = None
    default_ttl: float | None = None
    field_level_encryption_id: str | None = None
    forwarded_values: ForwardedValues | None = None
    function_associations: list[FunctionAssociation] = field(default_factory=list)
    grpc_config: GrpcConfig | None = None
    lambda_function_associations: list[LambdaFunctionAssociation] = field(
        default_factory=list
    )
    max_ttl: float | None = None
    min_ttl: float | None = None
    origin_request_policy_id: str | None = None
    realtime_log_config_arn: str | None = None
    response_headers_policy_id: str | None = None
    smooth_streaming: bool | None = None
    trusted_key_groups: list[String] = field(default_factory=list)
    trusted_signers: list[String] = field(default_factory=list)


@dataclass
class ConnectionFunctionAssociation(PropertyType):
    id: str | None = None


@dataclass
class Cookies(PropertyType):
    forward: str | None = None
    whitelisted_names: list[String] = field(default_factory=list)


@dataclass
class CustomErrorResponse(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "error_caching_min_ttl": "ErrorCachingMinTTL",
    }

    error_code: int | None = None
    error_caching_min_ttl: float | None = None
    response_code: int | None = None
    response_page_path: str | None = None


@dataclass
class CustomOriginConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_port": "HTTPPort",
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
    }

    origin_protocol_policy: str | None = None
    http_port: int | None = None
    https_port: int | None = None
    ip_address_type: str | None = None
    origin_keepalive_timeout: int | None = None
    origin_mtls_config: OriginMtlsConfig | None = None
    origin_read_timeout: int | None = None
    origin_ssl_protocols: list[String] = field(default_factory=list)


@dataclass
class DefaultCacheBehavior(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ttl": "DefaultTTL",
        "max_ttl": "MaxTTL",
        "min_ttl": "MinTTL",
    }

    target_origin_id: str | None = None
    viewer_protocol_policy: str | None = None
    allowed_methods: list[String] = field(default_factory=list)
    cache_policy_id: str | None = None
    cached_methods: list[String] = field(default_factory=list)
    compress: bool | None = None
    default_ttl: float | None = None
    field_level_encryption_id: str | None = None
    forwarded_values: ForwardedValues | None = None
    function_associations: list[FunctionAssociation] = field(default_factory=list)
    grpc_config: GrpcConfig | None = None
    lambda_function_associations: list[LambdaFunctionAssociation] = field(
        default_factory=list
    )
    max_ttl: float | None = None
    min_ttl: float | None = None
    origin_request_policy_id: str | None = None
    realtime_log_config_arn: str | None = None
    response_headers_policy_id: str | None = None
    smooth_streaming: bool | None = None
    trusted_key_groups: list[String] = field(default_factory=list)
    trusted_signers: list[String] = field(default_factory=list)


@dataclass
class Definition(PropertyType):
    string_schema: StringSchema | None = None


@dataclass
class DistributionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cnam_es": "CNAMEs",
        "ipv6_enabled": "IPV6Enabled",
        "web_acl_id": "WebACLId",
    }

    default_cache_behavior: DefaultCacheBehavior | None = None
    enabled: bool | None = None
    aliases: list[String] = field(default_factory=list)
    anycast_ip_list_id: str | None = None
    cache_behaviors: list[CacheBehavior] = field(default_factory=list)
    cnam_es: list[String] = field(default_factory=list)
    comment: str | None = None
    connection_function_association: ConnectionFunctionAssociation | None = None
    connection_mode: str | None = None
    continuous_deployment_policy_id: str | None = None
    custom_error_responses: list[CustomErrorResponse] = field(default_factory=list)
    custom_origin: LegacyCustomOrigin | None = None
    default_root_object: str | None = None
    http_version: str | None = None
    ipv6_enabled: bool | None = None
    logging: Logging | None = None
    origin_groups: OriginGroups | None = None
    origins: list[Origin] = field(default_factory=list)
    price_class: str | None = None
    restrictions: Restrictions | None = None
    s3_origin: LegacyS3Origin | None = None
    staging: bool | None = None
    tenant_config: TenantConfig | None = None
    viewer_certificate: ViewerCertificate | None = None
    viewer_mtls_config: ViewerMtlsConfig | None = None
    web_acl_id: str | None = None


@dataclass
class ForwardedValues(PropertyType):
    query_string: bool | None = None
    cookies: Cookies | None = None
    headers: list[String] = field(default_factory=list)
    query_string_cache_keys: list[String] = field(default_factory=list)


@dataclass
class FunctionAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionARN",
    }

    event_type: str | None = None
    function_arn: str | None = None


@dataclass
class GeoRestriction(PropertyType):
    restriction_type: str | None = None
    locations: list[String] = field(default_factory=list)


@dataclass
class GrpcConfig(PropertyType):
    enabled: bool | None = None


@dataclass
class LambdaFunctionAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lambda_function_arn": "LambdaFunctionARN",
    }

    event_type: str | None = None
    include_body: bool | None = None
    lambda_function_arn: str | None = None


@dataclass
class LegacyCustomOrigin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DNSName",
        "http_port": "HTTPPort",
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
    }

    dns_name: str | None = None
    origin_protocol_policy: str | None = None
    origin_ssl_protocols: list[String] = field(default_factory=list)
    http_port: int | None = None
    https_port: int | None = None


@dataclass
class LegacyS3Origin(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dns_name": "DNSName",
    }

    dns_name: str | None = None
    origin_access_identity: str | None = None


@dataclass
class Logging(PropertyType):
    bucket: str | None = None
    include_cookies: bool | None = None
    prefix: str | None = None


@dataclass
class Origin(PropertyType):
    domain_name: str | None = None
    id: str | None = None
    connection_attempts: int | None = None
    connection_timeout: int | None = None
    custom_origin_config: CustomOriginConfig | None = None
    origin_access_control_id: str | None = None
    origin_custom_headers: list[OriginCustomHeader] = field(default_factory=list)
    origin_path: str | None = None
    origin_shield: OriginShield | None = None
    response_completion_timeout: int | None = None
    s3_origin_config: S3OriginConfig | None = None
    vpc_origin_config: VpcOriginConfig | None = None


@dataclass
class OriginCustomHeader(PropertyType):
    header_name: str | None = None
    header_value: str | None = None


@dataclass
class OriginGroup(PropertyType):
    failover_criteria: OriginGroupFailoverCriteria | None = None
    id: str | None = None
    members: OriginGroupMembers | None = None
    selection_criteria: str | None = None


@dataclass
class OriginGroupFailoverCriteria(PropertyType):
    status_codes: StatusCodes | None = None


@dataclass
class OriginGroupMember(PropertyType):
    origin_id: str | None = None


@dataclass
class OriginGroupMembers(PropertyType):
    items: list[OriginGroupMember] = field(default_factory=list)
    quantity: int | None = None


@dataclass
class OriginGroups(PropertyType):
    quantity: int | None = None
    items: list[OriginGroup] = field(default_factory=list)


@dataclass
class OriginMtlsConfig(PropertyType):
    client_certificate_arn: str | None = None


@dataclass
class OriginShield(PropertyType):
    enabled: bool | None = None
    origin_shield_region: str | None = None


@dataclass
class ParameterDefinition(PropertyType):
    definition: Definition | None = None
    name: str | None = None


@dataclass
class Restrictions(PropertyType):
    geo_restriction: GeoRestriction | None = None


@dataclass
class S3OriginConfig(PropertyType):
    origin_access_identity: str | None = None
    origin_read_timeout: int | None = None


@dataclass
class StatusCodes(PropertyType):
    items: list[Integer] = field(default_factory=list)
    quantity: int | None = None


@dataclass
class StringSchema(PropertyType):
    required: bool | None = None
    comment: str | None = None
    default_value: str | None = None


@dataclass
class TenantConfig(PropertyType):
    parameter_definitions: list[ParameterDefinition] = field(default_factory=list)


@dataclass
class TrustStoreConfig(PropertyType):
    trust_store_id: str | None = None
    advertise_trust_store_ca_names: bool | None = None
    ignore_certificate_expiry: bool | None = None


@dataclass
class ViewerCertificate(PropertyType):
    acm_certificate_arn: str | None = None
    cloud_front_default_certificate: bool | None = None
    iam_certificate_id: str | None = None
    minimum_protocol_version: str | None = None
    ssl_support_method: str | None = None


@dataclass
class ViewerMtlsConfig(PropertyType):
    mode: str | None = None
    trust_store_config: TrustStoreConfig | None = None


@dataclass
class VpcOriginConfig(PropertyType):
    vpc_origin_id: str | None = None
    origin_keepalive_timeout: int | None = None
    origin_read_timeout: int | None = None
    owner_account_id: str | None = None
