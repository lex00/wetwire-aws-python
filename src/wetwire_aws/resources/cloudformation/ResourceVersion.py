"""PropertyTypes for AWS::CloudFormation::ResourceVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoggingConfig(PropertyType):
    log_group_name: str | None = None
    log_role_arn: str | None = None
