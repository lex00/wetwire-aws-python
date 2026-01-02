"""PropertyTypes for AWS::Invoicing::InvoiceUnit."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourceTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class Rule(PropertyType):
    linked_accounts: list[String] = field(default_factory=list)
