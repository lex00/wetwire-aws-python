"""PropertyTypes for AWS::CloudFront::Function."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FunctionConfig(PropertyType):
    comment: DslValue[str] | None = None
    runtime: DslValue[str] | None = None
    key_value_store_associations: list[DslValue[KeyValueStoreAssociation]] = field(
        default_factory=list
    )


@dataclass
class FunctionMetadata(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "function_arn": "FunctionARN",
    }

    function_arn: DslValue[str] | None = None


@dataclass
class KeyValueStoreAssociation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_value_store_arn": "KeyValueStoreARN",
    }

    key_value_store_arn: DslValue[str] | None = None
