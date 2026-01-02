"""PropertyTypes for AWS::ApplicationInsights::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Alarm(PropertyType):
    alarm_name: str | None = None
    severity: str | None = None


@dataclass
class AlarmMetric(PropertyType):
    alarm_metric_name: str | None = None


@dataclass
class ComponentConfiguration(PropertyType):
    configuration_details: ConfigurationDetails | None = None
    sub_component_type_configurations: list[SubComponentTypeConfiguration] = field(
        default_factory=list
    )


@dataclass
class ComponentMonitoringSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "component_arn": "ComponentARN",
    }

    component_configuration_mode: str | None = None
    tier: str | None = None
    component_arn: str | None = None
    component_name: str | None = None
    custom_component_configuration: ComponentConfiguration | None = None
    default_overwrite_component_configuration: ComponentConfiguration | None = None


@dataclass
class ConfigurationDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ha_cluster_prometheus_exporter": "HAClusterPrometheusExporter",
        "hana_prometheus_exporter": "HANAPrometheusExporter",
        "jmx_prometheus_exporter": "JMXPrometheusExporter",
        "sql_server_prometheus_exporter": "SQLServerPrometheusExporter",
    }

    alarm_metrics: list[AlarmMetric] = field(default_factory=list)
    alarms: list[Alarm] = field(default_factory=list)
    ha_cluster_prometheus_exporter: HAClusterPrometheusExporter | None = None
    hana_prometheus_exporter: HANAPrometheusExporter | None = None
    jmx_prometheus_exporter: JMXPrometheusExporter | None = None
    logs: list[Log] = field(default_factory=list)
    net_weaver_prometheus_exporter: NetWeaverPrometheusExporter | None = None
    processes: list[Process] = field(default_factory=list)
    sql_server_prometheus_exporter: SQLServerPrometheusExporter | None = None
    windows_events: list[WindowsEvent] = field(default_factory=list)


@dataclass
class CustomComponent(PropertyType):
    component_name: str | None = None
    resource_list: list[String] = field(default_factory=list)


@dataclass
class HAClusterPrometheusExporter(PropertyType):
    prometheus_port: str | None = None


@dataclass
class HANAPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "agree_to_install_hanadb_client": "AgreeToInstallHANADBClient",
        "hana_port": "HANAPort",
        "hana_secret_name": "HANASecretName",
        "hanasid": "HANASID",
    }

    agree_to_install_hanadb_client: bool | None = None
    hana_port: str | None = None
    hana_secret_name: str | None = None
    hanasid: str | None = None
    prometheus_port: str | None = None


@dataclass
class JMXPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "jmxurl": "JMXURL",
    }

    host_port: str | None = None
    jmxurl: str | None = None
    prometheus_port: str | None = None


@dataclass
class Log(PropertyType):
    log_type: str | None = None
    encoding: str | None = None
    log_group_name: str | None = None
    log_path: str | None = None
    pattern_set: str | None = None


@dataclass
class LogPattern(PropertyType):
    pattern: str | None = None
    pattern_name: str | None = None
    rank: int | None = None


@dataclass
class LogPatternSet(PropertyType):
    log_patterns: list[LogPattern] = field(default_factory=list)
    pattern_set_name: str | None = None


@dataclass
class NetWeaverPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapsid": "SAPSID",
    }

    instance_numbers: list[String] = field(default_factory=list)
    sapsid: str | None = None
    prometheus_port: str | None = None


@dataclass
class Process(PropertyType):
    alarm_metrics: list[AlarmMetric] = field(default_factory=list)
    process_name: str | None = None


@dataclass
class SQLServerPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sql_secret_name": "SQLSecretName",
    }

    prometheus_port: str | None = None
    sql_secret_name: str | None = None


@dataclass
class SubComponentConfigurationDetails(PropertyType):
    alarm_metrics: list[AlarmMetric] = field(default_factory=list)
    logs: list[Log] = field(default_factory=list)
    processes: list[Process] = field(default_factory=list)
    windows_events: list[WindowsEvent] = field(default_factory=list)


@dataclass
class SubComponentTypeConfiguration(PropertyType):
    sub_component_configuration_details: SubComponentConfigurationDetails | None = None
    sub_component_type: str | None = None


@dataclass
class WindowsEvent(PropertyType):
    event_levels: list[String] = field(default_factory=list)
    event_name: str | None = None
    log_group_name: str | None = None
    pattern_set: str | None = None
