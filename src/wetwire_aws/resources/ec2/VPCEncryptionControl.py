"""PropertyTypes for AWS::EC2::VPCEncryptionControl."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourceExclusions(PropertyType):
    egress_only_internet_gateway: VpcEncryptionControlExclusion | None = None
    elastic_file_system: VpcEncryptionControlExclusion | None = None
    internet_gateway: VpcEncryptionControlExclusion | None = None
    lambda_: VpcEncryptionControlExclusion | None = None
    nat_gateway: VpcEncryptionControlExclusion | None = None
    virtual_private_gateway: VpcEncryptionControlExclusion | None = None
    vpc_lattice: VpcEncryptionControlExclusion | None = None
    vpc_peering: VpcEncryptionControlExclusion | None = None


@dataclass
class VpcEncryptionControlExclusion(PropertyType):
    state: str | None = None
    state_message: str | None = None
