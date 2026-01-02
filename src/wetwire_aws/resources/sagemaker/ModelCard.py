"""PropertyTypes for AWS::SageMaker::ModelCard."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdditionalInformation(PropertyType):
    caveats_and_recommendations: str | None = None
    custom_details: dict[str, String] = field(default_factory=dict)
    ethical_considerations: str | None = None


@dataclass
class BusinessDetails(PropertyType):
    business_problem: str | None = None
    business_stakeholders: str | None = None
    line_of_business: str | None = None


@dataclass
class Container(PropertyType):
    image: str | None = None
    model_data_url: str | None = None
    nearest_model_name: str | None = None


@dataclass
class Content(PropertyType):
    additional_information: AdditionalInformation | None = None
    business_details: BusinessDetails | None = None
    evaluation_details: list[EvaluationDetail] = field(default_factory=list)
    intended_uses: IntendedUses | None = None
    model_overview: ModelOverview | None = None
    model_package_details: ModelPackageDetails | None = None
    training_details: TrainingDetails | None = None


@dataclass
class EvaluationDetail(PropertyType):
    name: str | None = None
    datasets: list[String] = field(default_factory=list)
    evaluation_job_arn: str | None = None
    evaluation_observation: str | None = None
    metadata: dict[str, String] = field(default_factory=dict)
    metric_groups: list[MetricGroup] = field(default_factory=list)


@dataclass
class Function(PropertyType):
    condition: str | None = None
    facet: str | None = None
    function: str | None = None


@dataclass
class InferenceEnvironment(PropertyType):
    container_image: list[String] = field(default_factory=list)


@dataclass
class InferenceSpecification(PropertyType):
    containers: list[Container] = field(default_factory=list)


@dataclass
class IntendedUses(PropertyType):
    explanations_for_risk_rating: str | None = None
    factors_affecting_model_efficiency: str | None = None
    intended_uses: str | None = None
    purpose_of_model: str | None = None
    risk_rating: str | None = None


@dataclass
class MetricDataItems(PropertyType):
    name: str | None = None
    type_: str | None = None
    value: dict[str, Any] | None = None
    notes: str | None = None
    x_axis_name: list[String] = field(default_factory=list)
    y_axis_name: list[String] = field(default_factory=list)


@dataclass
class MetricGroup(PropertyType):
    metric_data: list[MetricDataItems] = field(default_factory=list)
    name: str | None = None


@dataclass
class ModelOverview(PropertyType):
    algorithm_type: str | None = None
    inference_environment: InferenceEnvironment | None = None
    model_artifact: list[String] = field(default_factory=list)
    model_creator: str | None = None
    model_description: str | None = None
    model_id: str | None = None
    model_name: str | None = None
    model_owner: str | None = None
    model_version: float | None = None
    problem_type: str | None = None


@dataclass
class ModelPackageCreator(PropertyType):
    user_profile_name: str | None = None


@dataclass
class ModelPackageDetails(PropertyType):
    approval_description: str | None = None
    created_by: ModelPackageCreator | None = None
    domain: str | None = None
    inference_specification: InferenceSpecification | None = None
    model_approval_status: str | None = None
    model_package_arn: str | None = None
    model_package_description: str | None = None
    model_package_group_name: str | None = None
    model_package_name: str | None = None
    model_package_status: str | None = None
    model_package_version: float | None = None
    source_algorithms: list[SourceAlgorithm] = field(default_factory=list)
    task: str | None = None


@dataclass
class ObjectiveFunction(PropertyType):
    function: Function | None = None
    notes: str | None = None


@dataclass
class SecurityConfig(PropertyType):
    kms_key_id: str | None = None


@dataclass
class SourceAlgorithm(PropertyType):
    algorithm_name: str | None = None
    model_data_url: str | None = None


@dataclass
class TrainingDetails(PropertyType):
    objective_function: ObjectiveFunction | None = None
    training_job_details: TrainingJobDetails | None = None
    training_observations: str | None = None


@dataclass
class TrainingEnvironment(PropertyType):
    container_image: list[String] = field(default_factory=list)


@dataclass
class TrainingHyperParameter(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class TrainingJobDetails(PropertyType):
    hyper_parameters: list[TrainingHyperParameter] = field(default_factory=list)
    training_arn: str | None = None
    training_datasets: list[String] = field(default_factory=list)
    training_environment: TrainingEnvironment | None = None
    training_metrics: list[TrainingMetric] = field(default_factory=list)
    user_provided_hyper_parameters: list[TrainingHyperParameter] = field(
        default_factory=list
    )
    user_provided_training_metrics: list[TrainingMetric] = field(default_factory=list)


@dataclass
class TrainingMetric(PropertyType):
    name: str | None = None
    value: float | None = None
    notes: str | None = None


@dataclass
class UserContext(PropertyType):
    domain_id: str | None = None
    user_profile_arn: str | None = None
    user_profile_name: str | None = None
