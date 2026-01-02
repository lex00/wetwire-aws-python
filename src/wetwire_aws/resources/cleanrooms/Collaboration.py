"""PropertyTypes for AWS::CleanRooms::Collaboration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataEncryptionMetadata(PropertyType):
    allow_cleartext: bool | None = None
    allow_duplicates: bool | None = None
    allow_joins_on_columns_with_different_names: bool | None = None
    preserve_nulls: bool | None = None


@dataclass
class JobComputePaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class MLMemberAbilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_ml_member_abilities": "CustomMLMemberAbilities",
    }

    custom_ml_member_abilities: list[String] = field(default_factory=list)


@dataclass
class MLPaymentConfig(PropertyType):
    model_inference: ModelInferencePaymentConfig | None = None
    model_training: ModelTrainingPaymentConfig | None = None
    synthetic_data_generation: SyntheticDataGenerationPaymentConfig | None = None


@dataclass
class MemberSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ml_member_abilities": "MLMemberAbilities",
    }

    account_id: str | None = None
    display_name: str | None = None
    member_abilities: list[String] = field(default_factory=list)
    ml_member_abilities: MLMemberAbilities | None = None
    payment_configuration: PaymentConfiguration | None = None


@dataclass
class ModelInferencePaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class ModelTrainingPaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class PaymentConfiguration(PropertyType):
    query_compute: QueryComputePaymentConfig | None = None
    job_compute: JobComputePaymentConfig | None = None
    machine_learning: MLPaymentConfig | None = None


@dataclass
class QueryComputePaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class SyntheticDataGenerationPaymentConfig(PropertyType):
    is_responsible: bool | None = None
