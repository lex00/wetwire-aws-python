"""PropertyTypes for AWS::Connect::EvaluationForm."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoEvaluationConfiguration(PropertyType):
    enabled: bool | None = None


@dataclass
class AutomaticFailConfiguration(PropertyType):
    target_section: str | None = None


@dataclass
class EvaluationFormBaseItem(PropertyType):
    section: EvaluationFormSection | None = None


@dataclass
class EvaluationFormItem(PropertyType):
    question: EvaluationFormQuestion | None = None
    section: EvaluationFormSection | None = None


@dataclass
class EvaluationFormItemEnablementCondition(PropertyType):
    operands: list[EvaluationFormItemEnablementConditionOperand] = field(
        default_factory=list
    )
    operator: str | None = None


@dataclass
class EvaluationFormItemEnablementConditionOperand(PropertyType):
    expression: EvaluationFormItemEnablementExpression | None = None


@dataclass
class EvaluationFormItemEnablementConfiguration(PropertyType):
    action: str | None = None
    condition: EvaluationFormItemEnablementCondition | None = None
    default_action: str | None = None


@dataclass
class EvaluationFormItemEnablementExpression(PropertyType):
    comparator: str | None = None
    source: EvaluationFormItemEnablementSource | None = None
    values: list[EvaluationFormItemEnablementSourceValue] = field(default_factory=list)


@dataclass
class EvaluationFormItemEnablementSource(PropertyType):
    type_: str | None = None
    ref_id: str | None = None


@dataclass
class EvaluationFormItemEnablementSourceValue(PropertyType):
    ref_id: str | None = None
    type_: str | None = None


@dataclass
class EvaluationFormLanguageConfiguration(PropertyType):
    form_language: str | None = None


@dataclass
class EvaluationFormMultiSelectQuestionAutomation(PropertyType):
    options: list[EvaluationFormMultiSelectQuestionAutomationOption] = field(
        default_factory=list
    )
    answer_source: EvaluationFormQuestionAutomationAnswerSource | None = None
    default_option_ref_ids: list[String] = field(default_factory=list)


@dataclass
class EvaluationFormMultiSelectQuestionAutomationOption(PropertyType):
    rule_category: MultiSelectQuestionRuleCategoryAutomation | None = None


@dataclass
class EvaluationFormMultiSelectQuestionOption(PropertyType):
    ref_id: str | None = None
    text: str | None = None


@dataclass
class EvaluationFormMultiSelectQuestionProperties(PropertyType):
    options: list[EvaluationFormMultiSelectQuestionOption] = field(default_factory=list)
    automation: EvaluationFormMultiSelectQuestionAutomation | None = None
    display_as: str | None = None


@dataclass
class EvaluationFormNumericQuestionAutomation(PropertyType):
    answer_source: EvaluationFormQuestionAutomationAnswerSource | None = None
    property_value: NumericQuestionPropertyValueAutomation | None = None


@dataclass
class EvaluationFormNumericQuestionOption(PropertyType):
    max_value: int | None = None
    min_value: int | None = None
    automatic_fail: bool | None = None
    automatic_fail_configuration: AutomaticFailConfiguration | None = None
    score: int | None = None


@dataclass
class EvaluationFormNumericQuestionProperties(PropertyType):
    max_value: int | None = None
    min_value: int | None = None
    automation: EvaluationFormNumericQuestionAutomation | None = None
    options: list[EvaluationFormNumericQuestionOption] = field(default_factory=list)


@dataclass
class EvaluationFormQuestion(PropertyType):
    question_type: str | None = None
    ref_id: str | None = None
    title: str | None = None
    enablement: EvaluationFormItemEnablementConfiguration | None = None
    instructions: str | None = None
    not_applicable_enabled: bool | None = None
    question_type_properties: EvaluationFormQuestionTypeProperties | None = None
    weight: float | None = None


@dataclass
class EvaluationFormQuestionAutomationAnswerSource(PropertyType):
    source_type: str | None = None


@dataclass
class EvaluationFormQuestionTypeProperties(PropertyType):
    multi_select: EvaluationFormMultiSelectQuestionProperties | None = None
    numeric: EvaluationFormNumericQuestionProperties | None = None
    single_select: EvaluationFormSingleSelectQuestionProperties | None = None
    text: EvaluationFormTextQuestionProperties | None = None


@dataclass
class EvaluationFormSection(PropertyType):
    ref_id: str | None = None
    title: str | None = None
    instructions: str | None = None
    items: list[EvaluationFormItem] = field(default_factory=list)
    weight: float | None = None


@dataclass
class EvaluationFormSingleSelectQuestionAutomation(PropertyType):
    options: list[EvaluationFormSingleSelectQuestionAutomationOption] = field(
        default_factory=list
    )
    answer_source: EvaluationFormQuestionAutomationAnswerSource | None = None
    default_option_ref_id: str | None = None


@dataclass
class EvaluationFormSingleSelectQuestionAutomationOption(PropertyType):
    rule_category: SingleSelectQuestionRuleCategoryAutomation | None = None


@dataclass
class EvaluationFormSingleSelectQuestionOption(PropertyType):
    ref_id: str | None = None
    text: str | None = None
    automatic_fail: bool | None = None
    automatic_fail_configuration: AutomaticFailConfiguration | None = None
    score: int | None = None


@dataclass
class EvaluationFormSingleSelectQuestionProperties(PropertyType):
    options: list[EvaluationFormSingleSelectQuestionOption] = field(
        default_factory=list
    )
    automation: EvaluationFormSingleSelectQuestionAutomation | None = None
    display_as: str | None = None


@dataclass
class EvaluationFormTargetConfiguration(PropertyType):
    contact_interaction_type: str | None = None


@dataclass
class EvaluationFormTextQuestionAutomation(PropertyType):
    answer_source: EvaluationFormQuestionAutomationAnswerSource | None = None


@dataclass
class EvaluationFormTextQuestionProperties(PropertyType):
    automation: EvaluationFormTextQuestionAutomation | None = None


@dataclass
class MultiSelectQuestionRuleCategoryAutomation(PropertyType):
    category: str | None = None
    condition: str | None = None
    option_ref_ids: list[String] = field(default_factory=list)


@dataclass
class NumericQuestionPropertyValueAutomation(PropertyType):
    label: str | None = None


@dataclass
class ScoringStrategy(PropertyType):
    mode: str | None = None
    status: str | None = None


@dataclass
class SingleSelectQuestionRuleCategoryAutomation(PropertyType):
    category: str | None = None
    condition: str | None = None
    option_ref_id: str | None = None
