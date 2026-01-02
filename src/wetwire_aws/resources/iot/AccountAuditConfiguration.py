"""PropertyTypes for AWS::IoT::AccountAuditConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuditCheckConfiguration(PropertyType):
    enabled: bool | None = None


@dataclass
class AuditCheckConfigurations(PropertyType):
    authenticated_cognito_role_overly_permissive_check: (
        AuditCheckConfiguration | None
    ) = None
    ca_certificate_expiring_check: AuditCheckConfiguration | None = None
    ca_certificate_key_quality_check: AuditCheckConfiguration | None = None
    conflicting_client_ids_check: AuditCheckConfiguration | None = None
    device_certificate_age_check: DeviceCertAgeAuditCheckConfiguration | None = None
    device_certificate_expiring_check: (
        DeviceCertExpirationAuditCheckConfiguration | None
    ) = None
    device_certificate_key_quality_check: AuditCheckConfiguration | None = None
    device_certificate_shared_check: AuditCheckConfiguration | None = None
    intermediate_ca_revoked_for_active_device_certificates_check: (
        AuditCheckConfiguration | None
    ) = None
    io_t_policy_potential_mis_configuration_check: AuditCheckConfiguration | None = None
    iot_policy_overly_permissive_check: AuditCheckConfiguration | None = None
    iot_role_alias_allows_access_to_unused_services_check: (
        AuditCheckConfiguration | None
    ) = None
    iot_role_alias_overly_permissive_check: AuditCheckConfiguration | None = None
    logging_disabled_check: AuditCheckConfiguration | None = None
    revoked_ca_certificate_still_active_check: AuditCheckConfiguration | None = None
    revoked_device_certificate_still_active_check: AuditCheckConfiguration | None = None
    unauthenticated_cognito_role_overly_permissive_check: (
        AuditCheckConfiguration | None
    ) = None


@dataclass
class AuditNotificationTarget(PropertyType):
    enabled: bool | None = None
    role_arn: str | None = None
    target_arn: str | None = None


@dataclass
class AuditNotificationTargetConfigurations(PropertyType):
    sns: AuditNotificationTarget | None = None


@dataclass
class CertAgeCheckCustomConfiguration(PropertyType):
    cert_age_threshold_in_days: str | None = None


@dataclass
class CertExpirationCheckCustomConfiguration(PropertyType):
    cert_expiration_threshold_in_days: str | None = None


@dataclass
class DeviceCertAgeAuditCheckConfiguration(PropertyType):
    configuration: CertAgeCheckCustomConfiguration | None = None
    enabled: bool | None = None


@dataclass
class DeviceCertExpirationAuditCheckConfiguration(PropertyType):
    configuration: CertExpirationCheckCustomConfiguration | None = None
    enabled: bool | None = None
