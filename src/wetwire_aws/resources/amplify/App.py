"""PropertyTypes for AWS::Amplify::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoBranchCreationConfig(PropertyType):
    auto_branch_creation_patterns: list[String] = field(default_factory=list)
    basic_auth_config: BasicAuthConfig | None = None
    build_spec: str | None = None
    enable_auto_branch_creation: bool | None = None
    enable_auto_build: bool | None = None
    enable_performance_mode: bool | None = None
    enable_pull_request_preview: bool | None = None
    environment_variables: list[EnvironmentVariable] = field(default_factory=list)
    framework: str | None = None
    pull_request_environment_name: str | None = None
    stage: str | None = None


@dataclass
class BasicAuthConfig(PropertyType):
    enable_basic_auth: bool | None = None
    password: str | None = None
    username: str | None = None


@dataclass
class CacheConfig(PropertyType):
    type_: str | None = None


@dataclass
class CustomRule(PropertyType):
    source: str | None = None
    target: str | None = None
    condition: str | None = None
    status: str | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class JobConfig(PropertyType):
    build_compute_type: str | None = None
