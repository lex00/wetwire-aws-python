"""PropertyTypes for AWS::SES::Template."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Template(PropertyType):
    subject_part: str | None = None
    html_part: str | None = None
    template_name: str | None = None
    text_part: str | None = None
