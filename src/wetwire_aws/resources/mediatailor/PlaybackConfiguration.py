"""PropertyTypes for AWS::MediaTailor::PlaybackConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdConditioningConfiguration(PropertyType):
    streaming_media_file_conditioning: DslValue[str] | None = None


@dataclass
class AdDecisionServerConfiguration(PropertyType):
    http_request: DslValue[HttpRequest] | None = None


@dataclass
class AdMarkerPassthrough(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class AdsInteractionLog(PropertyType):
    exclude_event_types: list[DslValue[str]] = field(default_factory=list)
    publish_opt_in_event_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AvailSuppression(PropertyType):
    fill_policy: DslValue[str] | None = None
    mode: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Bumper(PropertyType):
    end_url: DslValue[str] | None = None
    start_url: DslValue[str] | None = None


@dataclass
class CdnConfiguration(PropertyType):
    ad_segment_url_prefix: DslValue[str] | None = None
    content_segment_url_prefix: DslValue[str] | None = None


@dataclass
class DashConfiguration(PropertyType):
    manifest_endpoint_prefix: DslValue[str] | None = None
    mpd_location: DslValue[str] | None = None
    origin_manifest_type: DslValue[str] | None = None


@dataclass
class HlsConfiguration(PropertyType):
    manifest_endpoint_prefix: DslValue[str] | None = None


@dataclass
class HttpRequest(PropertyType):
    body: DslValue[str] | None = None
    compress_request: DslValue[str] | None = None
    headers: dict[str, DslValue[str]] = field(default_factory=dict)
    http_method: DslValue[str] | None = None


@dataclass
class LivePreRollConfiguration(PropertyType):
    ad_decision_server_url: DslValue[str] | None = None
    max_duration_seconds: DslValue[int] | None = None


@dataclass
class LogConfiguration(PropertyType):
    percent_enabled: DslValue[int] | None = None
    ads_interaction_log: DslValue[AdsInteractionLog] | None = None
    enabled_logging_strategies: list[DslValue[str]] = field(default_factory=list)
    manifest_service_interaction_log: DslValue[ManifestServiceInteractionLog] | None = (
        None
    )


@dataclass
class ManifestProcessingRules(PropertyType):
    ad_marker_passthrough: DslValue[AdMarkerPassthrough] | None = None


@dataclass
class ManifestServiceInteractionLog(PropertyType):
    exclude_event_types: list[DslValue[str]] = field(default_factory=list)
