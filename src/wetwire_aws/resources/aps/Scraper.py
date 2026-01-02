"""PropertyTypes for AWS::APS::Scraper."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmpConfiguration(PropertyType):
    workspace_arn: str | None = None


@dataclass
class CloudWatchLogDestination(PropertyType):
    log_group_arn: str | None = None


@dataclass
class ComponentConfig(PropertyType):
    options: dict[str, String] = field(default_factory=dict)


@dataclass
class Destination(PropertyType):
    amp_configuration: AmpConfiguration | None = None


@dataclass
class EksConfiguration(PropertyType):
    cluster_arn: str | None = None
    subnet_ids: list[String] = field(default_factory=list)
    security_group_ids: list[String] = field(default_factory=list)


@dataclass
class RoleConfiguration(PropertyType):
    source_role_arn: str | None = None
    target_role_arn: str | None = None


@dataclass
class ScrapeConfiguration(PropertyType):
    configuration_blob: str | None = None


@dataclass
class ScraperComponent(PropertyType):
    type_: str | None = None
    config: ComponentConfig | None = None


@dataclass
class ScraperLoggingConfiguration(PropertyType):
    logging_destination: ScraperLoggingDestination | None = None
    scraper_components: list[ScraperComponent] = field(default_factory=list)


@dataclass
class ScraperLoggingDestination(PropertyType):
    cloud_watch_logs: CloudWatchLogDestination | None = None


@dataclass
class Source(PropertyType):
    eks_configuration: EksConfiguration | None = None
    vpc_configuration: VpcConfiguration | None = None


@dataclass
class VpcConfiguration(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
