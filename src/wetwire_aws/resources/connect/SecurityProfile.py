"""PropertyTypes for AWS::Connect::SecurityProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Application(PropertyType):
    application_permissions: list[String] = field(default_factory=list)
    namespace: str | None = None


@dataclass
class DataTableAccessControlConfiguration(PropertyType):
    primary_attribute_access_control_configuration: (
        PrimaryAttributeAccessControlConfigurationItem | None
    ) = None


@dataclass
class GranularAccessControlConfiguration(PropertyType):
    data_table_access_control_configuration: (
        DataTableAccessControlConfiguration | None
    ) = None


@dataclass
class PrimaryAttributeAccessControlConfigurationItem(PropertyType):
    primary_attribute_values: list[PrimaryAttributeValue] = field(default_factory=list)


@dataclass
class PrimaryAttributeValue(PropertyType):
    access_type: str | None = None
    attribute_name: str | None = None
    values: list[String] = field(default_factory=list)
