"""PropertyTypes for AWS::BedrockAgentCore::CodeInterpreterCustom."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CodeInterpreterNetworkConfiguration(PropertyType):
    network_mode: str | None = None
    vpc_config: VpcConfig | None = None


@dataclass
class VpcConfig(PropertyType):
    security_groups: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
