"""PropertyTypes for AWS::InspectorV2::CodeSecurityIntegration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CreateDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "gitlab_self_managed": "gitlabSelfManaged",
    }

    gitlab_self_managed: CreateGitLabSelfManagedIntegrationDetail | None = None


@dataclass
class CreateGitLabSelfManagedIntegrationDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "access_token": "accessToken",
        "instance_url": "instanceUrl",
    }

    access_token: str | None = None
    instance_url: str | None = None


@dataclass
class UpdateDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "github": "github",
        "gitlab_self_managed": "gitlabSelfManaged",
    }

    github: UpdateGitHubIntegrationDetail | None = None
    gitlab_self_managed: UpdateGitLabSelfManagedIntegrationDetail | None = None


@dataclass
class UpdateGitHubIntegrationDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "code": "code",
        "installation_id": "installationId",
    }

    code: str | None = None
    installation_id: str | None = None


@dataclass
class UpdateGitLabSelfManagedIntegrationDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_code": "authCode",
    }

    auth_code: str | None = None
