"""PropertyTypes for AWS::CleanRooms::IdMappingTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IdMappingTableInputReferenceConfig(PropertyType):
    input_reference_arn: DslValue[str] | None = None
    manage_resource_policies: DslValue[bool] | None = None


@dataclass
class IdMappingTableInputReferenceProperties(PropertyType):
    id_mapping_table_input_source: list[DslValue[IdMappingTableInputSource]] = field(
        default_factory=list
    )


@dataclass
class IdMappingTableInputSource(PropertyType):
    id_namespace_association_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
