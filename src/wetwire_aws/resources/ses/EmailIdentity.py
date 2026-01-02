"""PropertyTypes for AWS::SES::EmailIdentity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationSetAttributes(PropertyType):
    configuration_set_name: str | None = None


@dataclass
class DkimAttributes(PropertyType):
    signing_enabled: bool | None = None


@dataclass
class DkimSigningAttributes(PropertyType):
    domain_signing_private_key: str | None = None
    domain_signing_selector: str | None = None
    next_signing_key_length: str | None = None


@dataclass
class FeedbackAttributes(PropertyType):
    email_forwarding_enabled: bool | None = None


@dataclass
class MailFromAttributes(PropertyType):
    behavior_on_mx_failure: str | None = None
    mail_from_domain: str | None = None
