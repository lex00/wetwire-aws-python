"""PropertyTypes for AWS::ACMPCA::CertificateAuthority."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessDescription(PropertyType):
    access_location: DslValue[GeneralName] | None = None
    access_method: DslValue[AccessMethod] | None = None


@dataclass
class AccessMethod(PropertyType):
    access_method_type: DslValue[str] | None = None
    custom_object_identifier: DslValue[str] | None = None


@dataclass
class CrlConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    crl_distribution_point_extension_configuration: (
        DslValue[CrlDistributionPointExtensionConfiguration] | None
    ) = None
    crl_type: DslValue[str] | None = None
    custom_cname: DslValue[str] | None = None
    custom_path: DslValue[str] | None = None
    expiration_in_days: DslValue[int] | None = None
    s3_bucket_name: DslValue[str] | None = None
    s3_object_acl: DslValue[str] | None = None


@dataclass
class CrlDistributionPointExtensionConfiguration(PropertyType):
    omit_extension: DslValue[bool] | None = None


@dataclass
class CsrExtensions(PropertyType):
    key_usage: DslValue[KeyUsage] | None = None
    subject_information_access: list[DslValue[AccessDescription]] = field(
        default_factory=list
    )


@dataclass
class CustomAttribute(PropertyType):
    object_identifier: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EdiPartyName(PropertyType):
    party_name: DslValue[str] | None = None
    name_assigner: DslValue[str] | None = None


@dataclass
class GeneralName(PropertyType):
    directory_name: DslValue[Subject] | None = None
    dns_name: DslValue[str] | None = None
    edi_party_name: DslValue[EdiPartyName] | None = None
    ip_address: DslValue[str] | None = None
    other_name: DslValue[OtherName] | None = None
    registered_id: DslValue[str] | None = None
    rfc822_name: DslValue[str] | None = None
    uniform_resource_identifier: DslValue[str] | None = None


@dataclass
class KeyUsage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "crl_sign": "CRLSign",
    }

    crl_sign: DslValue[bool] | None = None
    data_encipherment: DslValue[bool] | None = None
    decipher_only: DslValue[bool] | None = None
    digital_signature: DslValue[bool] | None = None
    encipher_only: DslValue[bool] | None = None
    key_agreement: DslValue[bool] | None = None
    key_cert_sign: DslValue[bool] | None = None
    key_encipherment: DslValue[bool] | None = None
    non_repudiation: DslValue[bool] | None = None


@dataclass
class OcspConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    ocsp_custom_cname: DslValue[str] | None = None


@dataclass
class OtherName(PropertyType):
    type_id: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class RevocationConfiguration(PropertyType):
    crl_configuration: DslValue[CrlConfiguration] | None = None
    ocsp_configuration: DslValue[OcspConfiguration] | None = None


@dataclass
class Subject(PropertyType):
    common_name: DslValue[str] | None = None
    country: DslValue[str] | None = None
    custom_attributes: list[DslValue[CustomAttribute]] = field(default_factory=list)
    distinguished_name_qualifier: DslValue[str] | None = None
    generation_qualifier: DslValue[str] | None = None
    given_name: DslValue[str] | None = None
    initials: DslValue[str] | None = None
    locality: DslValue[str] | None = None
    organization: DslValue[str] | None = None
    organizational_unit: DslValue[str] | None = None
    pseudonym: DslValue[str] | None = None
    serial_number: DslValue[str] | None = None
    state: DslValue[str] | None = None
    surname: DslValue[str] | None = None
    title: DslValue[str] | None = None
