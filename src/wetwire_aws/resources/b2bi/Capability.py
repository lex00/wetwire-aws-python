"""PropertyTypes for AWS::B2BI::Capability."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapabilityConfiguration(PropertyType):
    edi: DslValue[EdiConfiguration] | None = None


@dataclass
class EdiConfiguration(PropertyType):
    input_location: DslValue[S3Location] | None = None
    output_location: DslValue[S3Location] | None = None
    transformer_id: DslValue[str] | None = None
    type_: DslValue[EdiType] | None = None
    capability_direction: DslValue[str] | None = None


@dataclass
class EdiType(PropertyType):
    x12_details: DslValue[X12Details] | None = None


@dataclass
class S3Location(PropertyType):
    bucket_name: DslValue[str] | None = None
    key: DslValue[str] | None = None


@dataclass
class X12Details(PropertyType):
    transaction_set: DslValue[str] | None = None
    version: DslValue[str] | None = None
