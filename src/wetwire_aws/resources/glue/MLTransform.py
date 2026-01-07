"""PropertyTypes for AWS::Glue::MLTransform."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FindMatchesParameters(PropertyType):
    primary_key_column_name: DslValue[str] | None = None
    accuracy_cost_tradeoff: DslValue[float] | None = None
    enforce_provided_labels: DslValue[bool] | None = None
    precision_recall_tradeoff: DslValue[float] | None = None


@dataclass
class GlueTables(PropertyType):
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    catalog_id: DslValue[str] | None = None
    connection_name: DslValue[str] | None = None


@dataclass
class InputRecordTables(PropertyType):
    glue_tables: list[DslValue[GlueTables]] = field(default_factory=list)


@dataclass
class MLUserDataEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_user_data_encryption_mode": "MLUserDataEncryptionMode",
    }

    ml_user_data_encryption_mode: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class TransformEncryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_user_data_encryption": "MLUserDataEncryption",
    }

    ml_user_data_encryption: DslValue[MLUserDataEncryption] | None = None
    task_run_security_configuration_name: DslValue[str] | None = None


@dataclass
class TransformParameters(PropertyType):
    transform_type: DslValue[str] | None = None
    find_matches_parameters: DslValue[FindMatchesParameters] | None = None
