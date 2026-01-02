"""PropertyTypes for AWS::OpsWorks::Stack."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ChefConfiguration(PropertyType):
    berkshelf_version: str | None = None
    manage_berkshelf: bool | None = None


@dataclass
class ElasticIp(PropertyType):
    ip: str | None = None
    name: str | None = None


@dataclass
class RdsDbInstance(PropertyType):
    db_password: str | None = None
    db_user: str | None = None
    rds_db_instance_arn: str | None = None


@dataclass
class Source(PropertyType):
    password: str | None = None
    revision: str | None = None
    ssh_key: str | None = None
    type_: str | None = None
    url: str | None = None
    username: str | None = None


@dataclass
class StackConfigurationManager(PropertyType):
    name: str | None = None
    version: str | None = None
