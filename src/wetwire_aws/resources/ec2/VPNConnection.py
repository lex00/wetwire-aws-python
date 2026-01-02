"""PropertyTypes for AWS::EC2::VPNConnection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudwatchLogOptionsSpecification(PropertyType):
    bgp_log_enabled: bool | None = None
    bgp_log_group_arn: str | None = None
    bgp_log_output_format: str | None = None
    log_enabled: bool | None = None
    log_group_arn: str | None = None
    log_output_format: str | None = None


@dataclass
class IKEVersionsRequestListValue(PropertyType):
    value: str | None = None


@dataclass
class Phase1DHGroupNumbersRequestListValue(PropertyType):
    value: int | None = None


@dataclass
class Phase1EncryptionAlgorithmsRequestListValue(PropertyType):
    value: str | None = None


@dataclass
class Phase1IntegrityAlgorithmsRequestListValue(PropertyType):
    value: str | None = None


@dataclass
class Phase2DHGroupNumbersRequestListValue(PropertyType):
    value: int | None = None


@dataclass
class Phase2EncryptionAlgorithmsRequestListValue(PropertyType):
    value: str | None = None


@dataclass
class Phase2IntegrityAlgorithmsRequestListValue(PropertyType):
    value: str | None = None


@dataclass
class VpnTunnelLogOptionsSpecification(PropertyType):
    cloudwatch_log_options: CloudwatchLogOptionsSpecification | None = None


@dataclass
class VpnTunnelOptionsSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dpd_timeout_action": "DPDTimeoutAction",
        "dpd_timeout_seconds": "DPDTimeoutSeconds",
        "ike_versions": "IKEVersions",
        "phase1_dh_group_numbers": "Phase1DHGroupNumbers",
        "phase2_dh_group_numbers": "Phase2DHGroupNumbers",
    }

    dpd_timeout_action: str | None = None
    dpd_timeout_seconds: int | None = None
    enable_tunnel_lifecycle_control: bool | None = None
    ike_versions: list[IKEVersionsRequestListValue] = field(default_factory=list)
    log_options: VpnTunnelLogOptionsSpecification | None = None
    phase1_dh_group_numbers: list[Phase1DHGroupNumbersRequestListValue] = field(
        default_factory=list
    )
    phase1_encryption_algorithms: list[Phase1EncryptionAlgorithmsRequestListValue] = (
        field(default_factory=list)
    )
    phase1_integrity_algorithms: list[Phase1IntegrityAlgorithmsRequestListValue] = (
        field(default_factory=list)
    )
    phase1_lifetime_seconds: int | None = None
    phase2_dh_group_numbers: list[Phase2DHGroupNumbersRequestListValue] = field(
        default_factory=list
    )
    phase2_encryption_algorithms: list[Phase2EncryptionAlgorithmsRequestListValue] = (
        field(default_factory=list)
    )
    phase2_integrity_algorithms: list[Phase2IntegrityAlgorithmsRequestListValue] = (
        field(default_factory=list)
    )
    phase2_lifetime_seconds: int | None = None
    pre_shared_key: str | None = None
    rekey_fuzz_percentage: int | None = None
    rekey_margin_time_seconds: int | None = None
    replay_window_size: int | None = None
    startup_action: str | None = None
    tunnel_inside_cidr: str | None = None
    tunnel_inside_ipv6_cidr: str | None = None
