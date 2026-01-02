"""PropertyTypes for AWS::OpsWorks::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataSource(PropertyType):
    arn: str | None = None
    database_name: str | None = None
    type_: str | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    key: str | None = None
    value: str | None = None
    secure: bool | None = None


@dataclass
class Source(PropertyType):
    password: str | None = None
    revision: str | None = None
    ssh_key: str | None = None
    type_: str | None = None
    url: str | None = None
    username: str | None = None


@dataclass
class SslConfiguration(PropertyType):
    certificate: str | None = None
    chain: str | None = None
    private_key: str | None = None
