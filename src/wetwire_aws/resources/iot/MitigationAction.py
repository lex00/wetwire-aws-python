"""PropertyTypes for AWS::IoT::MitigationAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionParams(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "update_ca_certificate_params": "UpdateCACertificateParams",
    }

    add_things_to_thing_group_params: AddThingsToThingGroupParams | None = None
    enable_io_t_logging_params: EnableIoTLoggingParams | None = None
    publish_finding_to_sns_params: PublishFindingToSnsParams | None = None
    replace_default_policy_version_params: ReplaceDefaultPolicyVersionParams | None = (
        None
    )
    update_ca_certificate_params: UpdateCACertificateParams | None = None
    update_device_certificate_params: UpdateDeviceCertificateParams | None = None


@dataclass
class AddThingsToThingGroupParams(PropertyType):
    thing_group_names: list[String] = field(default_factory=list)
    override_dynamic_groups: bool | None = None


@dataclass
class EnableIoTLoggingParams(PropertyType):
    log_level: str | None = None
    role_arn_for_logging: str | None = None


@dataclass
class PublishFindingToSnsParams(PropertyType):
    topic_arn: str | None = None


@dataclass
class ReplaceDefaultPolicyVersionParams(PropertyType):
    template_name: str | None = None


@dataclass
class UpdateCACertificateParams(PropertyType):
    action: str | None = None


@dataclass
class UpdateDeviceCertificateParams(PropertyType):
    action: str | None = None
