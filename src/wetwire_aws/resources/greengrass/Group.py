"""PropertyTypes for AWS::Greengrass::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GroupVersion(PropertyType):
    connector_definition_version_arn: str | None = None
    core_definition_version_arn: str | None = None
    device_definition_version_arn: str | None = None
    function_definition_version_arn: str | None = None
    logger_definition_version_arn: str | None = None
    resource_definition_version_arn: str | None = None
    subscription_definition_version_arn: str | None = None
