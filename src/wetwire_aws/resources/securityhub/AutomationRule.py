"""PropertyTypes for AWS::SecurityHub::AutomationRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutomationRulesAction(PropertyType):
    finding_fields_update: DslValue[AutomationRulesFindingFieldsUpdate] | None = None
    type_: DslValue[str] | None = None


@dataclass
class AutomationRulesFindingFieldsUpdate(PropertyType):
    confidence: DslValue[int] | None = None
    criticality: DslValue[int] | None = None
    note: DslValue[NoteUpdate] | None = None
    related_findings: list[DslValue[RelatedFinding]] = field(default_factory=list)
    severity: DslValue[SeverityUpdate] | None = None
    types: list[DslValue[str]] = field(default_factory=list)
    user_defined_fields: dict[str, DslValue[str]] = field(default_factory=dict)
    verification_state: DslValue[str] | None = None
    workflow: DslValue[WorkflowUpdate] | None = None


@dataclass
class AutomationRulesFindingFilters(PropertyType):
    aws_account_id: list[DslValue[StringFilter]] = field(default_factory=list)
    company_name: list[DslValue[StringFilter]] = field(default_factory=list)
    compliance_associated_standards_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    compliance_security_control_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    compliance_status: list[DslValue[StringFilter]] = field(default_factory=list)
    confidence: list[DslValue[NumberFilter]] = field(default_factory=list)
    created_at: list[DslValue[DateFilter]] = field(default_factory=list)
    criticality: list[DslValue[NumberFilter]] = field(default_factory=list)
    description: list[DslValue[StringFilter]] = field(default_factory=list)
    first_observed_at: list[DslValue[DateFilter]] = field(default_factory=list)
    generator_id: list[DslValue[StringFilter]] = field(default_factory=list)
    id: list[DslValue[StringFilter]] = field(default_factory=list)
    last_observed_at: list[DslValue[DateFilter]] = field(default_factory=list)
    note_text: list[DslValue[StringFilter]] = field(default_factory=list)
    note_updated_at: list[DslValue[DateFilter]] = field(default_factory=list)
    note_updated_by: list[DslValue[StringFilter]] = field(default_factory=list)
    product_arn: list[DslValue[StringFilter]] = field(default_factory=list)
    product_name: list[DslValue[StringFilter]] = field(default_factory=list)
    record_state: list[DslValue[StringFilter]] = field(default_factory=list)
    related_findings_id: list[DslValue[StringFilter]] = field(default_factory=list)
    related_findings_product_arn: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_details_other: list[DslValue[MapFilter]] = field(default_factory=list)
    resource_id: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_partition: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_region: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_tags: list[DslValue[MapFilter]] = field(default_factory=list)
    resource_type: list[DslValue[StringFilter]] = field(default_factory=list)
    severity_label: list[DslValue[StringFilter]] = field(default_factory=list)
    source_url: list[DslValue[StringFilter]] = field(default_factory=list)
    title: list[DslValue[StringFilter]] = field(default_factory=list)
    type_: list[DslValue[StringFilter]] = field(default_factory=list)
    updated_at: list[DslValue[DateFilter]] = field(default_factory=list)
    user_defined_fields: list[DslValue[MapFilter]] = field(default_factory=list)
    verification_state: list[DslValue[StringFilter]] = field(default_factory=list)
    workflow_status: list[DslValue[StringFilter]] = field(default_factory=list)


@dataclass
class DateFilter(PropertyType):
    date_range: DslValue[DateRange] | None = None
    end: DslValue[str] | None = None
    start: DslValue[str] | None = None


@dataclass
class DateRange(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class MapFilter(PropertyType):
    comparison: DslValue[str] | None = None
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class NoteUpdate(PropertyType):
    text: DslValue[str] | None = None
    updated_by: DslValue[dict[str, Any]] | None = None


@dataclass
class NumberFilter(PropertyType):
    eq: DslValue[float] | None = None
    gte: DslValue[float] | None = None
    lte: DslValue[float] | None = None


@dataclass
class RelatedFinding(PropertyType):
    id: DslValue[dict[str, Any]] | None = None
    product_arn: DslValue[str] | None = None


@dataclass
class SeverityUpdate(PropertyType):
    label: DslValue[str] | None = None
    normalized: DslValue[int] | None = None
    product: DslValue[float] | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class WorkflowUpdate(PropertyType):
    status: DslValue[str] | None = None
