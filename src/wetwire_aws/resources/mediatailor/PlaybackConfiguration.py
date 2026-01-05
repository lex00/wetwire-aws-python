"""PropertyTypes for AWS::MediaTailor::PlaybackConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdConditioningConfiguration(PropertyType):
    streaming_media_file_conditioning: str | None = None


@dataclass
class AdDecisionServerConfiguration(PropertyType):
    http_request: HttpRequest | None = None


@dataclass
class AdMarkerPassthrough(PropertyType):
    enabled: bool | None = None


@dataclass
class AdsInteractionLog(PropertyType):
    exclude_event_types: list[String] = field(default_factory=list)
    publish_opt_in_event_types: list[String] = field(default_factory=list)


@dataclass
class AvailSuppression(PropertyType):
    fill_policy: str | None = None
    mode: str | None = None
    value: str | None = None


@dataclass
class Bumper(PropertyType):
    end_url: str | None = None
    start_url: str | None = None


@dataclass
class CdnConfiguration(PropertyType):
    ad_segment_url_prefix: str | None = None
    content_segment_url_prefix: str | None = None


@dataclass
class DashConfiguration(PropertyType):
    manifest_endpoint_prefix: str | None = None
    mpd_location: str | None = None
    origin_manifest_type: str | None = None


@dataclass
class HlsConfiguration(PropertyType):
    manifest_endpoint_prefix: str | None = None


@dataclass
class HttpRequest(PropertyType):
    body: str | None = None
    compress_request: str | None = None
    headers: dict[str, String] = field(default_factory=dict)
    http_method: str | None = None


@dataclass
class LivePreRollConfiguration(PropertyType):
    ad_decision_server_url: str | None = None
    max_duration_seconds: int | None = None


@dataclass
class LogConfiguration(PropertyType):
    percent_enabled: int | None = None
    ads_interaction_log: AdsInteractionLog | None = None
    enabled_logging_strategies: list[String] = field(default_factory=list)
    manifest_service_interaction_log: ManifestServiceInteractionLog | None = None


@dataclass
class ManifestProcessingRules(PropertyType):
    ad_marker_passthrough: AdMarkerPassthrough | None = None


@dataclass
class ManifestServiceInteractionLog(PropertyType):
    exclude_event_types: list[String] = field(default_factory=list)
