"""PropertyTypes for AWS::Config::ConformancePack."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConformancePackInputParameter(PropertyType):
    parameter_name: str | None = None
    parameter_value: str | None = None


@dataclass
class TemplateSSMDocumentDetails(PropertyType):
    document_name: str | None = None
    document_version: str | None = None
