"""PropertyTypes for AWS::SecurityHub::AutomationRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutomationRulesAction(PropertyType):
    finding_fields_update: AutomationRulesFindingFieldsUpdate | None = None
    type_: str | None = None


@dataclass
class AutomationRulesFindingFieldsUpdate(PropertyType):
    confidence: int | None = None
    criticality: int | None = None
    note: NoteUpdate | None = None
    related_findings: list[RelatedFinding] = field(default_factory=list)
    severity: SeverityUpdate | None = None
    types: list[String] = field(default_factory=list)
    user_defined_fields: dict[str, String] = field(default_factory=dict)
    verification_state: str | None = None
    workflow: WorkflowUpdate | None = None


@dataclass
class AutomationRulesFindingFilters(PropertyType):
    aws_account_id: list[StringFilter] = field(default_factory=list)
    company_name: list[StringFilter] = field(default_factory=list)
    compliance_associated_standards_id: list[StringFilter] = field(default_factory=list)
    compliance_security_control_id: list[StringFilter] = field(default_factory=list)
    compliance_status: list[StringFilter] = field(default_factory=list)
    confidence: list[NumberFilter] = field(default_factory=list)
    created_at: list[DateFilter] = field(default_factory=list)
    criticality: list[NumberFilter] = field(default_factory=list)
    description: list[StringFilter] = field(default_factory=list)
    first_observed_at: list[DateFilter] = field(default_factory=list)
    generator_id: list[StringFilter] = field(default_factory=list)
    id: list[StringFilter] = field(default_factory=list)
    last_observed_at: list[DateFilter] = field(default_factory=list)
    note_text: list[StringFilter] = field(default_factory=list)
    note_updated_at: list[DateFilter] = field(default_factory=list)
    note_updated_by: list[StringFilter] = field(default_factory=list)
    product_arn: list[StringFilter] = field(default_factory=list)
    product_name: list[StringFilter] = field(default_factory=list)
    record_state: list[StringFilter] = field(default_factory=list)
    related_findings_id: list[StringFilter] = field(default_factory=list)
    related_findings_product_arn: list[StringFilter] = field(default_factory=list)
    resource_details_other: list[MapFilter] = field(default_factory=list)
    resource_id: list[StringFilter] = field(default_factory=list)
    resource_partition: list[StringFilter] = field(default_factory=list)
    resource_region: list[StringFilter] = field(default_factory=list)
    resource_tags: list[MapFilter] = field(default_factory=list)
    resource_type: list[StringFilter] = field(default_factory=list)
    severity_label: list[StringFilter] = field(default_factory=list)
    source_url: list[StringFilter] = field(default_factory=list)
    title: list[StringFilter] = field(default_factory=list)
    type_: list[StringFilter] = field(default_factory=list)
    updated_at: list[DateFilter] = field(default_factory=list)
    user_defined_fields: list[MapFilter] = field(default_factory=list)
    verification_state: list[StringFilter] = field(default_factory=list)
    workflow_status: list[StringFilter] = field(default_factory=list)


@dataclass
class DateFilter(PropertyType):
    date_range: DateRange | None = None
    end: str | None = None
    start: str | None = None


@dataclass
class DateRange(PropertyType):
    unit: str | None = None
    value: float | None = None


@dataclass
class MapFilter(PropertyType):
    comparison: str | None = None
    key: str | None = None
    value: str | None = None


@dataclass
class NoteUpdate(PropertyType):
    text: str | None = None
    updated_by: dict[str, Any] | None = None


@dataclass
class NumberFilter(PropertyType):
    eq: float | None = None
    gte: float | None = None
    lte: float | None = None


@dataclass
class RelatedFinding(PropertyType):
    id: dict[str, Any] | None = None
    product_arn: str | None = None


@dataclass
class SeverityUpdate(PropertyType):
    label: str | None = None
    normalized: int | None = None
    product: float | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: str | None = None
    value: str | None = None


@dataclass
class WorkflowUpdate(PropertyType):
    status: str | None = None
