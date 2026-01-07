"""PropertyTypes for AWS::SecurityHub::ConnectorV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class JiraCloudProviderConfiguration(PropertyType):
    project_key: DslValue[str] | None = None


@dataclass
class Provider(PropertyType):
    jira_cloud: DslValue[JiraCloudProviderConfiguration] | None = None
    service_now: DslValue[ServiceNowProviderConfiguration] | None = None


@dataclass
class ServiceNowProviderConfiguration(PropertyType):
    instance_name: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None
