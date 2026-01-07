"""PropertyTypes for AWS::MediaPackage::PackagingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Authorization(PropertyType):
    cdn_identifier_secret: DslValue[str] | None = None
    secrets_role_arn: DslValue[str] | None = None


@dataclass
class LogConfiguration(PropertyType):
    log_group_name: DslValue[str] | None = None
