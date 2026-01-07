"""PropertyTypes for AWS::Greengrass::FunctionDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DefaultConfig(PropertyType):
    execution: DslValue[Execution] | None = None


@dataclass
class Environment(PropertyType):
    access_sysfs: DslValue[bool] | None = None
    execution: DslValue[Execution] | None = None
    resource_access_policies: list[DslValue[ResourceAccessPolicy]] = field(
        default_factory=list
    )
    variables: DslValue[dict[str, Any]] | None = None


@dataclass
class Execution(PropertyType):
    isolation_mode: DslValue[str] | None = None
    run_as: DslValue[RunAs] | None = None


@dataclass
class Function(PropertyType):
    function_arn: DslValue[str] | None = None
    function_configuration: DslValue[FunctionConfiguration] | None = None
    id: DslValue[str] | None = None


@dataclass
class FunctionConfiguration(PropertyType):
    encoding_type: DslValue[str] | None = None
    environment: DslValue[Environment] | None = None
    exec_args: DslValue[str] | None = None
    executable: DslValue[str] | None = None
    memory_size: DslValue[int] | None = None
    pinned: DslValue[bool] | None = None
    timeout: DslValue[int] | None = None


@dataclass
class ResourceAccessPolicy(PropertyType):
    resource_id: DslValue[str] | None = None
    permission: DslValue[str] | None = None


@dataclass
class RunAs(PropertyType):
    gid: DslValue[int] | None = None
    uid: DslValue[int] | None = None
