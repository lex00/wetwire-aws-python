"""PropertyTypes for AWS::Kendra::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomDocumentEnrichmentConfiguration(PropertyType):
    inline_configurations: list[
        DslValue[InlineCustomDocumentEnrichmentConfiguration]
    ] = field(default_factory=list)
    post_extraction_hook_configuration: DslValue[HookConfiguration] | None = None
    pre_extraction_hook_configuration: DslValue[HookConfiguration] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class DataSourceConfiguration(PropertyType):
    template_configuration: DslValue[TemplateConfiguration] | None = None


@dataclass
class DocumentAttributeCondition(PropertyType):
    condition_document_attribute_key: DslValue[str] | None = None
    operator: DslValue[str] | None = None
    condition_on_value: DslValue[DocumentAttributeValue] | None = None


@dataclass
class DocumentAttributeTarget(PropertyType):
    target_document_attribute_key: DslValue[str] | None = None
    target_document_attribute_value: DslValue[DocumentAttributeValue] | None = None
    target_document_attribute_value_deletion: DslValue[bool] | None = None


@dataclass
class DocumentAttributeValue(PropertyType):
    date_value: DslValue[str] | None = None
    long_value: DslValue[int] | None = None
    string_list_value: list[DslValue[str]] = field(default_factory=list)
    string_value: DslValue[str] | None = None


@dataclass
class HookConfiguration(PropertyType):
    lambda_arn: DslValue[str] | None = None
    s3_bucket: DslValue[str] | None = None
    invocation_condition: DslValue[DocumentAttributeCondition] | None = None


@dataclass
class InlineCustomDocumentEnrichmentConfiguration(PropertyType):
    condition: DslValue[DocumentAttributeCondition] | None = None
    document_content_deletion: DslValue[bool] | None = None
    target: DslValue[DocumentAttributeTarget] | None = None


@dataclass
class TemplateConfiguration(PropertyType):
    template: DslValue[dict[str, Any]] | None = None
