"""PropertyTypes for AWS::PCAConnectorAD::Template."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApplicationPolicies(PropertyType):
    policies: list[ApplicationPolicy] = field(default_factory=list)
    critical: bool | None = None


@dataclass
class ApplicationPolicy(PropertyType):
    policy_object_identifier: str | None = None
    policy_type: str | None = None


@dataclass
class CertificateValidity(PropertyType):
    renewal_period: ValidityPeriod | None = None
    validity_period: ValidityPeriod | None = None


@dataclass
class EnrollmentFlagsV2(PropertyType):
    enable_key_reuse_on_nt_token_keyset_storage_full: bool | None = None
    include_symmetric_algorithms: bool | None = None
    no_security_extension: bool | None = None
    remove_invalid_certificate_from_personal_store: bool | None = None
    user_interaction_required: bool | None = None


@dataclass
class EnrollmentFlagsV3(PropertyType):
    enable_key_reuse_on_nt_token_keyset_storage_full: bool | None = None
    include_symmetric_algorithms: bool | None = None
    no_security_extension: bool | None = None
    remove_invalid_certificate_from_personal_store: bool | None = None
    user_interaction_required: bool | None = None


@dataclass
class EnrollmentFlagsV4(PropertyType):
    enable_key_reuse_on_nt_token_keyset_storage_full: bool | None = None
    include_symmetric_algorithms: bool | None = None
    no_security_extension: bool | None = None
    remove_invalid_certificate_from_personal_store: bool | None = None
    user_interaction_required: bool | None = None


@dataclass
class ExtensionsV2(PropertyType):
    key_usage: KeyUsage | None = None
    application_policies: ApplicationPolicies | None = None


@dataclass
class ExtensionsV3(PropertyType):
    key_usage: KeyUsage | None = None
    application_policies: ApplicationPolicies | None = None


@dataclass
class ExtensionsV4(PropertyType):
    key_usage: KeyUsage | None = None
    application_policies: ApplicationPolicies | None = None


@dataclass
class GeneralFlagsV2(PropertyType):
    auto_enrollment: bool | None = None
    machine_type: bool | None = None


@dataclass
class GeneralFlagsV3(PropertyType):
    auto_enrollment: bool | None = None
    machine_type: bool | None = None


@dataclass
class GeneralFlagsV4(PropertyType):
    auto_enrollment: bool | None = None
    machine_type: bool | None = None


@dataclass
class KeyUsage(PropertyType):
    usage_flags: KeyUsageFlags | None = None
    critical: bool | None = None


@dataclass
class KeyUsageFlags(PropertyType):
    data_encipherment: bool | None = None
    digital_signature: bool | None = None
    key_agreement: bool | None = None
    key_encipherment: bool | None = None
    non_repudiation: bool | None = None


@dataclass
class KeyUsageProperty(PropertyType):
    property_flags: KeyUsagePropertyFlags | None = None
    property_type: str | None = None


@dataclass
class KeyUsagePropertyFlags(PropertyType):
    decrypt: bool | None = None
    key_agreement: bool | None = None
    sign: bool | None = None


@dataclass
class PrivateKeyAttributesV2(PropertyType):
    key_spec: str | None = None
    minimal_key_length: float | None = None
    crypto_providers: list[String] = field(default_factory=list)


@dataclass
class PrivateKeyAttributesV3(PropertyType):
    algorithm: str | None = None
    key_spec: str | None = None
    key_usage_property: KeyUsageProperty | None = None
    minimal_key_length: float | None = None
    crypto_providers: list[String] = field(default_factory=list)


@dataclass
class PrivateKeyAttributesV4(PropertyType):
    key_spec: str | None = None
    minimal_key_length: float | None = None
    algorithm: str | None = None
    crypto_providers: list[String] = field(default_factory=list)
    key_usage_property: KeyUsageProperty | None = None


@dataclass
class PrivateKeyFlagsV2(PropertyType):
    client_version: str | None = None
    exportable_key: bool | None = None
    strong_key_protection_required: bool | None = None


@dataclass
class PrivateKeyFlagsV3(PropertyType):
    client_version: str | None = None
    exportable_key: bool | None = None
    require_alternate_signature_algorithm: bool | None = None
    strong_key_protection_required: bool | None = None


@dataclass
class PrivateKeyFlagsV4(PropertyType):
    client_version: str | None = None
    exportable_key: bool | None = None
    require_alternate_signature_algorithm: bool | None = None
    require_same_key_renewal: bool | None = None
    strong_key_protection_required: bool | None = None
    use_legacy_provider: bool | None = None


@dataclass
class SubjectNameFlagsV2(PropertyType):
    require_common_name: bool | None = None
    require_directory_path: bool | None = None
    require_dns_as_cn: bool | None = None
    require_email: bool | None = None
    san_require_directory_guid: bool | None = None
    san_require_dns: bool | None = None
    san_require_domain_dns: bool | None = None
    san_require_email: bool | None = None
    san_require_spn: bool | None = None
    san_require_upn: bool | None = None


@dataclass
class SubjectNameFlagsV3(PropertyType):
    require_common_name: bool | None = None
    require_directory_path: bool | None = None
    require_dns_as_cn: bool | None = None
    require_email: bool | None = None
    san_require_directory_guid: bool | None = None
    san_require_dns: bool | None = None
    san_require_domain_dns: bool | None = None
    san_require_email: bool | None = None
    san_require_spn: bool | None = None
    san_require_upn: bool | None = None


@dataclass
class SubjectNameFlagsV4(PropertyType):
    require_common_name: bool | None = None
    require_directory_path: bool | None = None
    require_dns_as_cn: bool | None = None
    require_email: bool | None = None
    san_require_directory_guid: bool | None = None
    san_require_dns: bool | None = None
    san_require_domain_dns: bool | None = None
    san_require_email: bool | None = None
    san_require_spn: bool | None = None
    san_require_upn: bool | None = None


@dataclass
class TemplateDefinition(PropertyType):
    template_v2: TemplateV2 | None = None
    template_v3: TemplateV3 | None = None
    template_v4: TemplateV4 | None = None


@dataclass
class TemplateV2(PropertyType):
    certificate_validity: CertificateValidity | None = None
    enrollment_flags: EnrollmentFlagsV2 | None = None
    extensions: ExtensionsV2 | None = None
    general_flags: GeneralFlagsV2 | None = None
    private_key_attributes: PrivateKeyAttributesV2 | None = None
    private_key_flags: PrivateKeyFlagsV2 | None = None
    subject_name_flags: SubjectNameFlagsV2 | None = None
    superseded_templates: list[String] = field(default_factory=list)


@dataclass
class TemplateV3(PropertyType):
    certificate_validity: CertificateValidity | None = None
    enrollment_flags: EnrollmentFlagsV3 | None = None
    extensions: ExtensionsV3 | None = None
    general_flags: GeneralFlagsV3 | None = None
    hash_algorithm: str | None = None
    private_key_attributes: PrivateKeyAttributesV3 | None = None
    private_key_flags: PrivateKeyFlagsV3 | None = None
    subject_name_flags: SubjectNameFlagsV3 | None = None
    superseded_templates: list[String] = field(default_factory=list)


@dataclass
class TemplateV4(PropertyType):
    certificate_validity: CertificateValidity | None = None
    enrollment_flags: EnrollmentFlagsV4 | None = None
    extensions: ExtensionsV4 | None = None
    general_flags: GeneralFlagsV4 | None = None
    private_key_attributes: PrivateKeyAttributesV4 | None = None
    private_key_flags: PrivateKeyFlagsV4 | None = None
    subject_name_flags: SubjectNameFlagsV4 | None = None
    hash_algorithm: str | None = None
    superseded_templates: list[String] = field(default_factory=list)


@dataclass
class ValidityPeriod(PropertyType):
    period: float | None = None
    period_type: str | None = None
