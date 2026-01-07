"""PropertyTypes for AWS::Lex::BotAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AudioLogDestination(PropertyType):
    s3_bucket: DslValue[S3BucketLogDestination] | None = None


@dataclass
class AudioLogSetting(PropertyType):
    destination: DslValue[AudioLogDestination] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class BotAliasLocaleSettings(PropertyType):
    enabled: DslValue[bool] | None = None
    code_hook_specification: DslValue[CodeHookSpecification] | None = None


@dataclass
class BotAliasLocaleSettingsItem(PropertyType):
    bot_alias_locale_setting: DslValue[BotAliasLocaleSettings] | None = None
    locale_id: DslValue[str] | None = None


@dataclass
class CloudWatchLogGroupLogDestination(PropertyType):
    cloud_watch_log_group_arn: DslValue[str] | None = None
    log_prefix: DslValue[str] | None = None


@dataclass
class CodeHookSpecification(PropertyType):
    lambda_code_hook: DslValue[LambdaCodeHook] | None = None


@dataclass
class ConversationLogSettings(PropertyType):
    audio_log_settings: list[DslValue[AudioLogSetting]] = field(default_factory=list)
    text_log_settings: list[DslValue[TextLogSetting]] = field(default_factory=list)


@dataclass
class LambdaCodeHook(PropertyType):
    code_hook_interface_version: DslValue[str] | None = None
    lambda_arn: DslValue[str] | None = None


@dataclass
class S3BucketLogDestination(PropertyType):
    log_prefix: DslValue[str] | None = None
    s3_bucket_arn: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class SentimentAnalysisSettings(PropertyType):
    detect_sentiment: DslValue[bool] | None = None


@dataclass
class TextLogDestination(PropertyType):
    cloud_watch: DslValue[CloudWatchLogGroupLogDestination] | None = None


@dataclass
class TextLogSetting(PropertyType):
    destination: DslValue[TextLogDestination] | None = None
    enabled: DslValue[bool] | None = None
