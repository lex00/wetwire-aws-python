"""PropertyTypes for AWS::Connect::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Attributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "use_custom_tts_voices": "UseCustomTTSVoices",
    }

    inbound_calls: bool | None = None
    outbound_calls: bool | None = None
    auto_resolve_best_voices: bool | None = None
    contact_lens: bool | None = None
    contactflow_logs: bool | None = None
    early_media: bool | None = None
    enhanced_chat_monitoring: bool | None = None
    enhanced_contact_monitoring: bool | None = None
    high_volume_out_bound: bool | None = None
    multi_party_chat_conference: bool | None = None
    multi_party_conference: bool | None = None
    use_custom_tts_voices: bool | None = None
