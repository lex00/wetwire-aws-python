"""PropertyTypes for AWS::ElasticBeanstalk::ConfigurationTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationOptionSetting(PropertyType):
    namespace: DslValue[str] | None = None
    option_name: DslValue[str] | None = None
    resource_name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SourceConfiguration(PropertyType):
    application_name: DslValue[str] | None = None
    template_name: DslValue[str] | None = None
