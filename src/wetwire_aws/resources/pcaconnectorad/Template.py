"""PropertyTypes for AWS::PCAConnectorAD::Template."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApplicationPolicies(PropertyType):
    policies: list[DslValue[ApplicationPolicy]] = field(default_factory=list)
    critical: DslValue[bool] | None = None


@dataclass
class ApplicationPolicy(PropertyType):
    policy_object_identifier: DslValue[str] | None = None
    policy_type: DslValue[str] | None = None


@dataclass
class CertificateValidity(PropertyType):
    renewal_period: DslValue[ValidityPeriod] | None = None
    validity_period: DslValue[ValidityPeriod] | None = None


@dataclass
class EnrollmentFlagsV2(PropertyType):
    enable_key_reuse_on_nt_token_keyset_storage_full: DslValue[bool] | None = None
    include_symmetric_algorithms: DslValue[bool] | None = None
    no_security_extension: DslValue[bool] | None = None
    remove_invalid_certificate_from_personal_store: DslValue[bool] | None = None
    user_interaction_required: DslValue[bool] | None = None


@dataclass
class EnrollmentFlagsV3(PropertyType):
    enable_key_reuse_on_nt_token_keyset_storage_full: DslValue[bool] | None = None
    include_symmetric_algorithms: DslValue[bool] | None = None
    no_security_extension: DslValue[bool] | None = None
    remove_invalid_certificate_from_personal_store: DslValue[bool] | None = None
    user_interaction_required: DslValue[bool] | None = None


@dataclass
class EnrollmentFlagsV4(PropertyType):
    enable_key_reuse_on_nt_token_keyset_storage_full: DslValue[bool] | None = None
    include_symmetric_algorithms: DslValue[bool] | None = None
    no_security_extension: DslValue[bool] | None = None
    remove_invalid_certificate_from_personal_store: DslValue[bool] | None = None
    user_interaction_required: DslValue[bool] | None = None


@dataclass
class ExtensionsV2(PropertyType):
    key_usage: DslValue[KeyUsage] | None = None
    application_policies: DslValue[ApplicationPolicies] | None = None


@dataclass
class ExtensionsV3(PropertyType):
    key_usage: DslValue[KeyUsage] | None = None
    application_policies: DslValue[ApplicationPolicies] | None = None


@dataclass
class ExtensionsV4(PropertyType):
    key_usage: DslValue[KeyUsage] | None = None
    application_policies: DslValue[ApplicationPolicies] | None = None


@dataclass
class GeneralFlagsV2(PropertyType):
    auto_enrollment: DslValue[bool] | None = None
    machine_type: DslValue[bool] | None = None


@dataclass
class GeneralFlagsV3(PropertyType):
    auto_enrollment: DslValue[bool] | None = None
    machine_type: DslValue[bool] | None = None


@dataclass
class GeneralFlagsV4(PropertyType):
    auto_enrollment: DslValue[bool] | None = None
    machine_type: DslValue[bool] | None = None


@dataclass
class KeyUsage(PropertyType):
    usage_flags: DslValue[KeyUsageFlags] | None = None
    critical: DslValue[bool] | None = None


@dataclass
class KeyUsageFlags(PropertyType):
    data_encipherment: DslValue[bool] | None = None
    digital_signature: DslValue[bool] | None = None
    key_agreement: DslValue[bool] | None = None
    key_encipherment: DslValue[bool] | None = None
    non_repudiation: DslValue[bool] | None = None


@dataclass
class KeyUsageProperty(PropertyType):
    property_flags: DslValue[KeyUsagePropertyFlags] | None = None
    property_type: DslValue[str] | None = None


@dataclass
class KeyUsagePropertyFlags(PropertyType):
    decrypt: DslValue[bool] | None = None
    key_agreement: DslValue[bool] | None = None
    sign: DslValue[bool] | None = None


@dataclass
class PrivateKeyAttributesV2(PropertyType):
    key_spec: DslValue[str] | None = None
    minimal_key_length: DslValue[float] | None = None
    crypto_providers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PrivateKeyAttributesV3(PropertyType):
    algorithm: DslValue[str] | None = None
    key_spec: DslValue[str] | None = None
    key_usage_property: DslValue[KeyUsageProperty] | None = None
    minimal_key_length: DslValue[float] | None = None
    crypto_providers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PrivateKeyAttributesV4(PropertyType):
    key_spec: DslValue[str] | None = None
    minimal_key_length: DslValue[float] | None = None
    algorithm: DslValue[str] | None = None
    crypto_providers: list[DslValue[str]] = field(default_factory=list)
    key_usage_property: DslValue[KeyUsageProperty] | None = None


@dataclass
class PrivateKeyFlagsV2(PropertyType):
    client_version: DslValue[str] | None = None
    exportable_key: DslValue[bool] | None = None
    strong_key_protection_required: DslValue[bool] | None = None


@dataclass
class PrivateKeyFlagsV3(PropertyType):
    client_version: DslValue[str] | None = None
    exportable_key: DslValue[bool] | None = None
    require_alternate_signature_algorithm: DslValue[bool] | None = None
    strong_key_protection_required: DslValue[bool] | None = None


@dataclass
class PrivateKeyFlagsV4(PropertyType):
    client_version: DslValue[str] | None = None
    exportable_key: DslValue[bool] | None = None
    require_alternate_signature_algorithm: DslValue[bool] | None = None
    require_same_key_renewal: DslValue[bool] | None = None
    strong_key_protection_required: DslValue[bool] | None = None
    use_legacy_provider: DslValue[bool] | None = None


@dataclass
class SubjectNameFlagsV2(PropertyType):
    require_common_name: DslValue[bool] | None = None
    require_directory_path: DslValue[bool] | None = None
    require_dns_as_cn: DslValue[bool] | None = None
    require_email: DslValue[bool] | None = None
    san_require_directory_guid: DslValue[bool] | None = None
    san_require_dns: DslValue[bool] | None = None
    san_require_domain_dns: DslValue[bool] | None = None
    san_require_email: DslValue[bool] | None = None
    san_require_spn: DslValue[bool] | None = None
    san_require_upn: DslValue[bool] | None = None


@dataclass
class SubjectNameFlagsV3(PropertyType):
    require_common_name: DslValue[bool] | None = None
    require_directory_path: DslValue[bool] | None = None
    require_dns_as_cn: DslValue[bool] | None = None
    require_email: DslValue[bool] | None = None
    san_require_directory_guid: DslValue[bool] | None = None
    san_require_dns: DslValue[bool] | None = None
    san_require_domain_dns: DslValue[bool] | None = None
    san_require_email: DslValue[bool] | None = None
    san_require_spn: DslValue[bool] | None = None
    san_require_upn: DslValue[bool] | None = None


@dataclass
class SubjectNameFlagsV4(PropertyType):
    require_common_name: DslValue[bool] | None = None
    require_directory_path: DslValue[bool] | None = None
    require_dns_as_cn: DslValue[bool] | None = None
    require_email: DslValue[bool] | None = None
    san_require_directory_guid: DslValue[bool] | None = None
    san_require_dns: DslValue[bool] | None = None
    san_require_domain_dns: DslValue[bool] | None = None
    san_require_email: DslValue[bool] | None = None
    san_require_spn: DslValue[bool] | None = None
    san_require_upn: DslValue[bool] | None = None


@dataclass
class TemplateDefinition(PropertyType):
    template_v2: DslValue[TemplateV2] | None = None
    template_v3: DslValue[TemplateV3] | None = None
    template_v4: DslValue[TemplateV4] | None = None


@dataclass
class TemplateV2(PropertyType):
    certificate_validity: DslValue[CertificateValidity] | None = None
    enrollment_flags: DslValue[EnrollmentFlagsV2] | None = None
    extensions: DslValue[ExtensionsV2] | None = None
    general_flags: DslValue[GeneralFlagsV2] | None = None
    private_key_attributes: DslValue[PrivateKeyAttributesV2] | None = None
    private_key_flags: DslValue[PrivateKeyFlagsV2] | None = None
    subject_name_flags: DslValue[SubjectNameFlagsV2] | None = None
    superseded_templates: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TemplateV3(PropertyType):
    certificate_validity: DslValue[CertificateValidity] | None = None
    enrollment_flags: DslValue[EnrollmentFlagsV3] | None = None
    extensions: DslValue[ExtensionsV3] | None = None
    general_flags: DslValue[GeneralFlagsV3] | None = None
    hash_algorithm: DslValue[str] | None = None
    private_key_attributes: DslValue[PrivateKeyAttributesV3] | None = None
    private_key_flags: DslValue[PrivateKeyFlagsV3] | None = None
    subject_name_flags: DslValue[SubjectNameFlagsV3] | None = None
    superseded_templates: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TemplateV4(PropertyType):
    certificate_validity: DslValue[CertificateValidity] | None = None
    enrollment_flags: DslValue[EnrollmentFlagsV4] | None = None
    extensions: DslValue[ExtensionsV4] | None = None
    general_flags: DslValue[GeneralFlagsV4] | None = None
    private_key_attributes: DslValue[PrivateKeyAttributesV4] | None = None
    private_key_flags: DslValue[PrivateKeyFlagsV4] | None = None
    subject_name_flags: DslValue[SubjectNameFlagsV4] | None = None
    hash_algorithm: DslValue[str] | None = None
    superseded_templates: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ValidityPeriod(PropertyType):
    period: DslValue[float] | None = None
    period_type: DslValue[str] | None = None
