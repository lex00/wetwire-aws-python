"""PropertyTypes for AWS::CodePipeline::CustomActionType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ArtifactDetails(PropertyType):
    maximum_count: int | None = None
    minimum_count: int | None = None


@dataclass
class ConfigurationProperties(PropertyType):
    key: bool | None = None
    name: str | None = None
    required: bool | None = None
    secret: bool | None = None
    description: str | None = None
    queryable: bool | None = None
    type_: str | None = None


@dataclass
class Settings(PropertyType):
    entity_url_template: str | None = None
    execution_url_template: str | None = None
    revision_url_template: str | None = None
    third_party_configuration_url: str | None = None
