"""PropertyTypes for AWS::APS::Scraper."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmpConfiguration(PropertyType):
    workspace_arn: DslValue[str] | None = None


@dataclass
class CloudWatchLogDestination(PropertyType):
    log_group_arn: DslValue[str] | None = None


@dataclass
class ComponentConfig(PropertyType):
    options: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class Destination(PropertyType):
    amp_configuration: DslValue[AmpConfiguration] | None = None


@dataclass
class EksConfiguration(PropertyType):
    cluster_arn: DslValue[str] | None = None
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    security_group_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RoleConfiguration(PropertyType):
    source_role_arn: DslValue[str] | None = None
    target_role_arn: DslValue[str] | None = None


@dataclass
class ScrapeConfiguration(PropertyType):
    configuration_blob: DslValue[str] | None = None


@dataclass
class ScraperComponent(PropertyType):
    type_: DslValue[str] | None = None
    config: DslValue[ComponentConfig] | None = None


@dataclass
class ScraperLoggingConfiguration(PropertyType):
    logging_destination: DslValue[ScraperLoggingDestination] | None = None
    scraper_components: list[DslValue[ScraperComponent]] = field(default_factory=list)


@dataclass
class ScraperLoggingDestination(PropertyType):
    cloud_watch_logs: DslValue[CloudWatchLogDestination] | None = None


@dataclass
class Source(PropertyType):
    eks_configuration: DslValue[EksConfiguration] | None = None
    vpc_configuration: DslValue[VpcConfiguration] | None = None


@dataclass
class VpcConfiguration(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
