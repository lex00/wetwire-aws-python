"""PropertyTypes for AWS::OpsWorks::Stack."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ChefConfiguration(PropertyType):
    berkshelf_version: DslValue[str] | None = None
    manage_berkshelf: DslValue[bool] | None = None


@dataclass
class ElasticIp(PropertyType):
    ip: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class RdsDbInstance(PropertyType):
    db_password: DslValue[str] | None = None
    db_user: DslValue[str] | None = None
    rds_db_instance_arn: DslValue[str] | None = None


@dataclass
class Source(PropertyType):
    password: DslValue[str] | None = None
    revision: DslValue[str] | None = None
    ssh_key: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    url: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class StackConfigurationManager(PropertyType):
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None
