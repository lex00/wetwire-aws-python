"""PropertyTypes for AWS::IoT::MitigationAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionParams(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "update_ca_certificate_params": "UpdateCACertificateParams",
    }

    add_things_to_thing_group_params: DslValue[AddThingsToThingGroupParams] | None = (
        None
    )
    enable_io_t_logging_params: DslValue[EnableIoTLoggingParams] | None = None
    publish_finding_to_sns_params: DslValue[PublishFindingToSnsParams] | None = None
    replace_default_policy_version_params: (
        DslValue[ReplaceDefaultPolicyVersionParams] | None
    ) = None
    update_ca_certificate_params: DslValue[UpdateCACertificateParams] | None = None
    update_device_certificate_params: DslValue[UpdateDeviceCertificateParams] | None = (
        None
    )


@dataclass
class AddThingsToThingGroupParams(PropertyType):
    thing_group_names: list[DslValue[str]] = field(default_factory=list)
    override_dynamic_groups: DslValue[bool] | None = None


@dataclass
class EnableIoTLoggingParams(PropertyType):
    log_level: DslValue[str] | None = None
    role_arn_for_logging: DslValue[str] | None = None


@dataclass
class PublishFindingToSnsParams(PropertyType):
    topic_arn: DslValue[str] | None = None


@dataclass
class ReplaceDefaultPolicyVersionParams(PropertyType):
    template_name: DslValue[str] | None = None


@dataclass
class UpdateCACertificateParams(PropertyType):
    action: DslValue[str] | None = None


@dataclass
class UpdateDeviceCertificateParams(PropertyType):
    action: DslValue[str] | None = None
