"""PropertyTypes for AWS::Connect::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Attributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "use_custom_tts_voices": "UseCustomTTSVoices",
    }

    inbound_calls: DslValue[bool] | None = None
    outbound_calls: DslValue[bool] | None = None
    auto_resolve_best_voices: DslValue[bool] | None = None
    contact_lens: DslValue[bool] | None = None
    contactflow_logs: DslValue[bool] | None = None
    early_media: DslValue[bool] | None = None
    enhanced_chat_monitoring: DslValue[bool] | None = None
    enhanced_contact_monitoring: DslValue[bool] | None = None
    high_volume_out_bound: DslValue[bool] | None = None
    multi_party_chat_conference: DslValue[bool] | None = None
    multi_party_conference: DslValue[bool] | None = None
    use_custom_tts_voices: DslValue[bool] | None = None
