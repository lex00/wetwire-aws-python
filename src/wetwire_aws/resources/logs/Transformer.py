"""PropertyTypes for AWS::Logs::Transformer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AddKeyEntry(PropertyType):
    key: str | None = None
    value: str | None = None
    overwrite_if_exists: bool | None = None


@dataclass
class AddKeys(PropertyType):
    entries: list[AddKeyEntry] = field(default_factory=list)


@dataclass
class CopyValue(PropertyType):
    entries: list[CopyValueEntry] = field(default_factory=list)


@dataclass
class CopyValueEntry(PropertyType):
    source: str | None = None
    target: str | None = None
    overwrite_if_exists: bool | None = None


@dataclass
class Csv(PropertyType):
    columns: list[String] = field(default_factory=list)
    delimiter: str | None = None
    quote_character: str | None = None
    source: str | None = None


@dataclass
class DateTimeConverter(PropertyType):
    match_patterns: list[String] = field(default_factory=list)
    source: str | None = None
    target: str | None = None
    locale: str | None = None
    source_timezone: str | None = None
    target_format: str | None = None
    target_timezone: str | None = None


@dataclass
class DeleteKeys(PropertyType):
    with_keys: list[String] = field(default_factory=list)


@dataclass
class Grok(PropertyType):
    match: str | None = None
    source: str | None = None


@dataclass
class ListToMap(PropertyType):
    key: str | None = None
    source: str | None = None
    flatten: bool | None = None
    flattened_element: str | None = None
    target: str | None = None
    value_key: str | None = None


@dataclass
class LowerCaseString(PropertyType):
    with_keys: list[String] = field(default_factory=list)


@dataclass
class MoveKeyEntry(PropertyType):
    source: str | None = None
    target: str | None = None
    overwrite_if_exists: bool | None = None


@dataclass
class MoveKeys(PropertyType):
    entries: list[MoveKeyEntry] = field(default_factory=list)


@dataclass
class ParseCloudfront(PropertyType):
    source: str | None = None


@dataclass
class ParseJSON(PropertyType):
    destination: str | None = None
    source: str | None = None


@dataclass
class ParseKeyValue(PropertyType):
    destination: str | None = None
    field_delimiter: str | None = None
    key_prefix: str | None = None
    key_value_delimiter: str | None = None
    non_match_value: str | None = None
    overwrite_if_exists: bool | None = None
    source: str | None = None


@dataclass
class ParsePostgres(PropertyType):
    source: str | None = None


@dataclass
class ParseRoute53(PropertyType):
    source: str | None = None


@dataclass
class ParseToOCSF(PropertyType):
    event_source: str | None = None
    ocsf_version: str | None = None
    mapping_version: str | None = None
    source: str | None = None


@dataclass
class ParseVPC(PropertyType):
    source: str | None = None


@dataclass
class ParseWAF(PropertyType):
    source: str | None = None


@dataclass
class Processor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parse_json": "ParseJSON",
        "parse_to_ocsf": "ParseToOCSF",
        "parse_vpc": "ParseVPC",
        "parse_waf": "ParseWAF",
    }

    add_keys: AddKeys | None = None
    copy_value: CopyValue | None = None
    csv: Csv | None = None
    date_time_converter: DateTimeConverter | None = None
    delete_keys: DeleteKeys | None = None
    grok: Grok | None = None
    list_to_map: ListToMap | None = None
    lower_case_string: LowerCaseString | None = None
    move_keys: MoveKeys | None = None
    parse_cloudfront: ParseCloudfront | None = None
    parse_json: ParseJSON | None = None
    parse_key_value: ParseKeyValue | None = None
    parse_postgres: ParsePostgres | None = None
    parse_route53: ParseRoute53 | None = None
    parse_to_ocsf: ParseToOCSF | None = None
    parse_vpc: ParseVPC | None = None
    parse_waf: ParseWAF | None = None
    rename_keys: RenameKeys | None = None
    split_string: SplitString | None = None
    substitute_string: SubstituteString | None = None
    trim_string: TrimString | None = None
    type_converter: TypeConverter | None = None
    upper_case_string: UpperCaseString | None = None


@dataclass
class RenameKeyEntry(PropertyType):
    key: str | None = None
    rename_to: str | None = None
    overwrite_if_exists: bool | None = None


@dataclass
class RenameKeys(PropertyType):
    entries: list[RenameKeyEntry] = field(default_factory=list)


@dataclass
class SplitString(PropertyType):
    entries: list[SplitStringEntry] = field(default_factory=list)


@dataclass
class SplitStringEntry(PropertyType):
    delimiter: str | None = None
    source: str | None = None


@dataclass
class SubstituteString(PropertyType):
    entries: list[SubstituteStringEntry] = field(default_factory=list)


@dataclass
class SubstituteStringEntry(PropertyType):
    from_: str | None = None
    source: str | None = None
    to: str | None = None


@dataclass
class TrimString(PropertyType):
    with_keys: list[String] = field(default_factory=list)


@dataclass
class TypeConverter(PropertyType):
    entries: list[TypeConverterEntry] = field(default_factory=list)


@dataclass
class TypeConverterEntry(PropertyType):
    key: str | None = None
    type_: str | None = None


@dataclass
class UpperCaseString(PropertyType):
    with_keys: list[String] = field(default_factory=list)
