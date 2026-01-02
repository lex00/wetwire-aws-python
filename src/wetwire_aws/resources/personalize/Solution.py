"""PropertyTypes for AWS::Personalize::Solution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AlgorithmHyperParameterRanges(PropertyType):
    categorical_hyper_parameter_ranges: list[CategoricalHyperParameterRange] = field(
        default_factory=list
    )
    continuous_hyper_parameter_ranges: list[ContinuousHyperParameterRange] = field(
        default_factory=list
    )
    integer_hyper_parameter_ranges: list[IntegerHyperParameterRange] = field(
        default_factory=list
    )


@dataclass
class AutoMLConfig(PropertyType):
    metric_name: str | None = None
    recipe_list: list[String] = field(default_factory=list)


@dataclass
class CategoricalHyperParameterRange(PropertyType):
    name: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class ContinuousHyperParameterRange(PropertyType):
    max_value: float | None = None
    min_value: float | None = None
    name: str | None = None


@dataclass
class HpoConfig(PropertyType):
    algorithm_hyper_parameter_ranges: AlgorithmHyperParameterRanges | None = None
    hpo_objective: HpoObjective | None = None
    hpo_resource_config: HpoResourceConfig | None = None


@dataclass
class HpoObjective(PropertyType):
    metric_name: str | None = None
    metric_regex: str | None = None
    type_: str | None = None


@dataclass
class HpoResourceConfig(PropertyType):
    max_number_of_training_jobs: str | None = None
    max_parallel_training_jobs: str | None = None


@dataclass
class IntegerHyperParameterRange(PropertyType):
    max_value: int | None = None
    min_value: int | None = None
    name: str | None = None


@dataclass
class SolutionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_ml_config": "AutoMLConfig",
    }

    algorithm_hyper_parameters: dict[str, String] = field(default_factory=dict)
    auto_ml_config: AutoMLConfig | None = None
    event_value_threshold: str | None = None
    feature_transformation_parameters: dict[str, String] = field(default_factory=dict)
    hpo_config: HpoConfig | None = None
