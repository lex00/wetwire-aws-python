"""PropertyTypes for AWS::ServiceCatalog::CloudFormationProduct."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CodeStarParameters(PropertyType):
    artifact_path: str | None = None
    branch: str | None = None
    connection_arn: str | None = None
    repository: str | None = None


@dataclass
class ConnectionParameters(PropertyType):
    code_star: CodeStarParameters | None = None


@dataclass
class ProvisioningArtifactProperties(PropertyType):
    info: dict[str, Any] | None = None
    description: str | None = None
    disable_template_validation: bool | None = None
    name: str | None = None
    type_: str | None = None


@dataclass
class SourceConnection(PropertyType):
    connection_parameters: ConnectionParameters | None = None
    type_: str | None = None
