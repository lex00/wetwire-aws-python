"""PropertyTypes for AWS::BedrockAgentCore::BrowserCustom."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BrowserNetworkConfiguration(PropertyType):
    network_mode: DslValue[str] | None = None
    vpc_config: DslValue[VpcConfig] | None = None


@dataclass
class BrowserSigning(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class RecordingConfig(PropertyType):
    enabled: DslValue[bool] | None = None
    s3_location: DslValue[S3Location] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_groups: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
