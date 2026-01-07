"""PropertyTypes for AWS::GuardDuty::Detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CFNDataSourceConfigurations(PropertyType):
    kubernetes: DslValue[CFNKubernetesConfiguration] | None = None
    malware_protection: DslValue[CFNMalwareProtectionConfiguration] | None = None
    s3_logs: DslValue[CFNS3LogsConfiguration] | None = None


@dataclass
class CFNFeatureAdditionalConfiguration(PropertyType):
    name: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class CFNFeatureConfiguration(PropertyType):
    name: DslValue[str] | None = None
    status: DslValue[str] | None = None
    additional_configuration: list[DslValue[CFNFeatureAdditionalConfiguration]] = field(
        default_factory=list
    )


@dataclass
class CFNKubernetesAuditLogsConfiguration(PropertyType):
    enable: DslValue[bool] | None = None


@dataclass
class CFNKubernetesConfiguration(PropertyType):
    audit_logs: DslValue[CFNKubernetesAuditLogsConfiguration] | None = None


@dataclass
class CFNMalwareProtectionConfiguration(PropertyType):
    scan_ec2_instance_with_findings: (
        DslValue[CFNScanEc2InstanceWithFindingsConfiguration] | None
    ) = None


@dataclass
class CFNS3LogsConfiguration(PropertyType):
    enable: DslValue[bool] | None = None


@dataclass
class CFNScanEc2InstanceWithFindingsConfiguration(PropertyType):
    ebs_volumes: DslValue[bool] | None = None


@dataclass
class TagItem(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
