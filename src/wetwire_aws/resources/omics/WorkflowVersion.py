"""PropertyTypes for AWS::Omics::WorkflowVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ContainerRegistryMap(PropertyType):
    image_mappings: list[DslValue[ImageMapping]] = field(default_factory=list)
    registry_mappings: list[DslValue[RegistryMapping]] = field(default_factory=list)


@dataclass
class DefinitionRepository(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_arn": "connectionArn",
        "exclude_file_patterns": "excludeFilePatterns",
        "full_repository_id": "fullRepositoryId",
        "source_reference": "sourceReference",
    }

    connection_arn: DslValue[str] | None = None
    exclude_file_patterns: list[DslValue[str]] = field(default_factory=list)
    full_repository_id: DslValue[str] | None = None
    source_reference: DslValue[SourceReference] | None = None


@dataclass
class ImageMapping(PropertyType):
    destination_image: DslValue[str] | None = None
    source_image: DslValue[str] | None = None


@dataclass
class RegistryMapping(PropertyType):
    ecr_account_id: DslValue[str] | None = None
    ecr_repository_prefix: DslValue[str] | None = None
    upstream_registry_url: DslValue[str] | None = None
    upstream_repository_prefix: DslValue[str] | None = None


@dataclass
class SourceReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "type",
        "value": "value",
    }

    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class WorkflowParameter(PropertyType):
    description: DslValue[str] | None = None
    optional: DslValue[bool] | None = None
