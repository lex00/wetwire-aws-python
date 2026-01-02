"""PropertyTypes for AWS::Lex::BotAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AudioLogDestination(PropertyType):
    s3_bucket: S3BucketLogDestination | None = None


@dataclass
class AudioLogSetting(PropertyType):
    destination: AudioLogDestination | None = None
    enabled: bool | None = None


@dataclass
class BotAliasLocaleSettings(PropertyType):
    enabled: bool | None = None
    code_hook_specification: CodeHookSpecification | None = None


@dataclass
class BotAliasLocaleSettingsItem(PropertyType):
    bot_alias_locale_setting: BotAliasLocaleSettings | None = None
    locale_id: str | None = None


@dataclass
class CloudWatchLogGroupLogDestination(PropertyType):
    cloud_watch_log_group_arn: str | None = None
    log_prefix: str | None = None


@dataclass
class CodeHookSpecification(PropertyType):
    lambda_code_hook: LambdaCodeHook | None = None


@dataclass
class ConversationLogSettings(PropertyType):
    audio_log_settings: list[AudioLogSetting] = field(default_factory=list)
    text_log_settings: list[TextLogSetting] = field(default_factory=list)


@dataclass
class LambdaCodeHook(PropertyType):
    code_hook_interface_version: str | None = None
    lambda_arn: str | None = None


@dataclass
class S3BucketLogDestination(PropertyType):
    log_prefix: str | None = None
    s3_bucket_arn: str | None = None
    kms_key_arn: str | None = None


@dataclass
class SentimentAnalysisSettings(PropertyType):
    detect_sentiment: bool | None = None


@dataclass
class TextLogDestination(PropertyType):
    cloud_watch: CloudWatchLogGroupLogDestination | None = None


@dataclass
class TextLogSetting(PropertyType):
    destination: TextLogDestination | None = None
    enabled: bool | None = None
