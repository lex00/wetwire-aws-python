"""PropertyTypes for AWS::GuardDuty::Detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CFNDataSourceConfigurations(PropertyType):
    kubernetes: CFNKubernetesConfiguration | None = None
    malware_protection: CFNMalwareProtectionConfiguration | None = None
    s3_logs: CFNS3LogsConfiguration | None = None


@dataclass
class CFNFeatureAdditionalConfiguration(PropertyType):
    name: str | None = None
    status: str | None = None


@dataclass
class CFNFeatureConfiguration(PropertyType):
    name: str | None = None
    status: str | None = None
    additional_configuration: list[CFNFeatureAdditionalConfiguration] = field(
        default_factory=list
    )


@dataclass
class CFNKubernetesAuditLogsConfiguration(PropertyType):
    enable: bool | None = None


@dataclass
class CFNKubernetesConfiguration(PropertyType):
    audit_logs: CFNKubernetesAuditLogsConfiguration | None = None


@dataclass
class CFNMalwareProtectionConfiguration(PropertyType):
    scan_ec2_instance_with_findings: (
        CFNScanEc2InstanceWithFindingsConfiguration | None
    ) = None


@dataclass
class CFNS3LogsConfiguration(PropertyType):
    enable: bool | None = None


@dataclass
class CFNScanEc2InstanceWithFindingsConfiguration(PropertyType):
    ebs_volumes: bool | None = None


@dataclass
class TagItem(PropertyType):
    key: str | None = None
    value: str | None = None
