"""PropertyTypes for AWS::RUM::AppMonitor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppMonitorConfiguration(PropertyType):
    allow_cookies: bool | None = None
    enable_x_ray: bool | None = None
    excluded_pages: list[String] = field(default_factory=list)
    favorite_pages: list[String] = field(default_factory=list)
    guest_role_arn: str | None = None
    identity_pool_id: str | None = None
    included_pages: list[String] = field(default_factory=list)
    metric_destinations: list[MetricDestination] = field(default_factory=list)
    session_sample_rate: float | None = None
    telemetries: list[String] = field(default_factory=list)


@dataclass
class CustomEvents(PropertyType):
    status: str | None = None


@dataclass
class DeobfuscationConfiguration(PropertyType):
    java_script_source_maps: JavaScriptSourceMaps | None = None


@dataclass
class JavaScriptSourceMaps(PropertyType):
    status: str | None = None
    s3_uri: str | None = None


@dataclass
class MetricDefinition(PropertyType):
    name: str | None = None
    dimension_keys: dict[str, String] = field(default_factory=dict)
    event_pattern: str | None = None
    namespace: str | None = None
    unit_label: str | None = None
    value_key: str | None = None


@dataclass
class MetricDestination(PropertyType):
    destination: str | None = None
    destination_arn: str | None = None
    iam_role_arn: str | None = None
    metric_definitions: list[MetricDefinition] = field(default_factory=list)


@dataclass
class ResourcePolicy(PropertyType):
    policy_document: str | None = None
    policy_revision_id: str | None = None
