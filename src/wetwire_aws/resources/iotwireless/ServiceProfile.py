"""PropertyTypes for AWS::IoTWireless::ServiceProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoRaWANServiceProfile(PropertyType):
    add_gw_metadata: DslValue[bool] | None = None
    channel_mask: DslValue[str] | None = None
    dev_status_req_freq: DslValue[int] | None = None
    dl_bucket_size: DslValue[int] | None = None
    dl_rate: DslValue[int] | None = None
    dl_rate_policy: DslValue[str] | None = None
    dr_max: DslValue[int] | None = None
    dr_min: DslValue[int] | None = None
    hr_allowed: DslValue[bool] | None = None
    min_gw_diversity: DslValue[int] | None = None
    nwk_geo_loc: DslValue[bool] | None = None
    pr_allowed: DslValue[bool] | None = None
    ra_allowed: DslValue[bool] | None = None
    report_dev_status_battery: DslValue[bool] | None = None
    report_dev_status_margin: DslValue[bool] | None = None
    target_per: DslValue[int] | None = None
    ul_bucket_size: DslValue[int] | None = None
    ul_rate: DslValue[int] | None = None
    ul_rate_policy: DslValue[str] | None = None
