"""PropertyTypes for AWS::RDS::DBSecurityGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Ingress(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cidrip": "CIDRIP",
        "ec2_security_group_id": "EC2SecurityGroupId",
        "ec2_security_group_name": "EC2SecurityGroupName",
        "ec2_security_group_owner_id": "EC2SecurityGroupOwnerId",
    }

    cidrip: DslValue[str] | None = None
    ec2_security_group_id: DslValue[str] | None = None
    ec2_security_group_name: DslValue[str] | None = None
    ec2_security_group_owner_id: DslValue[str] | None = None
