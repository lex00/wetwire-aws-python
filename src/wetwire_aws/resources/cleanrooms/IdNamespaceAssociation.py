"""PropertyTypes for AWS::CleanRooms::IdNamespaceAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IdMappingConfig(PropertyType):
    allow_use_as_dimension_column: DslValue[bool] | None = None


@dataclass
class IdNamespaceAssociationInputReferenceConfig(PropertyType):
    input_reference_arn: DslValue[str] | None = None
    manage_resource_policies: DslValue[bool] | None = None


@dataclass
class IdNamespaceAssociationInputReferenceProperties(PropertyType):
    id_mapping_workflows_supported: list[DslValue[dict[str, Any]]] = field(
        default_factory=list
    )
    id_namespace_type: DslValue[str] | None = None
