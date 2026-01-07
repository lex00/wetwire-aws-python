"""PropertyTypes for AWS::Logs::Transformer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AddKeyEntry(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
    overwrite_if_exists: DslValue[bool] | None = None


@dataclass
class AddKeys(PropertyType):
    entries: list[DslValue[AddKeyEntry]] = field(default_factory=list)


@dataclass
class CopyValue(PropertyType):
    entries: list[DslValue[CopyValueEntry]] = field(default_factory=list)


@dataclass
class CopyValueEntry(PropertyType):
    source: DslValue[str] | None = None
    target: DslValue[str] | None = None
    overwrite_if_exists: DslValue[bool] | None = None


@dataclass
class Csv(PropertyType):
    columns: list[DslValue[str]] = field(default_factory=list)
    delimiter: DslValue[str] | None = None
    quote_character: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class DateTimeConverter(PropertyType):
    match_patterns: list[DslValue[str]] = field(default_factory=list)
    source: DslValue[str] | None = None
    target: DslValue[str] | None = None
    locale: DslValue[str] | None = None
    source_timezone: DslValue[str] | None = None
    target_format: DslValue[str] | None = None
    target_timezone: DslValue[str] | None = None


@dataclass
class DeleteKeys(PropertyType):
    with_keys: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Grok(PropertyType):
    match: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class ListToMap(PropertyType):
    key: DslValue[str] | None = None
    source: DslValue[str] | None = None
    flatten: DslValue[bool] | None = None
    flattened_element: DslValue[str] | None = None
    target: DslValue[str] | None = None
    value_key: DslValue[str] | None = None


@dataclass
class LowerCaseString(PropertyType):
    with_keys: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MoveKeyEntry(PropertyType):
    source: DslValue[str] | None = None
    target: DslValue[str] | None = None
    overwrite_if_exists: DslValue[bool] | None = None


@dataclass
class MoveKeys(PropertyType):
    entries: list[DslValue[MoveKeyEntry]] = field(default_factory=list)


@dataclass
class ParseCloudfront(PropertyType):
    source: DslValue[str] | None = None


@dataclass
class ParseJSON(PropertyType):
    destination: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class ParseKeyValue(PropertyType):
    destination: DslValue[str] | None = None
    field_delimiter: DslValue[str] | None = None
    key_prefix: DslValue[str] | None = None
    key_value_delimiter: DslValue[str] | None = None
    non_match_value: DslValue[str] | None = None
    overwrite_if_exists: DslValue[bool] | None = None
    source: DslValue[str] | None = None


@dataclass
class ParsePostgres(PropertyType):
    source: DslValue[str] | None = None


@dataclass
class ParseRoute53(PropertyType):
    source: DslValue[str] | None = None


@dataclass
class ParseToOCSF(PropertyType):
    event_source: DslValue[str] | None = None
    ocsf_version: DslValue[str] | None = None
    mapping_version: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class ParseVPC(PropertyType):
    source: DslValue[str] | None = None


@dataclass
class ParseWAF(PropertyType):
    source: DslValue[str] | None = None


@dataclass
class Processor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parse_json": "ParseJSON",
        "parse_to_ocsf": "ParseToOCSF",
        "parse_vpc": "ParseVPC",
        "parse_waf": "ParseWAF",
    }

    add_keys: DslValue[AddKeys] | None = None
    copy_value: DslValue[CopyValue] | None = None
    csv: DslValue[Csv] | None = None
    date_time_converter: DslValue[DateTimeConverter] | None = None
    delete_keys: DslValue[DeleteKeys] | None = None
    grok: DslValue[Grok] | None = None
    list_to_map: DslValue[ListToMap] | None = None
    lower_case_string: DslValue[LowerCaseString] | None = None
    move_keys: DslValue[MoveKeys] | None = None
    parse_cloudfront: DslValue[ParseCloudfront] | None = None
    parse_json: DslValue[ParseJSON] | None = None
    parse_key_value: DslValue[ParseKeyValue] | None = None
    parse_postgres: DslValue[ParsePostgres] | None = None
    parse_route53: DslValue[ParseRoute53] | None = None
    parse_to_ocsf: DslValue[ParseToOCSF] | None = None
    parse_vpc: DslValue[ParseVPC] | None = None
    parse_waf: DslValue[ParseWAF] | None = None
    rename_keys: DslValue[RenameKeys] | None = None
    split_string: DslValue[SplitString] | None = None
    substitute_string: DslValue[SubstituteString] | None = None
    trim_string: DslValue[TrimString] | None = None
    type_converter: DslValue[TypeConverter] | None = None
    upper_case_string: DslValue[UpperCaseString] | None = None


@dataclass
class RenameKeyEntry(PropertyType):
    key: DslValue[str] | None = None
    rename_to: DslValue[str] | None = None
    overwrite_if_exists: DslValue[bool] | None = None


@dataclass
class RenameKeys(PropertyType):
    entries: list[DslValue[RenameKeyEntry]] = field(default_factory=list)


@dataclass
class SplitString(PropertyType):
    entries: list[DslValue[SplitStringEntry]] = field(default_factory=list)


@dataclass
class SplitStringEntry(PropertyType):
    delimiter: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class SubstituteString(PropertyType):
    entries: list[DslValue[SubstituteStringEntry]] = field(default_factory=list)


@dataclass
class SubstituteStringEntry(PropertyType):
    from_: DslValue[str] | None = None
    source: DslValue[str] | None = None
    to: DslValue[str] | None = None


@dataclass
class TrimString(PropertyType):
    with_keys: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TypeConverter(PropertyType):
    entries: list[DslValue[TypeConverterEntry]] = field(default_factory=list)


@dataclass
class TypeConverterEntry(PropertyType):
    key: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class UpperCaseString(PropertyType):
    with_keys: list[DslValue[str]] = field(default_factory=list)
