"""PropertyTypes for AWS::SageMaker::ModelCard."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdditionalInformation(PropertyType):
    caveats_and_recommendations: DslValue[str] | None = None
    custom_details: dict[str, DslValue[str]] = field(default_factory=dict)
    ethical_considerations: DslValue[str] | None = None


@dataclass
class BusinessDetails(PropertyType):
    business_problem: DslValue[str] | None = None
    business_stakeholders: DslValue[str] | None = None
    line_of_business: DslValue[str] | None = None


@dataclass
class Container(PropertyType):
    image: DslValue[str] | None = None
    model_data_url: DslValue[str] | None = None
    nearest_model_name: DslValue[str] | None = None


@dataclass
class Content(PropertyType):
    additional_information: DslValue[AdditionalInformation] | None = None
    business_details: DslValue[BusinessDetails] | None = None
    evaluation_details: list[DslValue[EvaluationDetail]] = field(default_factory=list)
    intended_uses: DslValue[IntendedUses] | None = None
    model_overview: DslValue[ModelOverview] | None = None
    model_package_details: DslValue[ModelPackageDetails] | None = None
    training_details: DslValue[TrainingDetails] | None = None


@dataclass
class EvaluationDetail(PropertyType):
    name: DslValue[str] | None = None
    datasets: list[DslValue[str]] = field(default_factory=list)
    evaluation_job_arn: DslValue[str] | None = None
    evaluation_observation: DslValue[str] | None = None
    metadata: dict[str, DslValue[str]] = field(default_factory=dict)
    metric_groups: list[DslValue[MetricGroup]] = field(default_factory=list)


@dataclass
class Function(PropertyType):
    condition: DslValue[str] | None = None
    facet: DslValue[str] | None = None
    function: DslValue[str] | None = None


@dataclass
class InferenceEnvironment(PropertyType):
    container_image: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InferenceSpecification(PropertyType):
    containers: list[DslValue[Container]] = field(default_factory=list)


@dataclass
class IntendedUses(PropertyType):
    explanations_for_risk_rating: DslValue[str] | None = None
    factors_affecting_model_efficiency: DslValue[str] | None = None
    intended_uses: DslValue[str] | None = None
    purpose_of_model: DslValue[str] | None = None
    risk_rating: DslValue[str] | None = None


@dataclass
class MetricDataItems(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    value: DslValue[dict[str, Any]] | None = None
    notes: DslValue[str] | None = None
    x_axis_name: list[DslValue[str]] = field(default_factory=list)
    y_axis_name: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MetricGroup(PropertyType):
    metric_data: list[DslValue[MetricDataItems]] = field(default_factory=list)
    name: DslValue[str] | None = None


@dataclass
class ModelOverview(PropertyType):
    algorithm_type: DslValue[str] | None = None
    inference_environment: DslValue[InferenceEnvironment] | None = None
    model_artifact: list[DslValue[str]] = field(default_factory=list)
    model_creator: DslValue[str] | None = None
    model_description: DslValue[str] | None = None
    model_id: DslValue[str] | None = None
    model_name: DslValue[str] | None = None
    model_owner: DslValue[str] | None = None
    model_version: DslValue[float] | None = None
    problem_type: DslValue[str] | None = None


@dataclass
class ModelPackageCreator(PropertyType):
    user_profile_name: DslValue[str] | None = None


@dataclass
class ModelPackageDetails(PropertyType):
    approval_description: DslValue[str] | None = None
    created_by: DslValue[ModelPackageCreator] | None = None
    domain: DslValue[str] | None = None
    inference_specification: DslValue[InferenceSpecification] | None = None
    model_approval_status: DslValue[str] | None = None
    model_package_arn: DslValue[str] | None = None
    model_package_description: DslValue[str] | None = None
    model_package_group_name: DslValue[str] | None = None
    model_package_name: DslValue[str] | None = None
    model_package_status: DslValue[str] | None = None
    model_package_version: DslValue[float] | None = None
    source_algorithms: list[DslValue[SourceAlgorithm]] = field(default_factory=list)
    task: DslValue[str] | None = None


@dataclass
class ObjectiveFunction(PropertyType):
    function: DslValue[Function] | None = None
    notes: DslValue[str] | None = None


@dataclass
class SecurityConfig(PropertyType):
    kms_key_id: DslValue[str] | None = None


@dataclass
class SourceAlgorithm(PropertyType):
    algorithm_name: DslValue[str] | None = None
    model_data_url: DslValue[str] | None = None


@dataclass
class TrainingDetails(PropertyType):
    objective_function: DslValue[ObjectiveFunction] | None = None
    training_job_details: DslValue[TrainingJobDetails] | None = None
    training_observations: DslValue[str] | None = None


@dataclass
class TrainingEnvironment(PropertyType):
    container_image: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TrainingHyperParameter(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TrainingJobDetails(PropertyType):
    hyper_parameters: list[DslValue[TrainingHyperParameter]] = field(
        default_factory=list
    )
    training_arn: DslValue[str] | None = None
    training_datasets: list[DslValue[str]] = field(default_factory=list)
    training_environment: DslValue[TrainingEnvironment] | None = None
    training_metrics: list[DslValue[TrainingMetric]] = field(default_factory=list)
    user_provided_hyper_parameters: list[DslValue[TrainingHyperParameter]] = field(
        default_factory=list
    )
    user_provided_training_metrics: list[DslValue[TrainingMetric]] = field(
        default_factory=list
    )


@dataclass
class TrainingMetric(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[float] | None = None
    notes: DslValue[str] | None = None


@dataclass
class UserContext(PropertyType):
    domain_id: DslValue[str] | None = None
    user_profile_arn: DslValue[str] | None = None
    user_profile_name: DslValue[str] | None = None
