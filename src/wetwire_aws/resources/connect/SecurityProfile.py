"""PropertyTypes for AWS::Connect::SecurityProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Application(PropertyType):
    application_permissions: list[DslValue[str]] = field(default_factory=list)
    namespace: DslValue[str] | None = None


@dataclass
class DataTableAccessControlConfiguration(PropertyType):
    primary_attribute_access_control_configuration: (
        DslValue[PrimaryAttributeAccessControlConfigurationItem] | None
    ) = None


@dataclass
class GranularAccessControlConfiguration(PropertyType):
    data_table_access_control_configuration: (
        DslValue[DataTableAccessControlConfiguration] | None
    ) = None


@dataclass
class PrimaryAttributeAccessControlConfigurationItem(PropertyType):
    primary_attribute_values: list[DslValue[PrimaryAttributeValue]] = field(
        default_factory=list
    )


@dataclass
class PrimaryAttributeValue(PropertyType):
    access_type: DslValue[str] | None = None
    attribute_name: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)
