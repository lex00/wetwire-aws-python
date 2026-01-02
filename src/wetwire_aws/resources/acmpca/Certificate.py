"""PropertyTypes for AWS::ACMPCA::Certificate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApiPassthrough(PropertyType):
    extensions: Extensions | None = None
    subject: Subject | None = None


@dataclass
class CustomAttribute(PropertyType):
    object_identifier: str | None = None
    value: str | None = None


@dataclass
class CustomExtension(PropertyType):
    object_identifier: str | None = None
    value: str | None = None
    critical: bool | None = None


@dataclass
class EdiPartyName(PropertyType):
    name_assigner: str | None = None
    party_name: str | None = None


@dataclass
class ExtendedKeyUsage(PropertyType):
    extended_key_usage_object_identifier: str | None = None
    extended_key_usage_type: str | None = None


@dataclass
class Extensions(PropertyType):
    certificate_policies: list[PolicyInformation] = field(default_factory=list)
    custom_extensions: list[CustomExtension] = field(default_factory=list)
    extended_key_usage: list[ExtendedKeyUsage] = field(default_factory=list)
    key_usage: KeyUsage | None = None
    subject_alternative_names: list[GeneralName] = field(default_factory=list)


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
class OtherName(PropertyType):
    type_id: str | None = None
    value: str | None = None


@dataclass
class PolicyInformation(PropertyType):
    cert_policy_id: str | None = None
    policy_qualifiers: list[PolicyQualifierInfo] = field(default_factory=list)


@dataclass
class PolicyQualifierInfo(PropertyType):
    policy_qualifier_id: str | None = None
    qualifier: Qualifier | None = None


@dataclass
class Qualifier(PropertyType):
    cps_uri: str | None = None


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


@dataclass
class Validity(PropertyType):
    type_: str | None = None
    value: float | None = None
