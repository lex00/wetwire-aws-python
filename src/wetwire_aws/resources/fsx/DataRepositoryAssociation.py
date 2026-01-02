"""PropertyTypes for AWS::FSx::DataRepositoryAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoExportPolicy(PropertyType):
    events: list[String] = field(default_factory=list)


@dataclass
class AutoImportPolicy(PropertyType):
    events: list[String] = field(default_factory=list)


@dataclass
class S3(PropertyType):
    auto_export_policy: AutoExportPolicy | None = None
    auto_import_policy: AutoImportPolicy | None = None
