"""PropertyTypes for AWS::OpsWorks::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataSource(PropertyType):
    arn: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
    secure: DslValue[bool] | None = None


@dataclass
class Source(PropertyType):
    password: DslValue[str] | None = None
    revision: DslValue[str] | None = None
    ssh_key: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    url: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class SslConfiguration(PropertyType):
    certificate: DslValue[str] | None = None
    chain: DslValue[str] | None = None
    private_key: DslValue[str] | None = None
