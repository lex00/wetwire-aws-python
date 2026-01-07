"""PropertyTypes for AWS::Connect::EvaluationForm."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoEvaluationConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class AutomaticFailConfiguration(PropertyType):
    target_section: DslValue[str] | None = None


@dataclass
class EvaluationFormBaseItem(PropertyType):
    section: DslValue[EvaluationFormSection] | None = None


@dataclass
class EvaluationFormItem(PropertyType):
    question: DslValue[EvaluationFormQuestion] | None = None
    section: DslValue[EvaluationFormSection] | None = None


@dataclass
class EvaluationFormItemEnablementCondition(PropertyType):
    operands: list[DslValue[EvaluationFormItemEnablementConditionOperand]] = field(
        default_factory=list
    )
    operator: DslValue[str] | None = None


@dataclass
class EvaluationFormItemEnablementConditionOperand(PropertyType):
    expression: DslValue[EvaluationFormItemEnablementExpression] | None = None


@dataclass
class EvaluationFormItemEnablementConfiguration(PropertyType):
    action: DslValue[str] | None = None
    condition: DslValue[EvaluationFormItemEnablementCondition] | None = None
    default_action: DslValue[str] | None = None


@dataclass
class EvaluationFormItemEnablementExpression(PropertyType):
    comparator: DslValue[str] | None = None
    source: DslValue[EvaluationFormItemEnablementSource] | None = None
    values: list[DslValue[EvaluationFormItemEnablementSourceValue]] = field(
        default_factory=list
    )


@dataclass
class EvaluationFormItemEnablementSource(PropertyType):
    type_: DslValue[str] | None = None
    ref_id: DslValue[str] | None = None


@dataclass
class EvaluationFormItemEnablementSourceValue(PropertyType):
    ref_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class EvaluationFormLanguageConfiguration(PropertyType):
    form_language: DslValue[str] | None = None


@dataclass
class EvaluationFormMultiSelectQuestionAutomation(PropertyType):
    options: list[DslValue[EvaluationFormMultiSelectQuestionAutomationOption]] = field(
        default_factory=list
    )
    answer_source: DslValue[EvaluationFormQuestionAutomationAnswerSource] | None = None
    default_option_ref_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class EvaluationFormMultiSelectQuestionAutomationOption(PropertyType):
    rule_category: DslValue[MultiSelectQuestionRuleCategoryAutomation] | None = None


@dataclass
class EvaluationFormMultiSelectQuestionOption(PropertyType):
    ref_id: DslValue[str] | None = None
    text: DslValue[str] | None = None


@dataclass
class EvaluationFormMultiSelectQuestionProperties(PropertyType):
    options: list[DslValue[EvaluationFormMultiSelectQuestionOption]] = field(
        default_factory=list
    )
    automation: DslValue[EvaluationFormMultiSelectQuestionAutomation] | None = None
    display_as: DslValue[str] | None = None


@dataclass
class EvaluationFormNumericQuestionAutomation(PropertyType):
    answer_source: DslValue[EvaluationFormQuestionAutomationAnswerSource] | None = None
    property_value: DslValue[NumericQuestionPropertyValueAutomation] | None = None


@dataclass
class EvaluationFormNumericQuestionOption(PropertyType):
    max_value: DslValue[int] | None = None
    min_value: DslValue[int] | None = None
    automatic_fail: DslValue[bool] | None = None
    automatic_fail_configuration: DslValue[AutomaticFailConfiguration] | None = None
    score: DslValue[int] | None = None


@dataclass
class EvaluationFormNumericQuestionProperties(PropertyType):
    max_value: DslValue[int] | None = None
    min_value: DslValue[int] | None = None
    automation: DslValue[EvaluationFormNumericQuestionAutomation] | None = None
    options: list[DslValue[EvaluationFormNumericQuestionOption]] = field(
        default_factory=list
    )


@dataclass
class EvaluationFormQuestion(PropertyType):
    question_type: DslValue[str] | None = None
    ref_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    enablement: DslValue[EvaluationFormItemEnablementConfiguration] | None = None
    instructions: DslValue[str] | None = None
    not_applicable_enabled: DslValue[bool] | None = None
    question_type_properties: DslValue[EvaluationFormQuestionTypeProperties] | None = (
        None
    )
    weight: DslValue[float] | None = None


@dataclass
class EvaluationFormQuestionAutomationAnswerSource(PropertyType):
    source_type: DslValue[str] | None = None


@dataclass
class EvaluationFormQuestionTypeProperties(PropertyType):
    multi_select: DslValue[EvaluationFormMultiSelectQuestionProperties] | None = None
    numeric: DslValue[EvaluationFormNumericQuestionProperties] | None = None
    single_select: DslValue[EvaluationFormSingleSelectQuestionProperties] | None = None
    text: DslValue[EvaluationFormTextQuestionProperties] | None = None


@dataclass
class EvaluationFormSection(PropertyType):
    ref_id: DslValue[str] | None = None
    title: DslValue[str] | None = None
    instructions: DslValue[str] | None = None
    items: list[DslValue[EvaluationFormItem]] = field(default_factory=list)
    weight: DslValue[float] | None = None


@dataclass
class EvaluationFormSingleSelectQuestionAutomation(PropertyType):
    options: list[DslValue[EvaluationFormSingleSelectQuestionAutomationOption]] = field(
        default_factory=list
    )
    answer_source: DslValue[EvaluationFormQuestionAutomationAnswerSource] | None = None
    default_option_ref_id: DslValue[str] | None = None


@dataclass
class EvaluationFormSingleSelectQuestionAutomationOption(PropertyType):
    rule_category: DslValue[SingleSelectQuestionRuleCategoryAutomation] | None = None


@dataclass
class EvaluationFormSingleSelectQuestionOption(PropertyType):
    ref_id: DslValue[str] | None = None
    text: DslValue[str] | None = None
    automatic_fail: DslValue[bool] | None = None
    automatic_fail_configuration: DslValue[AutomaticFailConfiguration] | None = None
    score: DslValue[int] | None = None


@dataclass
class EvaluationFormSingleSelectQuestionProperties(PropertyType):
    options: list[DslValue[EvaluationFormSingleSelectQuestionOption]] = field(
        default_factory=list
    )
    automation: DslValue[EvaluationFormSingleSelectQuestionAutomation] | None = None
    display_as: DslValue[str] | None = None


@dataclass
class EvaluationFormTargetConfiguration(PropertyType):
    contact_interaction_type: DslValue[str] | None = None


@dataclass
class EvaluationFormTextQuestionAutomation(PropertyType):
    answer_source: DslValue[EvaluationFormQuestionAutomationAnswerSource] | None = None


@dataclass
class EvaluationFormTextQuestionProperties(PropertyType):
    automation: DslValue[EvaluationFormTextQuestionAutomation] | None = None


@dataclass
class MultiSelectQuestionRuleCategoryAutomation(PropertyType):
    category: DslValue[str] | None = None
    condition: DslValue[str] | None = None
    option_ref_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class NumericQuestionPropertyValueAutomation(PropertyType):
    label: DslValue[str] | None = None


@dataclass
class ScoringStrategy(PropertyType):
    mode: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class SingleSelectQuestionRuleCategoryAutomation(PropertyType):
    category: DslValue[str] | None = None
    condition: DslValue[str] | None = None
    option_ref_id: DslValue[str] | None = None
