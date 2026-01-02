"""PropertyTypes for AWS::IoTWireless::ServiceProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoRaWANServiceProfile(PropertyType):
    add_gw_metadata: bool | None = None
    channel_mask: str | None = None
    dev_status_req_freq: int | None = None
    dl_bucket_size: int | None = None
    dl_rate: int | None = None
    dl_rate_policy: str | None = None
    dr_max: int | None = None
    dr_min: int | None = None
    hr_allowed: bool | None = None
    min_gw_diversity: int | None = None
    nwk_geo_loc: bool | None = None
    pr_allowed: bool | None = None
    ra_allowed: bool | None = None
    report_dev_status_battery: bool | None = None
    report_dev_status_margin: bool | None = None
    target_per: int | None = None
    ul_bucket_size: int | None = None
    ul_rate: int | None = None
    ul_rate_policy: str | None = None
