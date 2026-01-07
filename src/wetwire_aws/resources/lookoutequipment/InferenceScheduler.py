"""PropertyTypes for AWS::LookoutEquipment::InferenceScheduler."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataInputConfiguration(PropertyType):
    s3_input_configuration: DslValue[S3InputConfiguration] | None = None
    inference_input_name_configuration: DslValue[InputNameConfiguration] | None = None
    input_time_zone_offset: DslValue[str] | None = None


@dataclass
class DataOutputConfiguration(PropertyType):
    s3_output_configuration: DslValue[S3OutputConfiguration] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class InputNameConfiguration(PropertyType):
    component_timestamp_delimiter: DslValue[str] | None = None
    timestamp_format: DslValue[str] | None = None


@dataclass
class S3InputConfiguration(PropertyType):
    bucket: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class S3OutputConfiguration(PropertyType):
    bucket: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
