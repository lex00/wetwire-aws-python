"""PropertyTypes for AWS::ApplicationInsights::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Alarm(PropertyType):
    alarm_name: DslValue[str] | None = None
    severity: DslValue[str] | None = None


@dataclass
class AlarmMetric(PropertyType):
    alarm_metric_name: DslValue[str] | None = None


@dataclass
class ComponentConfiguration(PropertyType):
    configuration_details: DslValue[ConfigurationDetails] | None = None
    sub_component_type_configurations: list[DslValue[SubComponentTypeConfiguration]] = (
        field(default_factory=list)
    )


@dataclass
class ComponentMonitoringSetting(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "component_arn": "ComponentARN",
    }

    component_configuration_mode: DslValue[str] | None = None
    tier: DslValue[str] | None = None
    component_arn: DslValue[str] | None = None
    component_name: DslValue[str] | None = None
    custom_component_configuration: DslValue[ComponentConfiguration] | None = None
    default_overwrite_component_configuration: (
        DslValue[ComponentConfiguration] | None
    ) = None


@dataclass
class ConfigurationDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ha_cluster_prometheus_exporter": "HAClusterPrometheusExporter",
        "hana_prometheus_exporter": "HANAPrometheusExporter",
        "jmx_prometheus_exporter": "JMXPrometheusExporter",
        "sql_server_prometheus_exporter": "SQLServerPrometheusExporter",
    }

    alarm_metrics: list[DslValue[AlarmMetric]] = field(default_factory=list)
    alarms: list[DslValue[Alarm]] = field(default_factory=list)
    ha_cluster_prometheus_exporter: DslValue[HAClusterPrometheusExporter] | None = None
    hana_prometheus_exporter: DslValue[HANAPrometheusExporter] | None = None
    jmx_prometheus_exporter: DslValue[JMXPrometheusExporter] | None = None
    logs: list[DslValue[Log]] = field(default_factory=list)
    net_weaver_prometheus_exporter: DslValue[NetWeaverPrometheusExporter] | None = None
    processes: list[DslValue[Process]] = field(default_factory=list)
    sql_server_prometheus_exporter: DslValue[SQLServerPrometheusExporter] | None = None
    windows_events: list[DslValue[WindowsEvent]] = field(default_factory=list)


@dataclass
class CustomComponent(PropertyType):
    component_name: DslValue[str] | None = None
    resource_list: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HAClusterPrometheusExporter(PropertyType):
    prometheus_port: DslValue[str] | None = None


@dataclass
class HANAPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "agree_to_install_hanadb_client": "AgreeToInstallHANADBClient",
        "hana_port": "HANAPort",
        "hana_secret_name": "HANASecretName",
        "hanasid": "HANASID",
    }

    agree_to_install_hanadb_client: DslValue[bool] | None = None
    hana_port: DslValue[str] | None = None
    hana_secret_name: DslValue[str] | None = None
    hanasid: DslValue[str] | None = None
    prometheus_port: DslValue[str] | None = None


@dataclass
class JMXPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "jmxurl": "JMXURL",
    }

    host_port: DslValue[str] | None = None
    jmxurl: DslValue[str] | None = None
    prometheus_port: DslValue[str] | None = None


@dataclass
class Log(PropertyType):
    log_type: DslValue[str] | None = None
    encoding: DslValue[str] | None = None
    log_group_name: DslValue[str] | None = None
    log_path: DslValue[str] | None = None
    pattern_set: DslValue[str] | None = None


@dataclass
class LogPattern(PropertyType):
    pattern: DslValue[str] | None = None
    pattern_name: DslValue[str] | None = None
    rank: DslValue[int] | None = None


@dataclass
class LogPatternSet(PropertyType):
    log_patterns: list[DslValue[LogPattern]] = field(default_factory=list)
    pattern_set_name: DslValue[str] | None = None


@dataclass
class NetWeaverPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapsid": "SAPSID",
    }

    instance_numbers: list[DslValue[str]] = field(default_factory=list)
    sapsid: DslValue[str] | None = None
    prometheus_port: DslValue[str] | None = None


@dataclass
class Process(PropertyType):
    alarm_metrics: list[DslValue[AlarmMetric]] = field(default_factory=list)
    process_name: DslValue[str] | None = None


@dataclass
class SQLServerPrometheusExporter(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sql_secret_name": "SQLSecretName",
    }

    prometheus_port: DslValue[str] | None = None
    sql_secret_name: DslValue[str] | None = None


@dataclass
class SubComponentConfigurationDetails(PropertyType):
    alarm_metrics: list[DslValue[AlarmMetric]] = field(default_factory=list)
    logs: list[DslValue[Log]] = field(default_factory=list)
    processes: list[DslValue[Process]] = field(default_factory=list)
    windows_events: list[DslValue[WindowsEvent]] = field(default_factory=list)


@dataclass
class SubComponentTypeConfiguration(PropertyType):
    sub_component_configuration_details: (
        DslValue[SubComponentConfigurationDetails] | None
    ) = None
    sub_component_type: DslValue[str] | None = None


@dataclass
class WindowsEvent(PropertyType):
    event_levels: list[DslValue[str]] = field(default_factory=list)
    event_name: DslValue[str] | None = None
    log_group_name: DslValue[str] | None = None
    pattern_set: DslValue[str] | None = None
