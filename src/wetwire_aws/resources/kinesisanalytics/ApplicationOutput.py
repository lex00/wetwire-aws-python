"""PropertyTypes for AWS::KinesisAnalytics::ApplicationOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DestinationSchema(PropertyType):
    record_format_type: DslValue[str] | None = None


@dataclass
class KinesisFirehoseOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class KinesisStreamsOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class LambdaOutput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class Output(PropertyType):
    destination_schema: DslValue[DestinationSchema] | None = None
    kinesis_firehose_output: DslValue[KinesisFirehoseOutput] | None = None
    kinesis_streams_output: DslValue[KinesisStreamsOutput] | None = None
    lambda_output: DslValue[LambdaOutput] | None = None
    name: DslValue[str] | None = None
