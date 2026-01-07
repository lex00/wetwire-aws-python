"""PropertyTypes for AWS::RUM::AppMonitor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppMonitorConfiguration(PropertyType):
    allow_cookies: DslValue[bool] | None = None
    enable_x_ray: DslValue[bool] | None = None
    excluded_pages: list[DslValue[str]] = field(default_factory=list)
    favorite_pages: list[DslValue[str]] = field(default_factory=list)
    guest_role_arn: DslValue[str] | None = None
    identity_pool_id: DslValue[str] | None = None
    included_pages: list[DslValue[str]] = field(default_factory=list)
    metric_destinations: list[DslValue[MetricDestination]] = field(default_factory=list)
    session_sample_rate: DslValue[float] | None = None
    telemetries: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CustomEvents(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class DeobfuscationConfiguration(PropertyType):
    java_script_source_maps: DslValue[JavaScriptSourceMaps] | None = None


@dataclass
class JavaScriptSourceMaps(PropertyType):
    status: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None


@dataclass
class MetricDefinition(PropertyType):
    name: DslValue[str] | None = None
    dimension_keys: dict[str, DslValue[str]] = field(default_factory=dict)
    event_pattern: DslValue[str] | None = None
    namespace: DslValue[str] | None = None
    unit_label: DslValue[str] | None = None
    value_key: DslValue[str] | None = None


@dataclass
class MetricDestination(PropertyType):
    destination: DslValue[str] | None = None
    destination_arn: DslValue[str] | None = None
    iam_role_arn: DslValue[str] | None = None
    metric_definitions: list[DslValue[MetricDefinition]] = field(default_factory=list)


@dataclass
class ResourcePolicy(PropertyType):
    policy_document: DslValue[str] | None = None
    policy_revision_id: DslValue[str] | None = None
