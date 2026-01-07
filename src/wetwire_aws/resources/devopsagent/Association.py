"""PropertyTypes for AWS::DevOpsAgent::Association."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AWSConfiguration(PropertyType):
    account_id: DslValue[str] | None = None
    account_type: DslValue[str] | None = None
    assumable_role_arn: DslValue[str] | None = None
    resources: list[DslValue[AWSResource]] = field(default_factory=list)
    tags: list[DslValue[KeyValuePair]] = field(default_factory=list)


@dataclass
class AWSResource(PropertyType):
    resource_arn: DslValue[str] | None = None
    resource_metadata: DslValue[dict[str, Any]] | None = None
    resource_type: DslValue[str] | None = None


@dataclass
class DynatraceConfiguration(PropertyType):
    env_id: DslValue[str] | None = None
    enable_webhook_updates: DslValue[bool] | None = None
    resources: list[DslValue[str]] = field(default_factory=list)


@dataclass
class EventChannelConfiguration(PropertyType):
    enable_webhook_updates: DslValue[bool] | None = None


@dataclass
class GitHubConfiguration(PropertyType):
    owner: DslValue[str] | None = None
    owner_type: DslValue[str] | None = None
    repo_id: DslValue[str] | None = None
    repo_name: DslValue[str] | None = None


@dataclass
class GitLabConfiguration(PropertyType):
    project_id: DslValue[str] | None = None
    project_path: DslValue[str] | None = None
    enable_webhook_updates: DslValue[bool] | None = None
    instance_identifier: DslValue[str] | None = None


@dataclass
class KeyValuePair(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class MCPServerConfiguration(PropertyType):
    endpoint: DslValue[str] | None = None
    name: DslValue[str] | None = None
    tools: list[DslValue[str]] = field(default_factory=list)
    description: DslValue[str] | None = None
    enable_webhook_updates: DslValue[bool] | None = None


@dataclass
class MCPServerDatadogConfiguration(PropertyType):
    endpoint: DslValue[str] | None = None
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None
    enable_webhook_updates: DslValue[bool] | None = None


@dataclass
class MCPServerNewRelicConfiguration(PropertyType):
    account_id: DslValue[str] | None = None
    endpoint: DslValue[str] | None = None


@dataclass
class MCPServerSplunkConfiguration(PropertyType):
    endpoint: DslValue[str] | None = None
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None
    enable_webhook_updates: DslValue[bool] | None = None


@dataclass
class ServiceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mcp_server": "MCPServer",
        "mcp_server_datadog": "MCPServerDatadog",
        "mcp_server_new_relic": "MCPServerNewRelic",
        "mcp_server_splunk": "MCPServerSplunk",
    }

    aws: DslValue[AWSConfiguration] | None = None
    dynatrace: DslValue[DynatraceConfiguration] | None = None
    event_channel: DslValue[EventChannelConfiguration] | None = None
    git_hub: DslValue[GitHubConfiguration] | None = None
    git_lab: DslValue[GitLabConfiguration] | None = None
    mcp_server: DslValue[MCPServerConfiguration] | None = None
    mcp_server_datadog: DslValue[MCPServerDatadogConfiguration] | None = None
    mcp_server_new_relic: DslValue[MCPServerNewRelicConfiguration] | None = None
    mcp_server_splunk: DslValue[MCPServerSplunkConfiguration] | None = None
    service_now: DslValue[ServiceNowConfiguration] | None = None
    slack: DslValue[SlackConfiguration] | None = None
    source_aws: DslValue[SourceAwsConfiguration] | None = None


@dataclass
class ServiceNowConfiguration(PropertyType):
    enable_webhook_updates: DslValue[bool] | None = None
    instance_id: DslValue[str] | None = None


@dataclass
class SlackChannel(PropertyType):
    channel_id: DslValue[str] | None = None
    channel_name: DslValue[str] | None = None


@dataclass
class SlackConfiguration(PropertyType):
    transmission_target: DslValue[SlackTransmissionTarget] | None = None
    workspace_id: DslValue[str] | None = None
    workspace_name: DslValue[str] | None = None


@dataclass
class SlackTransmissionTarget(PropertyType):
    incident_response_target: DslValue[SlackChannel] | None = None


@dataclass
class SourceAwsConfiguration(PropertyType):
    account_id: DslValue[str] | None = None
    account_type: DslValue[str] | None = None
    assumable_role_arn: DslValue[str] | None = None
    resources: list[DslValue[AWSResource]] = field(default_factory=list)
    tags: list[DslValue[KeyValuePair]] = field(default_factory=list)
