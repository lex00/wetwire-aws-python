"""PropertyTypes for AWS::SecurityLake::Subscriber."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AwsLogSource(PropertyType):
    source_name: str | None = None
    source_version: str | None = None


@dataclass
class CustomLogSource(PropertyType):
    source_name: str | None = None
    source_version: str | None = None


@dataclass
class Source(PropertyType):
    aws_log_source: AwsLogSource | None = None
    custom_log_source: CustomLogSource | None = None


@dataclass
class SubscriberIdentity(PropertyType):
    external_id: str | None = None
    principal: str | None = None
