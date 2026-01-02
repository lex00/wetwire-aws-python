"""PropertyTypes for AWS::MediaConnect::FlowOutput."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DestinationConfiguration(PropertyType):
    destination_ip: str | None = None
    destination_port: int | None = None
    interface: Interface | None = None


@dataclass
class EncodingParameters(PropertyType):
    compression_factor: float | None = None
    encoder_profile: str | None = None


@dataclass
class Encryption(PropertyType):
    role_arn: str | None = None
    secret_arn: str | None = None
    algorithm: str | None = None
    key_type: str | None = None


@dataclass
class FlowTransitEncryption(PropertyType):
    encryption_key_configuration: FlowTransitEncryptionKeyConfiguration | None = None
    encryption_key_type: str | None = None


@dataclass
class FlowTransitEncryptionKeyConfiguration(PropertyType):
    automatic: dict[str, Any] | None = None
    secrets_manager: SecretsManagerEncryptionKeyConfiguration | None = None


@dataclass
class Interface(PropertyType):
    name: str | None = None


@dataclass
class MediaStreamOutputConfiguration(PropertyType):
    encoding_name: str | None = None
    media_stream_name: str | None = None
    destination_configurations: list[DestinationConfiguration] = field(
        default_factory=list
    )
    encoding_parameters: EncodingParameters | None = None


@dataclass
class SecretsManagerEncryptionKeyConfiguration(PropertyType):
    role_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: str | None = None
