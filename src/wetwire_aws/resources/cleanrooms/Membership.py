"""PropertyTypes for AWS::CleanRooms::Membership."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MembershipJobComputePaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class MembershipMLPaymentConfig(PropertyType):
    model_inference: DslValue[MembershipModelInferencePaymentConfig] | None = None
    model_training: DslValue[MembershipModelTrainingPaymentConfig] | None = None
    synthetic_data_generation: (
        DslValue[MembershipSyntheticDataGenerationPaymentConfig] | None
    ) = None


@dataclass
class MembershipModelInferencePaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class MembershipModelTrainingPaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class MembershipPaymentConfiguration(PropertyType):
    query_compute: DslValue[MembershipQueryComputePaymentConfig] | None = None
    job_compute: DslValue[MembershipJobComputePaymentConfig] | None = None
    machine_learning: DslValue[MembershipMLPaymentConfig] | None = None


@dataclass
class MembershipProtectedJobOutputConfiguration(PropertyType):
    s3: DslValue[ProtectedJobS3OutputConfigurationInput] | None = None


@dataclass
class MembershipProtectedJobResultConfiguration(PropertyType):
    output_configuration: DslValue[MembershipProtectedJobOutputConfiguration] | None = (
        None
    )
    role_arn: DslValue[str] | None = None


@dataclass
class MembershipProtectedQueryOutputConfiguration(PropertyType):
    s3: DslValue[ProtectedQueryS3OutputConfiguration] | None = None


@dataclass
class MembershipProtectedQueryResultConfiguration(PropertyType):
    output_configuration: (
        DslValue[MembershipProtectedQueryOutputConfiguration] | None
    ) = None
    role_arn: DslValue[str] | None = None


@dataclass
class MembershipQueryComputePaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class MembershipSyntheticDataGenerationPaymentConfig(PropertyType):
    is_responsible: DslValue[bool] | None = None


@dataclass
class ProtectedJobS3OutputConfigurationInput(PropertyType):
    bucket: DslValue[str] | None = None
    key_prefix: DslValue[str] | None = None


@dataclass
class ProtectedQueryS3OutputConfiguration(PropertyType):
    bucket: DslValue[str] | None = None
    result_format: DslValue[str] | None = None
    key_prefix: DslValue[str] | None = None
    single_file_output: DslValue[bool] | None = None
