"""PropertyTypes for AWS::DMS::DataMigration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataMigrationSettings(PropertyType):
    cloudwatch_logs_enabled: bool | None = None
    number_of_jobs: int | None = None
    selection_rules: str | None = None


@dataclass
class SourceDataSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cdc_start_position": "CDCStartPosition",
        "cdc_start_time": "CDCStartTime",
        "cdc_stop_time": "CDCStopTime",
    }

    cdc_start_position: str | None = None
    cdc_start_time: str | None = None
    cdc_stop_time: str | None = None
    slot_name: str | None = None
