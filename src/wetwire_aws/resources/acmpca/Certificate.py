"""PropertyTypes for AWS::ACMPCA::Certificate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApiPassthrough(PropertyType):
    extensions: DslValue[Extensions] | None = None
    subject: DslValue[Subject] | None = None


@dataclass
class CustomAttribute(PropertyType):
    object_identifier: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class CustomExtension(PropertyType):
    object_identifier: DslValue[str] | None = None
    value: DslValue[str] | None = None
    critical: DslValue[bool] | None = None


@dataclass
class EdiPartyName(PropertyType):
    name_assigner: DslValue[str] | None = None
    party_name: DslValue[str] | None = None


@dataclass
class ExtendedKeyUsage(PropertyType):
    extended_key_usage_object_identifier: DslValue[str] | None = None
    extended_key_usage_type: DslValue[str] | None = None


@dataclass
class Extensions(PropertyType):
    certificate_policies: list[DslValue[PolicyInformation]] = field(
        default_factory=list
    )
    custom_extensions: list[DslValue[CustomExtension]] = field(default_factory=list)
    extended_key_usage: list[DslValue[ExtendedKeyUsage]] = field(default_factory=list)
    key_usage: DslValue[KeyUsage] | None = None
    subject_alternative_names: list[DslValue[GeneralName]] = field(default_factory=list)


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
class OtherName(PropertyType):
    type_id: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class PolicyInformation(PropertyType):
    cert_policy_id: DslValue[str] | None = None
    policy_qualifiers: list[DslValue[PolicyQualifierInfo]] = field(default_factory=list)


@dataclass
class PolicyQualifierInfo(PropertyType):
    policy_qualifier_id: DslValue[str] | None = None
    qualifier: DslValue[Qualifier] | None = None


@dataclass
class Qualifier(PropertyType):
    cps_uri: DslValue[str] | None = None


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


@dataclass
class Validity(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[float] | None = None
