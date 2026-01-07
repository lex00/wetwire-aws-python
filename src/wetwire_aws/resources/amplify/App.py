"""PropertyTypes for AWS::Amplify::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoBranchCreationConfig(PropertyType):
    auto_branch_creation_patterns: list[DslValue[str]] = field(default_factory=list)
    basic_auth_config: DslValue[BasicAuthConfig] | None = None
    build_spec: DslValue[str] | None = None
    enable_auto_branch_creation: DslValue[bool] | None = None
    enable_auto_build: DslValue[bool] | None = None
    enable_performance_mode: DslValue[bool] | None = None
    enable_pull_request_preview: DslValue[bool] | None = None
    environment_variables: list[DslValue[EnvironmentVariable]] = field(
        default_factory=list
    )
    framework: DslValue[str] | None = None
    pull_request_environment_name: DslValue[str] | None = None
    stage: DslValue[str] | None = None


@dataclass
class BasicAuthConfig(PropertyType):
    enable_basic_auth: DslValue[bool] | None = None
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class CacheConfig(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class CustomRule(PropertyType):
    source: DslValue[str] | None = None
    target: DslValue[str] | None = None
    condition: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class JobConfig(PropertyType):
    build_compute_type: DslValue[str] | None = None
