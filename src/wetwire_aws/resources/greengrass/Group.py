"""PropertyTypes for AWS::Greengrass::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GroupVersion(PropertyType):
    connector_definition_version_arn: DslValue[str] | None = None
    core_definition_version_arn: DslValue[str] | None = None
    device_definition_version_arn: DslValue[str] | None = None
    function_definition_version_arn: DslValue[str] | None = None
    logger_definition_version_arn: DslValue[str] | None = None
    resource_definition_version_arn: DslValue[str] | None = None
    subscription_definition_version_arn: DslValue[str] | None = None
