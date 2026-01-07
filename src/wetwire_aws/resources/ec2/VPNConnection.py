"""PropertyTypes for AWS::EC2::VPNConnection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudwatchLogOptionsSpecification(PropertyType):
    bgp_log_enabled: DslValue[bool] | None = None
    bgp_log_group_arn: DslValue[str] | None = None
    bgp_log_output_format: DslValue[str] | None = None
    log_enabled: DslValue[bool] | None = None
    log_group_arn: DslValue[str] | None = None
    log_output_format: DslValue[str] | None = None


@dataclass
class IKEVersionsRequestListValue(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class Phase1DHGroupNumbersRequestListValue(PropertyType):
    value: DslValue[int] | None = None


@dataclass
class Phase1EncryptionAlgorithmsRequestListValue(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class Phase1IntegrityAlgorithmsRequestListValue(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class Phase2DHGroupNumbersRequestListValue(PropertyType):
    value: DslValue[int] | None = None


@dataclass
class Phase2EncryptionAlgorithmsRequestListValue(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class Phase2IntegrityAlgorithmsRequestListValue(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class VpnTunnelLogOptionsSpecification(PropertyType):
    cloudwatch_log_options: DslValue[CloudwatchLogOptionsSpecification] | None = None


@dataclass
class VpnTunnelOptionsSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dpd_timeout_action": "DPDTimeoutAction",
        "dpd_timeout_seconds": "DPDTimeoutSeconds",
        "ike_versions": "IKEVersions",
        "phase1_dh_group_numbers": "Phase1DHGroupNumbers",
        "phase2_dh_group_numbers": "Phase2DHGroupNumbers",
    }

    dpd_timeout_action: DslValue[str] | None = None
    dpd_timeout_seconds: DslValue[int] | None = None
    enable_tunnel_lifecycle_control: DslValue[bool] | None = None
    ike_versions: list[DslValue[IKEVersionsRequestListValue]] = field(
        default_factory=list
    )
    log_options: DslValue[VpnTunnelLogOptionsSpecification] | None = None
    phase1_dh_group_numbers: list[DslValue[Phase1DHGroupNumbersRequestListValue]] = (
        field(default_factory=list)
    )
    phase1_encryption_algorithms: list[
        DslValue[Phase1EncryptionAlgorithmsRequestListValue]
    ] = field(default_factory=list)
    phase1_integrity_algorithms: list[
        DslValue[Phase1IntegrityAlgorithmsRequestListValue]
    ] = field(default_factory=list)
    phase1_lifetime_seconds: DslValue[int] | None = None
    phase2_dh_group_numbers: list[DslValue[Phase2DHGroupNumbersRequestListValue]] = (
        field(default_factory=list)
    )
    phase2_encryption_algorithms: list[
        DslValue[Phase2EncryptionAlgorithmsRequestListValue]
    ] = field(default_factory=list)
    phase2_integrity_algorithms: list[
        DslValue[Phase2IntegrityAlgorithmsRequestListValue]
    ] = field(default_factory=list)
    phase2_lifetime_seconds: DslValue[int] | None = None
    pre_shared_key: DslValue[str] | None = None
    rekey_fuzz_percentage: DslValue[int] | None = None
    rekey_margin_time_seconds: DslValue[int] | None = None
    replay_window_size: DslValue[int] | None = None
    startup_action: DslValue[str] | None = None
    tunnel_inside_cidr: DslValue[str] | None = None
    tunnel_inside_ipv6_cidr: DslValue[str] | None = None
