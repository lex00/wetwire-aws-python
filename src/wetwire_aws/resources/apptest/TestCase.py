"""PropertyTypes for AWS::AppTest::TestCase."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Batch(PropertyType):
    batch_job_name: DslValue[str] | None = None
    batch_job_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    export_data_set_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CloudFormationAction(PropertyType):
    resource: DslValue[str] | None = None
    action_type: DslValue[str] | None = None


@dataclass
class CompareAction(PropertyType):
    input: DslValue[Input] | None = None
    output: DslValue[Output] | None = None


@dataclass
class DataSet(PropertyType):
    ccsid: DslValue[str] | None = None
    format: DslValue[str] | None = None
    length: DslValue[float] | None = None
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DatabaseCDC(PropertyType):
    source_metadata: DslValue[SourceDatabaseMetadata] | None = None
    target_metadata: DslValue[TargetDatabaseMetadata] | None = None


@dataclass
class FileMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_cdc": "DatabaseCDC",
    }

    data_sets: list[DslValue[DataSet]] = field(default_factory=list)
    database_cdc: DslValue[DatabaseCDC] | None = None


@dataclass
class Input(PropertyType):
    file: DslValue[InputFile] | None = None


@dataclass
class InputFile(PropertyType):
    file_metadata: DslValue[FileMetadata] | None = None
    source_location: DslValue[str] | None = None
    target_location: DslValue[str] | None = None


@dataclass
class M2ManagedActionProperties(PropertyType):
    force_stop: DslValue[bool] | None = None
    import_data_set_location: DslValue[str] | None = None


@dataclass
class M2ManagedApplicationAction(PropertyType):
    action_type: DslValue[str] | None = None
    resource: DslValue[str] | None = None
    properties: DslValue[M2ManagedActionProperties] | None = None


@dataclass
class M2NonManagedApplicationAction(PropertyType):
    action_type: DslValue[str] | None = None
    resource: DslValue[str] | None = None


@dataclass
class MainframeAction(PropertyType):
    action_type: DslValue[MainframeActionType] | None = None
    resource: DslValue[str] | None = None
    properties: DslValue[MainframeActionProperties] | None = None


@dataclass
class MainframeActionProperties(PropertyType):
    dms_task_arn: DslValue[str] | None = None


@dataclass
class MainframeActionType(PropertyType):
    batch: DslValue[Batch] | None = None
    tn3270: DslValue[TN3270] | None = None


@dataclass
class Output(PropertyType):
    file: DslValue[OutputFile] | None = None


@dataclass
class OutputFile(PropertyType):
    file_location: DslValue[str] | None = None


@dataclass
class ResourceAction(PropertyType):
    cloud_formation_action: DslValue[CloudFormationAction] | None = None
    m2_managed_application_action: DslValue[M2ManagedApplicationAction] | None = None
    m2_non_managed_application_action: (
        DslValue[M2NonManagedApplicationAction] | None
    ) = None


@dataclass
class Script(PropertyType):
    script_location: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class SourceDatabaseMetadata(PropertyType):
    capture_tool: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class Step(PropertyType):
    action: DslValue[StepAction] | None = None
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class StepAction(PropertyType):
    compare_action: DslValue[CompareAction] | None = None
    mainframe_action: DslValue[MainframeAction] | None = None
    resource_action: DslValue[ResourceAction] | None = None


@dataclass
class TN3270(PropertyType):
    script: DslValue[Script] | None = None
    export_data_set_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TargetDatabaseMetadata(PropertyType):
    capture_tool: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class TestCaseLatestVersion(PropertyType):
    status: DslValue[str] | None = None
    version: DslValue[float] | None = None
