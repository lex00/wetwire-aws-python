"""PropertyTypes for AWS::DevOpsAgent::Association."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AWSConfiguration(PropertyType):
    account_id: str | None = None
    account_type: str | None = None
    assumable_role_arn: str | None = None
    resources: list[AWSResource] = field(default_factory=list)
    tags: list[KeyValuePair] = field(default_factory=list)


@dataclass
class AWSResource(PropertyType):
    resource_arn: str | None = None
    resource_metadata: dict[str, Any] | None = None
    resource_type: str | None = None


@dataclass
class DynatraceConfiguration(PropertyType):
    env_id: str | None = None
    enable_webhook_updates: bool | None = None
    resources: list[String] = field(default_factory=list)


@dataclass
class EventChannelConfiguration(PropertyType):
    enable_webhook_updates: bool | None = None


@dataclass
class GitHubConfiguration(PropertyType):
    owner: str | None = None
    owner_type: str | None = None
    repo_id: str | None = None
    repo_name: str | None = None


@dataclass
class GitLabConfiguration(PropertyType):
    project_id: str | None = None
    project_path: str | None = None
    enable_webhook_updates: bool | None = None
    instance_identifier: str | None = None


@dataclass
class KeyValuePair(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class MCPServerConfiguration(PropertyType):
    endpoint: str | None = None
    name: str | None = None
    tools: list[String] = field(default_factory=list)
    description: str | None = None
    enable_webhook_updates: bool | None = None


@dataclass
class MCPServerDatadogConfiguration(PropertyType):
    endpoint: str | None = None
    name: str | None = None
    description: str | None = None
    enable_webhook_updates: bool | None = None


@dataclass
class MCPServerNewRelicConfiguration(PropertyType):
    account_id: str | None = None
    endpoint: str | None = None


@dataclass
class MCPServerSplunkConfiguration(PropertyType):
    endpoint: str | None = None
    name: str | None = None
    description: str | None = None
    enable_webhook_updates: bool | None = None


@dataclass
class ServiceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mcp_server": "MCPServer",
        "mcp_server_datadog": "MCPServerDatadog",
        "mcp_server_new_relic": "MCPServerNewRelic",
        "mcp_server_splunk": "MCPServerSplunk",
    }

    aws: AWSConfiguration | None = None
    dynatrace: DynatraceConfiguration | None = None
    event_channel: EventChannelConfiguration | None = None
    git_hub: GitHubConfiguration | None = None
    git_lab: GitLabConfiguration | None = None
    mcp_server: MCPServerConfiguration | None = None
    mcp_server_datadog: MCPServerDatadogConfiguration | None = None
    mcp_server_new_relic: MCPServerNewRelicConfiguration | None = None
    mcp_server_splunk: MCPServerSplunkConfiguration | None = None
    service_now: ServiceNowConfiguration | None = None
    slack: SlackConfiguration | None = None
    source_aws: SourceAwsConfiguration | None = None


@dataclass
class ServiceNowConfiguration(PropertyType):
    enable_webhook_updates: bool | None = None
    instance_id: str | None = None


@dataclass
class SlackChannel(PropertyType):
    channel_id: str | None = None
    channel_name: str | None = None


@dataclass
class SlackConfiguration(PropertyType):
    transmission_target: SlackTransmissionTarget | None = None
    workspace_id: str | None = None
    workspace_name: str | None = None


@dataclass
class SlackTransmissionTarget(PropertyType):
    incident_response_target: SlackChannel | None = None


@dataclass
class SourceAwsConfiguration(PropertyType):
    account_id: str | None = None
    account_type: str | None = None
    assumable_role_arn: str | None = None
    resources: list[AWSResource] = field(default_factory=list)
    tags: list[KeyValuePair] = field(default_factory=list)
