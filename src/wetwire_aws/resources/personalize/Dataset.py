"""PropertyTypes for AWS::Personalize::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataSource(PropertyType):
    data_location: DslValue[str] | None = None


@dataclass
class DatasetImportJob(PropertyType):
    data_source: DslValue[DataSource] | None = None
    dataset_arn: DslValue[str] | None = None
    dataset_import_job_arn: DslValue[str] | None = None
    job_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
