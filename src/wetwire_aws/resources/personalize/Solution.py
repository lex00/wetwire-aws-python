"""PropertyTypes for AWS::Personalize::Solution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AlgorithmHyperParameterRanges(PropertyType):
    categorical_hyper_parameter_ranges: list[
        DslValue[CategoricalHyperParameterRange]
    ] = field(default_factory=list)
    continuous_hyper_parameter_ranges: list[DslValue[ContinuousHyperParameterRange]] = (
        field(default_factory=list)
    )
    integer_hyper_parameter_ranges: list[DslValue[IntegerHyperParameterRange]] = field(
        default_factory=list
    )


@dataclass
class AutoMLConfig(PropertyType):
    metric_name: DslValue[str] | None = None
    recipe_list: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CategoricalHyperParameterRange(PropertyType):
    name: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ContinuousHyperParameterRange(PropertyType):
    max_value: DslValue[float] | None = None
    min_value: DslValue[float] | None = None
    name: DslValue[str] | None = None


@dataclass
class HpoConfig(PropertyType):
    algorithm_hyper_parameter_ranges: DslValue[AlgorithmHyperParameterRanges] | None = (
        None
    )
    hpo_objective: DslValue[HpoObjective] | None = None
    hpo_resource_config: DslValue[HpoResourceConfig] | None = None


@dataclass
class HpoObjective(PropertyType):
    metric_name: DslValue[str] | None = None
    metric_regex: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class HpoResourceConfig(PropertyType):
    max_number_of_training_jobs: DslValue[str] | None = None
    max_parallel_training_jobs: DslValue[str] | None = None


@dataclass
class IntegerHyperParameterRange(PropertyType):
    max_value: DslValue[int] | None = None
    min_value: DslValue[int] | None = None
    name: DslValue[str] | None = None


@dataclass
class SolutionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_ml_config": "AutoMLConfig",
    }

    algorithm_hyper_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    auto_ml_config: DslValue[AutoMLConfig] | None = None
    event_value_threshold: DslValue[str] | None = None
    feature_transformation_parameters: dict[str, DslValue[str]] = field(
        default_factory=dict
    )
    hpo_config: DslValue[HpoConfig] | None = None
