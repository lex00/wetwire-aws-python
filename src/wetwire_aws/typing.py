"""
Type aliases for wetwire-aws DSL patterns.

The DSL allows assigning class references, intrinsic functions, and literal values
to resource properties. This module provides type aliases that make these patterns
type-safe.
"""

from typing import TypeVar, Union

from dataclass_dsl import AttrRef

# Import IntrinsicFunction for type hints
from wetwire_aws.intrinsics.functions import IntrinsicFunction

T = TypeVar("T")

# DslValue represents any value that can be assigned to a resource property:
# - Literal values (str, int, bool, etc.)
# - Class references (type[Parameter], type[Resource], type[PropertyType])
# - Intrinsic functions (Sub, Ref, GetAtt, etc.)
# - AttrRef markers (from MyResource.Attribute syntax)
DslValue = Union[T, type, IntrinsicFunction, AttrRef]
