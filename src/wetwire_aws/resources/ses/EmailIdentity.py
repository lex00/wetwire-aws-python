"""PropertyTypes for AWS::SES::EmailIdentity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationSetAttributes(PropertyType):
    configuration_set_name: DslValue[str] | None = None


@dataclass
class DkimAttributes(PropertyType):
    signing_enabled: DslValue[bool] | None = None


@dataclass
class DkimSigningAttributes(PropertyType):
    domain_signing_private_key: DslValue[str] | None = None
    domain_signing_selector: DslValue[str] | None = None
    next_signing_key_length: DslValue[str] | None = None


@dataclass
class FeedbackAttributes(PropertyType):
    email_forwarding_enabled: DslValue[bool] | None = None


@dataclass
class MailFromAttributes(PropertyType):
    behavior_on_mx_failure: DslValue[str] | None = None
    mail_from_domain: DslValue[str] | None = None
