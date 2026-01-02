"""PropertyTypes for AWS::Greengrass::FunctionDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DefaultConfig(PropertyType):
    execution: Execution | None = None


@dataclass
class Environment(PropertyType):
    access_sysfs: bool | None = None
    execution: Execution | None = None
    resource_access_policies: list[ResourceAccessPolicy] = field(default_factory=list)
    variables: dict[str, Any] | None = None


@dataclass
class Execution(PropertyType):
    isolation_mode: str | None = None
    run_as: RunAs | None = None


@dataclass
class Function(PropertyType):
    function_arn: str | None = None
    function_configuration: FunctionConfiguration | None = None
    id: str | None = None


@dataclass
class FunctionConfiguration(PropertyType):
    encoding_type: str | None = None
    environment: Environment | None = None
    exec_args: str | None = None
    executable: str | None = None
    memory_size: int | None = None
    pinned: bool | None = None
    timeout: int | None = None


@dataclass
class ResourceAccessPolicy(PropertyType):
    resource_id: str | None = None
    permission: str | None = None


@dataclass
class RunAs(PropertyType):
    gid: int | None = None
    uid: int | None = None
