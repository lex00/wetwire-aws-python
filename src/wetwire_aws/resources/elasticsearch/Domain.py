"""PropertyTypes for AWS::Elasticsearch::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
    anonymous_auth_enabled: bool | None = None
    enabled: bool | None = None
    internal_user_database_enabled: bool | None = None
    master_user_options: MasterUserOptions | None = None


@dataclass
class CognitoOptions(PropertyType):
    enabled: bool | None = None
    identity_pool_id: str | None = None
    role_arn: str | None = None
    user_pool_id: str | None = None


@dataclass
class ColdStorageOptions(PropertyType):
    enabled: bool | None = None


@dataclass
class DomainEndpointOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enforce_https": "EnforceHTTPS",
        "tls_security_policy": "TLSSecurityPolicy",
    }

    custom_endpoint: str | None = None
    custom_endpoint_certificate_arn: str | None = None
    custom_endpoint_enabled: bool | None = None
    enforce_https: bool | None = None
    tls_security_policy: str | None = None


@dataclass
class EBSOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_enabled": "EBSEnabled",
    }

    ebs_enabled: bool | None = None
    iops: int | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class ElasticsearchClusterConfig(PropertyType):
    cold_storage_options: ColdStorageOptions | None = None
    dedicated_master_count: int | None = None
    dedicated_master_enabled: bool | None = None
    dedicated_master_type: str | None = None
    instance_count: int | None = None
    instance_type: str | None = None
    warm_count: int | None = None
    warm_enabled: bool | None = None
    warm_type: str | None = None
    zone_awareness_config: ZoneAwarenessConfig | None = None
    zone_awareness_enabled: bool | None = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    enabled: bool | None = None
    kms_key_id: str | None = None


@dataclass
class LogPublishingOption(PropertyType):
    cloud_watch_logs_log_group_arn: str | None = None
    enabled: bool | None = None


@dataclass
class MasterUserOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "master_user_arn": "MasterUserARN",
    }

    master_user_arn: str | None = None
    master_user_name: str | None = None
    master_user_password: str | None = None


@dataclass
class NodeToNodeEncryptionOptions(PropertyType):
    enabled: bool | None = None


@dataclass
class SnapshotOptions(PropertyType):
    automated_snapshot_start_hour: int | None = None


@dataclass
class VPCOptions(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class ZoneAwarenessConfig(PropertyType):
    availability_zone_count: int | None = None
