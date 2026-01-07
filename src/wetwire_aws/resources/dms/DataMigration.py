"""PropertyTypes for AWS::DMS::DataMigration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataMigrationSettings(PropertyType):
    cloudwatch_logs_enabled: DslValue[bool] | None = None
    number_of_jobs: DslValue[int] | None = None
    selection_rules: DslValue[str] | None = None


@dataclass
class SourceDataSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cdc_start_position": "CDCStartPosition",
        "cdc_start_time": "CDCStartTime",
        "cdc_stop_time": "CDCStopTime",
    }

    cdc_start_position: DslValue[str] | None = None
    cdc_start_time: DslValue[str] | None = None
    cdc_stop_time: DslValue[str] | None = None
    slot_name: DslValue[str] | None = None
