"""PropertyTypes for AWS::CleanRooms::Membership."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MembershipJobComputePaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class MembershipMLPaymentConfig(PropertyType):
    model_inference: MembershipModelInferencePaymentConfig | None = None
    model_training: MembershipModelTrainingPaymentConfig | None = None
    synthetic_data_generation: MembershipSyntheticDataGenerationPaymentConfig | None = (
        None
    )


@dataclass
class MembershipModelInferencePaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class MembershipModelTrainingPaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class MembershipPaymentConfiguration(PropertyType):
    query_compute: MembershipQueryComputePaymentConfig | None = None
    job_compute: MembershipJobComputePaymentConfig | None = None
    machine_learning: MembershipMLPaymentConfig | None = None


@dataclass
class MembershipProtectedJobOutputConfiguration(PropertyType):
    s3: ProtectedJobS3OutputConfigurationInput | None = None


@dataclass
class MembershipProtectedJobResultConfiguration(PropertyType):
    output_configuration: MembershipProtectedJobOutputConfiguration | None = None
    role_arn: str | None = None


@dataclass
class MembershipProtectedQueryOutputConfiguration(PropertyType):
    s3: ProtectedQueryS3OutputConfiguration | None = None


@dataclass
class MembershipProtectedQueryResultConfiguration(PropertyType):
    output_configuration: MembershipProtectedQueryOutputConfiguration | None = None
    role_arn: str | None = None


@dataclass
class MembershipQueryComputePaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class MembershipSyntheticDataGenerationPaymentConfig(PropertyType):
    is_responsible: bool | None = None


@dataclass
class ProtectedJobS3OutputConfigurationInput(PropertyType):
    bucket: str | None = None
    key_prefix: str | None = None


@dataclass
class ProtectedQueryS3OutputConfiguration(PropertyType):
    bucket: str | None = None
    result_format: str | None = None
    key_prefix: str | None = None
    single_file_output: bool | None = None
