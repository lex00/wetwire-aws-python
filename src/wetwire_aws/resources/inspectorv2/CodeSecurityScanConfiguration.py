"""PropertyTypes for AWS::InspectorV2::CodeSecurityScanConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CodeSecurityScanConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "continuous_integration_scan_configuration": "continuousIntegrationScanConfiguration",
        "periodic_scan_configuration": "periodicScanConfiguration",
        "rule_set_categories": "ruleSetCategories",
    }

    rule_set_categories: list[String] = field(default_factory=list)
    continuous_integration_scan_configuration: (
        ContinuousIntegrationScanConfiguration | None
    ) = None
    periodic_scan_configuration: PeriodicScanConfiguration | None = None


@dataclass
class ContinuousIntegrationScanConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "supported_events": "supportedEvents",
    }

    supported_events: list[String] = field(default_factory=list)


@dataclass
class PeriodicScanConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "frequency": "frequency",
        "frequency_expression": "frequencyExpression",
    }

    frequency: str | None = None
    frequency_expression: str | None = None


@dataclass
class ScopeSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "project_selection_scope": "projectSelectionScope",
    }

    project_selection_scope: str | None = None
