"""PropertyTypes for AWS::SecurityLake::Subscriber."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AwsLogSource(PropertyType):
    source_name: DslValue[str] | None = None
    source_version: DslValue[str] | None = None


@dataclass
class CustomLogSource(PropertyType):
    source_name: DslValue[str] | None = None
    source_version: DslValue[str] | None = None


@dataclass
class Source(PropertyType):
    aws_log_source: DslValue[AwsLogSource] | None = None
    custom_log_source: DslValue[CustomLogSource] | None = None


@dataclass
class SubscriberIdentity(PropertyType):
    external_id: DslValue[str] | None = None
    principal: DslValue[str] | None = None
