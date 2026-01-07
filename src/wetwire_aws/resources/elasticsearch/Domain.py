"""PropertyTypes for AWS::Elasticsearch::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
    anonymous_auth_enabled: DslValue[bool] | None = None
    enabled: DslValue[bool] | None = None
    internal_user_database_enabled: DslValue[bool] | None = None
    master_user_options: DslValue[MasterUserOptions] | None = None


@dataclass
class CognitoOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    identity_pool_id: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    user_pool_id: DslValue[str] | None = None


@dataclass
class ColdStorageOptions(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class DomainEndpointOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enforce_https": "EnforceHTTPS",
        "tls_security_policy": "TLSSecurityPolicy",
    }

    custom_endpoint: DslValue[str] | None = None
    custom_endpoint_certificate_arn: DslValue[str] | None = None
    custom_endpoint_enabled: DslValue[bool] | None = None
    enforce_https: DslValue[bool] | None = None
    tls_security_policy: DslValue[str] | None = None


@dataclass
class EBSOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_enabled": "EBSEnabled",
    }

    ebs_enabled: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class ElasticsearchClusterConfig(PropertyType):
    cold_storage_options: DslValue[ColdStorageOptions] | None = None
    dedicated_master_count: DslValue[int] | None = None
    dedicated_master_enabled: DslValue[bool] | None = None
    dedicated_master_type: DslValue[str] | None = None
    instance_count: DslValue[int] | None = None
    instance_type: DslValue[str] | None = None
    warm_count: DslValue[int] | None = None
    warm_enabled: DslValue[bool] | None = None
    warm_type: DslValue[str] | None = None
    zone_awareness_config: DslValue[ZoneAwarenessConfig] | None = None
    zone_awareness_enabled: DslValue[bool] | None = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class LogPublishingOption(PropertyType):
    cloud_watch_logs_log_group_arn: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class MasterUserOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "master_user_arn": "MasterUserARN",
    }

    master_user_arn: DslValue[str] | None = None
    master_user_name: DslValue[str] | None = None
    master_user_password: DslValue[str] | None = None


@dataclass
class NodeToNodeEncryptionOptions(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class SnapshotOptions(PropertyType):
    automated_snapshot_start_hour: DslValue[int] | None = None


@dataclass
class VPCOptions(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ZoneAwarenessConfig(PropertyType):
    availability_zone_count: DslValue[int] | None = None
