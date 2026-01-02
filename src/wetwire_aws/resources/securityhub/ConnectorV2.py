"""PropertyTypes for AWS::SecurityHub::ConnectorV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class JiraCloud(PropertyType):
    project_key: str | None = None
    auth_status: str | None = None
    auth_url: str | None = None
    cloud_id: str | None = None
    domain: str | None = None


@dataclass
class Provider(PropertyType):
    jira_cloud: JiraCloud | None = None
    service_now: ServiceNow | None = None


@dataclass
class ServiceNow(PropertyType):
    instance_name: str | None = None
    secret_arn: str | None = None
    auth_status: str | None = None
