"""PropertyTypes for AWS::Glue::DataQualityRuleset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataQualityTargetTable(PropertyType):
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
