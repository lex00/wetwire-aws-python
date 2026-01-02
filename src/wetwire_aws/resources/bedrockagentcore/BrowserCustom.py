"""PropertyTypes for AWS::BedrockAgentCore::BrowserCustom."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BrowserNetworkConfiguration(PropertyType):
    network_mode: str | None = None
    vpc_config: VpcConfig | None = None


@dataclass
class BrowserSigning(PropertyType):
    enabled: bool | None = None


@dataclass
class RecordingConfig(PropertyType):
    enabled: bool | None = None
    s3_location: S3Location | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    prefix: str | None = None


@dataclass
class VpcConfig(PropertyType):
    security_groups: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
