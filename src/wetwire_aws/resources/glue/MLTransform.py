"""PropertyTypes for AWS::Glue::MLTransform."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FindMatchesParameters(PropertyType):
    primary_key_column_name: str | None = None
    accuracy_cost_tradeoff: float | None = None
    enforce_provided_labels: bool | None = None
    precision_recall_tradeoff: float | None = None


@dataclass
class GlueTables(PropertyType):
    database_name: str | None = None
    table_name: str | None = None
    catalog_id: str | None = None
    connection_name: str | None = None


@dataclass
class InputRecordTables(PropertyType):
    glue_tables: list[GlueTables] = field(default_factory=list)


@dataclass
class MLUserDataEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_user_data_encryption_mode": "MLUserDataEncryptionMode",
    }

    ml_user_data_encryption_mode: str | None = None
    kms_key_id: str | None = None


@dataclass
class TransformEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_user_data_encryption": "MLUserDataEncryption",
    }

    ml_user_data_encryption: MLUserDataEncryption | None = None
    task_run_security_configuration_name: str | None = None


@dataclass
class TransformParameters(PropertyType):
    transform_type: str | None = None
    find_matches_parameters: FindMatchesParameters | None = None
