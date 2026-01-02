"""PropertyTypes for AWS::Personalize::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataSource(PropertyType):
    data_location: str | None = None


@dataclass
class DatasetImportJob(PropertyType):
    data_source: DataSource | None = None
    dataset_arn: str | None = None
    dataset_import_job_arn: str | None = None
    job_name: str | None = None
    role_arn: str | None = None
