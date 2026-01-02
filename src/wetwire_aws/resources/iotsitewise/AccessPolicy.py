"""PropertyTypes for AWS::IoTSiteWise::AccessPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessPolicyIdentity(PropertyType):
    iam_role: IamRole | None = None
    iam_user: IamUser | None = None
    user: User | None = None


@dataclass
class AccessPolicyResource(PropertyType):
    portal: Portal | None = None
    project: Project | None = None


@dataclass
class IamRole(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "arn",
    }

    arn: str | None = None


@dataclass
class IamUser(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "arn",
    }

    arn: str | None = None


@dataclass
class Portal(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: str | None = None


@dataclass
class Project(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: str | None = None


@dataclass
class User(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "id": "id",
    }

    id: str | None = None
