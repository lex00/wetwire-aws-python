"""PropertyTypes for AWS::AppTest::TestCase."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Batch(PropertyType):
    batch_job_name: str | None = None
    batch_job_parameters: dict[str, String] = field(default_factory=dict)
    export_data_set_names: list[String] = field(default_factory=list)


@dataclass
class CloudFormationAction(PropertyType):
    resource: str | None = None
    action_type: str | None = None


@dataclass
class CompareAction(PropertyType):
    input: Input | None = None
    output: Output | None = None


@dataclass
class DataSet(PropertyType):
    ccsid: str | None = None
    format: str | None = None
    length: float | None = None
    name: str | None = None
    type_: str | None = None


@dataclass
class DatabaseCDC(PropertyType):
    source_metadata: SourceDatabaseMetadata | None = None
    target_metadata: TargetDatabaseMetadata | None = None


@dataclass
class FileMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_cdc": "DatabaseCDC",
    }

    data_sets: list[DataSet] = field(default_factory=list)
    database_cdc: DatabaseCDC | None = None


@dataclass
class Input(PropertyType):
    file: InputFile | None = None


@dataclass
class InputFile(PropertyType):
    file_metadata: FileMetadata | None = None
    source_location: str | None = None
    target_location: str | None = None


@dataclass
class M2ManagedActionProperties(PropertyType):
    force_stop: bool | None = None
    import_data_set_location: str | None = None


@dataclass
class M2ManagedApplicationAction(PropertyType):
    action_type: str | None = None
    resource: str | None = None
    properties: M2ManagedActionProperties | None = None


@dataclass
class M2NonManagedApplicationAction(PropertyType):
    action_type: str | None = None
    resource: str | None = None


@dataclass
class MainframeAction(PropertyType):
    action_type: MainframeActionType | None = None
    resource: str | None = None
    properties: MainframeActionProperties | None = None


@dataclass
class MainframeActionProperties(PropertyType):
    dms_task_arn: str | None = None


@dataclass
class MainframeActionType(PropertyType):
    batch: Batch | None = None
    tn3270: TN3270 | None = None


@dataclass
class Output(PropertyType):
    file: OutputFile | None = None


@dataclass
class OutputFile(PropertyType):
    file_location: str | None = None


@dataclass
class ResourceAction(PropertyType):
    cloud_formation_action: CloudFormationAction | None = None
    m2_managed_application_action: M2ManagedApplicationAction | None = None
    m2_non_managed_application_action: M2NonManagedApplicationAction | None = None


@dataclass
class Script(PropertyType):
    script_location: str | None = None
    type_: str | None = None


@dataclass
class SourceDatabaseMetadata(PropertyType):
    capture_tool: str | None = None
    type_: str | None = None


@dataclass
class Step(PropertyType):
    action: StepAction | None = None
    name: str | None = None
    description: str | None = None


@dataclass
class StepAction(PropertyType):
    compare_action: CompareAction | None = None
    mainframe_action: MainframeAction | None = None
    resource_action: ResourceAction | None = None


@dataclass
class TN3270(PropertyType):
    script: Script | None = None
    export_data_set_names: list[String] = field(default_factory=list)


@dataclass
class TargetDatabaseMetadata(PropertyType):
    capture_tool: str | None = None
    type_: str | None = None


@dataclass
class TestCaseLatestVersion(PropertyType):
    status: str | None = None
    version: float | None = None
