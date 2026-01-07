"""PropertyTypes for AWS::BedrockAgentCore::CodeInterpreterCustom."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CodeInterpreterNetworkConfiguration(PropertyType):
    network_mode: DslValue[str] | None = None
    vpc_config: DslValue[VpcConfig] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_groups: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
