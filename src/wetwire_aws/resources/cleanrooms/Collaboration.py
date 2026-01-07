"""PropertyTypes for AWS::CleanRooms::Collaboration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataEncryptionMetadata(PropertyType):
    allow_cleartext: DslValue[bool] | None = None
    allow_duplicates: DslValue[bool] | None = None
    allow_joins_on_columns_with_different_names: DslValue[bool] | None = None
    preserve_nulls: DslValue[bool] | None = None


@dataclass
class JobComputePaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class MLMemberAbilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_ml_member_abilities": "CustomMLMemberAbilities",
    }

    custom_ml_member_abilities: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MLPaymentConfig(PropertyType):
    model_inference: DslValue[ModelInferencePaymentConfig] | None = None
    model_training: DslValue[ModelTrainingPaymentConfig] | None = None
    synthetic_data_generation: DslValue[SyntheticDataGenerationPaymentConfig] | None = (
        None
    )


@dataclass
class MemberSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_member_abilities": "MLMemberAbilities",
    }

    account_id: DslValue[str] | None = None
    display_name: DslValue[str] | None = None
    member_abilities: list[DslValue[str]] = field(default_factory=list)
    ml_member_abilities: DslValue[MLMemberAbilities] | None = None
    payment_configuration: DslValue[PaymentConfiguration] | None = None


@dataclass
class ModelInferencePaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class ModelTrainingPaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class PaymentConfiguration(PropertyType):
    query_compute: DslValue[QueryComputePaymentConfig] | None = None
    job_compute: DslValue[JobComputePaymentConfig] | None = None
    machine_learning: DslValue[MLPaymentConfig] | None = None


@dataclass
class QueryComputePaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class SyntheticDataGenerationPaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None
