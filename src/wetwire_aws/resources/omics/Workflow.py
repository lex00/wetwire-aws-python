"""PropertyTypes for AWS::Omics::Workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ContainerRegistryMap(PropertyType):
    image_mappings: list[ImageMapping] = field(default_factory=list)
    registry_mappings: list[RegistryMapping] = field(default_factory=list)


@dataclass
class DefinitionRepository(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "connection_arn": "connectionArn",
        "exclude_file_patterns": "excludeFilePatterns",
        "full_repository_id": "fullRepositoryId",
        "source_reference": "sourceReference",
    }

    connection_arn: str | None = None
    exclude_file_patterns: list[String] = field(default_factory=list)
    full_repository_id: str | None = None
    source_reference: SourceReference | None = None


@dataclass
class ImageMapping(PropertyType):
    destination_image: str | None = None
    source_image: str | None = None


@dataclass
class RegistryMapping(PropertyType):
    ecr_account_id: str | None = None
    ecr_repository_prefix: str | None = None
    upstream_registry_url: str | None = None
    upstream_repository_prefix: str | None = None


@dataclass
class SourceReference(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "type_": "type",
        "value": "value",
    }

    type_: str | None = None
    value: str | None = None


@dataclass
class WorkflowParameter(PropertyType):
    description: str | None = None
    optional: bool | None = None
