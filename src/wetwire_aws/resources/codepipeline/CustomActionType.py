"""PropertyTypes for AWS::CodePipeline::CustomActionType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ArtifactDetails(PropertyType):
    maximum_count: DslValue[int] | None = None
    minimum_count: DslValue[int] | None = None


@dataclass
class ConfigurationProperties(PropertyType):
    key: DslValue[bool] | None = None
    name: DslValue[str] | None = None
    required: DslValue[bool] | None = None
    secret: DslValue[bool] | None = None
    description: DslValue[str] | None = None
    queryable: DslValue[bool] | None = None
    type_: DslValue[str] | None = None


@dataclass
class Settings(PropertyType):
    entity_url_template: DslValue[str] | None = None
    execution_url_template: DslValue[str] | None = None
    revision_url_template: DslValue[str] | None = None
    third_party_configuration_url: DslValue[str] | None = None
