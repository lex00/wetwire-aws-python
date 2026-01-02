"""PropertyTypes for AWS::LookoutEquipment::InferenceScheduler."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataInputConfiguration(PropertyType):
    s3_input_configuration: S3InputConfiguration | None = None
    inference_input_name_configuration: InputNameConfiguration | None = None
    input_time_zone_offset: str | None = None


@dataclass
class DataOutputConfiguration(PropertyType):
    s3_output_configuration: S3OutputConfiguration | None = None
    kms_key_id: str | None = None


@dataclass
class InputNameConfiguration(PropertyType):
    component_timestamp_delimiter: str | None = None
    timestamp_format: str | None = None


@dataclass
class S3InputConfiguration(PropertyType):
    bucket: str | None = None
    prefix: str | None = None


@dataclass
class S3OutputConfiguration(PropertyType):
    bucket: str | None = None
    prefix: str | None = None
