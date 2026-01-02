"""PropertyTypes for AWS::Kendra::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomDocumentEnrichmentConfiguration(PropertyType):
    inline_configurations: list[InlineCustomDocumentEnrichmentConfiguration] = field(
        default_factory=list
    )
    post_extraction_hook_configuration: HookConfiguration | None = None
    pre_extraction_hook_configuration: HookConfiguration | None = None
    role_arn: str | None = None


@dataclass
class DataSourceConfiguration(PropertyType):
    template_configuration: TemplateConfiguration | None = None


@dataclass
class DocumentAttributeCondition(PropertyType):
    condition_document_attribute_key: str | None = None
    operator: str | None = None
    condition_on_value: DocumentAttributeValue | None = None


@dataclass
class DocumentAttributeTarget(PropertyType):
    target_document_attribute_key: str | None = None
    target_document_attribute_value: DocumentAttributeValue | None = None
    target_document_attribute_value_deletion: bool | None = None


@dataclass
class DocumentAttributeValue(PropertyType):
    date_value: str | None = None
    long_value: int | None = None
    string_list_value: list[String] = field(default_factory=list)
    string_value: str | None = None


@dataclass
class HookConfiguration(PropertyType):
    lambda_arn: str | None = None
    s3_bucket: str | None = None
    invocation_condition: DocumentAttributeCondition | None = None


@dataclass
class InlineCustomDocumentEnrichmentConfiguration(PropertyType):
    condition: DocumentAttributeCondition | None = None
    document_content_deletion: bool | None = None
    target: DocumentAttributeTarget | None = None


@dataclass
class TemplateConfiguration(PropertyType):
    template: dict[str, Any] | None = None
