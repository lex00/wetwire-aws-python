"""PropertyTypes for AWS::SecurityHub::ConnectorV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class JiraCloudProviderConfiguration(PropertyType):
    project_key: str | None = None


@dataclass
class Provider(PropertyType):
    jira_cloud: JiraCloudProviderConfiguration | None = None
    service_now: ServiceNowProviderConfiguration | None = None


@dataclass
class ServiceNowProviderConfiguration(PropertyType):
    instance_name: str | None = None
    secret_arn: str | None = None
