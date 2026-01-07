"""PropertyTypes for AWS::EC2::VPCEncryptionControl."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ResourceExclusions(PropertyType):
    egress_only_internet_gateway: DslValue[VpcEncryptionControlExclusion] | None = None
    elastic_file_system: DslValue[VpcEncryptionControlExclusion] | None = None
    internet_gateway: DslValue[VpcEncryptionControlExclusion] | None = None
    lambda_: DslValue[VpcEncryptionControlExclusion] | None = None
    nat_gateway: DslValue[VpcEncryptionControlExclusion] | None = None
    virtual_private_gateway: DslValue[VpcEncryptionControlExclusion] | None = None
    vpc_lattice: DslValue[VpcEncryptionControlExclusion] | None = None
    vpc_peering: DslValue[VpcEncryptionControlExclusion] | None = None


@dataclass
class VpcEncryptionControlExclusion(PropertyType):
    state: DslValue[str] | None = None
    state_message: DslValue[str] | None = None
