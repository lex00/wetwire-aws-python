"""PropertyTypes for AWS::SES::MailManagerArchive."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ArchiveRetention(PropertyType):
    retention_period: str | None = None
