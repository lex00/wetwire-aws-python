"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DestinationSchema(PropertyType):
    record_format_type: str | None = None


@dataclass
class KinesisFirehoseOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: str | None = None


@dataclass
class KinesisStreamsOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: str | None = None


@dataclass
class LambdaOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: str | None = None


@dataclass
class Output(PropertyType):
    destination_schema: DestinationSchema | None = None
    kinesis_firehose_output: KinesisFirehoseOutput | None = None
    kinesis_streams_output: KinesisStreamsOutput | None = None
    lambda_output: LambdaOutput | None = None
    name: str | None = None
