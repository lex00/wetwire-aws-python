"""PropertyTypes for AWS::OpenSearchService::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AIMLOptions(PropertyType):
    s3_vectors_engine: S3VectorsEngine | None = None


@dataclass
class AdvancedSecurityOptionsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_federation_options": "IAMFederationOptions",
        "jwt_options": "JWTOptions",
        "saml_options": "SAMLOptions",
    }

    anonymous_auth_disable_date: str | None = None
    anonymous_auth_enabled: bool | None = None
    enabled: bool | None = None
    iam_federation_options: IAMFederationOptions | None = None
    internal_user_database_enabled: bool | None = None
    jwt_options: JWTOptions | None = None
    master_user_options: MasterUserOptions | None = None
    saml_options: SAMLOptions | None = None


@dataclass
class ClusterConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_az_with_standby_enabled": "MultiAZWithStandbyEnabled",
    }

    cold_storage_options: ColdStorageOptions | None = None
    dedicated_master_count: int | None = None
    dedicated_master_enabled: bool | None = None
    dedicated_master_type: str | None = None
    instance_count: int | None = None
    instance_type: str | None = None
    multi_az_with_standby_enabled: bool | None = None
    node_options: list[NodeOption] = field(default_factory=list)
    warm_count: int | None = None
    warm_enabled: bool | None = None
    warm_type: str | None = None
    zone_awareness_config: ZoneAwarenessConfig | None = None
    zone_awareness_enabled: bool | None = None


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
    throughput: int | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    enabled: bool | None = None
    kms_key_id: str | None = None


@dataclass
class IAMFederationOptions(PropertyType):
    enabled: bool | None = None
    roles_key: str | None = None
    subject_key: str | None = None


@dataclass
class IdentityCenterOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled_api_access": "EnabledAPIAccess",
        "identity_center_application_arn": "IdentityCenterApplicationARN",
        "identity_center_instance_arn": "IdentityCenterInstanceARN",
    }

    enabled_api_access: bool | None = None
    identity_center_application_arn: str | None = None
    identity_center_instance_arn: str | None = None
    identity_store_id: str | None = None
    roles_key: str | None = None
    subject_key: str | None = None


@dataclass
class Idp(PropertyType):
    entity_id: str | None = None
    metadata_content: str | None = None


@dataclass
class JWTOptions(PropertyType):
    enabled: bool | None = None
    public_key: str | None = None
    roles_key: str | None = None
    subject_key: str | None = None


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
class NodeConfig(PropertyType):
    count: int | None = None
    enabled: bool | None = None
    type_: str | None = None


@dataclass
class NodeOption(PropertyType):
    node_config: NodeConfig | None = None
    node_type: str | None = None


@dataclass
class NodeToNodeEncryptionOptions(PropertyType):
    enabled: bool | None = None


@dataclass
class OffPeakWindow(PropertyType):
    window_start_time: WindowStartTime | None = None


@dataclass
class OffPeakWindowOptions(PropertyType):
    enabled: bool | None = None
    off_peak_window: OffPeakWindow | None = None


@dataclass
class S3VectorsEngine(PropertyType):
    enabled: bool | None = None


@dataclass
class SAMLOptions(PropertyType):
    enabled: bool | None = None
    idp: Idp | None = None
    master_backend_role: str | None = None
    master_user_name: str | None = None
    roles_key: str | None = None
    session_timeout_minutes: int | None = None
    subject_key: str | None = None


@dataclass
class ServiceSoftwareOptions(PropertyType):
    automated_update_date: str | None = None
    cancellable: bool | None = None
    current_version: str | None = None
    description: str | None = None
    new_version: str | None = None
    optional_deployment: bool | None = None
    update_available: bool | None = None
    update_status: str | None = None


@dataclass
class SnapshotOptions(PropertyType):
    automated_snapshot_start_hour: int | None = None


@dataclass
class SoftwareUpdateOptions(PropertyType):
    auto_software_update_enabled: bool | None = None


@dataclass
class VPCOptions(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class WindowStartTime(PropertyType):
    hours: int | None = None
    minutes: int | None = None


@dataclass
class ZoneAwarenessConfig(PropertyType):
    availability_zone_count: int | None = None
