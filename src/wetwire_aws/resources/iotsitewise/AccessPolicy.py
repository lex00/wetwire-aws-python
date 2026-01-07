"""PropertyTypes for AWS::IoTSiteWise::AccessPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessPolicyIdentity(PropertyType):
    iam_role: DslValue[IamRole] | None = None
    iam_user: DslValue[IamUser] | None = None
    user: DslValue[User] | None = None


@dataclass
class AccessPolicyResource(PropertyType):
    portal: DslValue[Portal] | None = None
    project: DslValue[Project] | None = None


@dataclass
class IamRole(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "arn",
    }

    arn: DslValue[str] | None = None


@dataclass
class IamUser(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "arn",
    }

    arn: DslValue[str] | None = None


@dataclass
class Portal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: DslValue[str] | None = None


@dataclass
class Project(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: DslValue[str] | None = None


@dataclass
class User(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: DslValue[str] | None = None
