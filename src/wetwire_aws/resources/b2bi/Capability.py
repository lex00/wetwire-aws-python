"""PropertyTypes for AWS::B2BI::Capability."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapabilityConfiguration(PropertyType):
    edi: EdiConfiguration | None = None


@dataclass
class EdiConfiguration(PropertyType):
    input_location: S3Location | None = None
    output_location: S3Location | None = None
    transformer_id: str | None = None
    type_: EdiType | None = None
    capability_direction: str | None = None


@dataclass
class EdiType(PropertyType):
    x12_details: X12Details | None = None


@dataclass
class S3Location(PropertyType):
    bucket_name: str | None = None
    key: str | None = None


@dataclass
class X12Details(PropertyType):
    transaction_set: str | None = None
    version: str | None = None
