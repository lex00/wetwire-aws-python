"""PropertyTypes for AWS::CleanRooms::IdMappingTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IdMappingTableInputReferenceConfig(PropertyType):
    input_reference_arn: str | None = None
    manage_resource_policies: bool | None = None


@dataclass
class IdMappingTableInputReferenceProperties(PropertyType):
    id_mapping_table_input_source: list[IdMappingTableInputSource] = field(
        default_factory=list
    )


@dataclass
class IdMappingTableInputSource(PropertyType):
    id_namespace_association_id: str | None = None
    type_: str | None = None
