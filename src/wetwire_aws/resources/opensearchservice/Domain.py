"""PropertyTypes for AWS::OpenSearchService::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AIMLOptions(PropertyType):
    s3_vectors_engine: DslValue[S3VectorsEngine] | None = None


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_federation_options": "IAMFederationOptions",
        "jwt_options": "JWTOptions",
        "saml_options": "SAMLOptions",
    }

    anonymous_auth_disable_date: DslValue[str] | None = None
    anonymous_auth_enabled: DslValue[bool] | None = None
    enabled: DslValue[bool] | None = None
    iam_federation_options: DslValue[IAMFederationOptions] | None = None
    internal_user_database_enabled: DslValue[bool] | None = None
    jwt_options: DslValue[JWTOptions] | None = None
    master_user_options: DslValue[MasterUserOptions] | None = None
    saml_options: DslValue[SAMLOptions] | None = None


@dataclass
class ClusterConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_az_with_standby_enabled": "MultiAZWithStandbyEnabled",
    }

    cold_storage_options: DslValue[ColdStorageOptions] | None = None
    dedicated_master_count: DslValue[int] | None = None
    dedicated_master_enabled: DslValue[bool] | None = None
    dedicated_master_type: DslValue[str] | None = None
    instance_count: DslValue[int] | None = None
    instance_type: DslValue[str] | None = None
    multi_az_with_standby_enabled: DslValue[bool] | None = None
    node_options: list[DslValue[NodeOption]] = field(default_factory=list)
    warm_count: DslValue[int] | None = None
    warm_enabled: DslValue[bool] | None = None
    warm_type: DslValue[str] | None = None
    zone_awareness_config: DslValue[ZoneAwarenessConfig] | None = None
    zone_awareness_enabled: DslValue[bool] | None = None


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
    throughput: DslValue[int] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class IAMFederationOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    roles_key: DslValue[str] | None = None
    subject_key: DslValue[str] | None = None


@dataclass
class IdentityCenterOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_api_access": "EnabledAPIAccess",
        "identity_center_application_arn": "IdentityCenterApplicationARN",
        "identity_center_instance_arn": "IdentityCenterInstanceARN",
    }

    enabled_api_access: DslValue[bool] | None = None
    identity_center_application_arn: DslValue[str] | None = None
    identity_center_instance_arn: DslValue[str] | None = None
    identity_store_id: DslValue[str] | None = None
    roles_key: DslValue[str] | None = None
    subject_key: DslValue[str] | None = None


@dataclass
class Idp(PropertyType):
    entity_id: DslValue[str] | None = None
    metadata_content: DslValue[str] | None = None


@dataclass
class JWTOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    public_key: DslValue[str] | None = None
    roles_key: DslValue[str] | None = None
    subject_key: DslValue[str] | None = None


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
class NodeConfig(PropertyType):
    count: DslValue[int] | None = None
    enabled: DslValue[bool] | None = None
    type_: DslValue[str] | None = None


@dataclass
class NodeOption(PropertyType):
    node_config: DslValue[NodeConfig] | None = None
    node_type: DslValue[str] | None = None


@dataclass
class NodeToNodeEncryptionOptions(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class OffPeakWindow(PropertyType):
    window_start_time: DslValue[WindowStartTime] | None = None


@dataclass
class OffPeakWindowOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    off_peak_window: DslValue[OffPeakWindow] | None = None


@dataclass
class S3VectorsEngine(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class SAMLOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    idp: DslValue[Idp] | None = None
    master_backend_role: DslValue[str] | None = None
    master_user_name: DslValue[str] | None = None
    roles_key: DslValue[str] | None = None
    session_timeout_minutes: DslValue[int] | None = None
    subject_key: DslValue[str] | None = None


@dataclass
class ServiceSoftwareOptions(PropertyType):
    automated_update_date: DslValue[str] | None = None
    cancellable: DslValue[bool] | None = None
    current_version: DslValue[str] | None = None
    description: DslValue[str] | None = None
    new_version: DslValue[str] | None = None
    optional_deployment: DslValue[bool] | None = None
    update_available: DslValue[bool] | None = None
    update_status: DslValue[str] | None = None


@dataclass
class SnapshotOptions(PropertyType):
    automated_snapshot_start_hour: DslValue[int] | None = None


@dataclass
class SoftwareUpdateOptions(PropertyType):
    auto_software_update_enabled: DslValue[bool] | None = None


@dataclass
class VPCOptions(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class WindowStartTime(PropertyType):
    hours: DslValue[int] | None = None
    minutes: DslValue[int] | None = None


@dataclass
class ZoneAwarenessConfig(PropertyType):
    availability_zone_count: DslValue[int] | None = None
