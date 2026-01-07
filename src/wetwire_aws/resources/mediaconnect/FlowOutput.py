"""PropertyTypes for AWS::MediaConnect::FlowOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DestinationConfiguration(PropertyType):
    destination_ip: DslValue[str] | None = None
    destination_port: DslValue[int] | None = None
    interface: DslValue[Interface] | None = None


@dataclass
class EncodingParameters(PropertyType):
    compression_factor: DslValue[float] | None = None
    encoder_profile: DslValue[str] | None = None


@dataclass
class Encryption(PropertyType):
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None
    algorithm: DslValue[str] | None = None
    key_type: DslValue[str] | None = None


@dataclass
class FlowTransitEncryption(PropertyType):
    encryption_key_configuration: (
        DslValue[FlowTransitEncryptionKeyConfiguration] | None
    ) = None
    encryption_key_type: DslValue[str] | None = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    automatic: DslValue[dict[str, Any]] | None = None
    secrets_manager: DslValue[SecretsManagerEncryptionKeyConfiguration] | None = None


@dataclass
class Interface(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class MediaStreamOutputConfiguration(PropertyType):
    encoding_name: DslValue[str] | None = None
    media_stream_name: DslValue[str] | None = None
    destination_configurations: list[DslValue[DestinationConfiguration]] = field(
        default_factory=list
    )
    encoding_parameters: DslValue[EncodingParameters] | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: DslValue[str] | None = None
