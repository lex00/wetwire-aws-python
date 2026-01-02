"""PropertyTypes for AWS::ACMPCA::CertificateAuthority."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessDescription(PropertyType):
    access_location: GeneralName | None = None
    access_method: AccessMethod | None = None


@dataclass
class AccessMethod(PropertyType):
    access_method_type: str | None = None
    custom_object_identifier: str | None = None


@dataclass
class CrlConfiguration(PropertyType):
    enabled: bool | None = None
    crl_distribution_point_extension_configuration: (
        CrlDistributionPointExtensionConfiguration | None
    ) = None
    crl_type: str | None = None
    custom_cname: str | None = None
    custom_path: str | None = None
    expiration_in_days: int | None = None
    s3_bucket_name: str | None = None
    s3_object_acl: str | None = None


@dataclass
class CrlDistributionPointExtensionConfiguration(PropertyType):
    omit_extension: bool | None = None


@dataclass
class CsrExtensions(PropertyType):
    key_usage: KeyUsage | None = None
    subject_information_access: list[AccessDescription] = field(default_factory=list)


@dataclass
class CustomAttribute(PropertyType):
    object_identifier: str | None = None
    value: str | None = None


@dataclass
class EdiPartyName(PropertyType):
    party_name: str | None = None
    name_assigner: str | None = None


@dataclass
class GeneralName(PropertyType):
    directory_name: Subject | None = None
    dns_name: str | None = None
    edi_party_name: EdiPartyName | None = None
    ip_address: str | None = None
    other_name: OtherName | None = None
    registered_id: str | None = None
    rfc822_name: str | None = None
    uniform_resource_identifier: str | None = None


@dataclass
class KeyUsage(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "crl_sign": "CRLSign",
    }

    crl_sign: bool | None = None
    data_encipherment: bool | None = None
    decipher_only: bool | None = None
    digital_signature: bool | None = None
    encipher_only: bool | None = None
    key_agreement: bool | None = None
    key_cert_sign: bool | None = None
    key_encipherment: bool | None = None
    non_repudiation: bool | None = None


@dataclass
class OcspConfiguration(PropertyType):
    enabled: bool | None = None
    ocsp_custom_cname: str | None = None


@dataclass
class OtherName(PropertyType):
    type_id: str | None = None
    value: str | None = None


@dataclass
class RevocationConfiguration(PropertyType):
    crl_configuration: CrlConfiguration | None = None
    ocsp_configuration: OcspConfiguration | None = None


@dataclass
class Subject(PropertyType):
    common_name: str | None = None
    country: str | None = None
    custom_attributes: list[CustomAttribute] = field(default_factory=list)
    distinguished_name_qualifier: str | None = None
    generation_qualifier: str | None = None
    given_name: str | None = None
    initials: str | None = None
    locality: str | None = None
    organization: str | None = None
    organizational_unit: str | None = None
    pseudonym: str | None = None
    serial_number: str | None = None
    state: str | None = None
    surname: str | None = None
    title: str | None = None
