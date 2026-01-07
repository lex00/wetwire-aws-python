"""PropertyTypes for AWS::ServiceCatalog::CloudFormationProduct."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CodeStarParameters(PropertyType):
    artifact_path: DslValue[str] | None = None
    branch: DslValue[str] | None = None
    connection_arn: DslValue[str] | None = None
    repository: DslValue[str] | None = None


@dataclass
class ConnectionParameters(PropertyType):
    code_star: DslValue[CodeStarParameters] | None = None


@dataclass
class ProvisioningArtifactProperties(PropertyType):
    info: DslValue[dict[str, Any]] | None = None
    description: DslValue[str] | None = None
    disable_template_validation: DslValue[bool] | None = None
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class SourceConnection(PropertyType):
    connection_parameters: DslValue[ConnectionParameters] | None = None
    type_: DslValue[str] | None = None
