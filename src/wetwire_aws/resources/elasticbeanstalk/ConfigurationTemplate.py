"""PropertyTypes for AWS::ElasticBeanstalk::ConfigurationTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationOptionSetting(PropertyType):
    namespace: str | None = None
    option_name: str | None = None
    resource_name: str | None = None
    value: str | None = None


@dataclass
class SourceConfiguration(PropertyType):
    application_name: str | None = None
    template_name: str | None = None
