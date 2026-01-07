"""PropertyTypes for AWS::SES::MailManagerTrafficPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IngressAnalysis(PropertyType):
    analyzer: DslValue[str] | None = None
    result_field: DslValue[str] | None = None


@dataclass
class IngressBooleanExpression(PropertyType):
    evaluate: DslValue[IngressBooleanToEvaluate] | None = None
    operator: DslValue[str] | None = None


@dataclass
class IngressBooleanToEvaluate(PropertyType):
    analysis: DslValue[IngressAnalysis] | None = None
    is_in_address_list: DslValue[IngressIsInAddressList] | None = None


@dataclass
class IngressIpToEvaluate(PropertyType):
    attribute: DslValue[str] | None = None


@dataclass
class IngressIpv4Expression(PropertyType):
    evaluate: DslValue[IngressIpToEvaluate] | None = None
    operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IngressIpv6Expression(PropertyType):
    evaluate: DslValue[IngressIpv6ToEvaluate] | None = None
    operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IngressIpv6ToEvaluate(PropertyType):
    attribute: DslValue[str] | None = None


@dataclass
class IngressIsInAddressList(PropertyType):
    address_lists: list[DslValue[str]] = field(default_factory=list)
    attribute: DslValue[str] | None = None


@dataclass
class IngressStringExpression(PropertyType):
    evaluate: DslValue[IngressStringToEvaluate] | None = None
    operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IngressStringToEvaluate(PropertyType):
    analysis: DslValue[IngressAnalysis] | None = None
    attribute: DslValue[str] | None = None


@dataclass
class IngressTlsProtocolExpression(PropertyType):
    evaluate: DslValue[IngressTlsProtocolToEvaluate] | None = None
    operator: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class IngressTlsProtocolToEvaluate(PropertyType):
    attribute: DslValue[str] | None = None


@dataclass
class PolicyCondition(PropertyType):
    boolean_expression: DslValue[IngressBooleanExpression] | None = None
    ip_expression: DslValue[IngressIpv4Expression] | None = None
    ipv6_expression: DslValue[IngressIpv6Expression] | None = None
    string_expression: DslValue[IngressStringExpression] | None = None
    tls_expression: DslValue[IngressTlsProtocolExpression] | None = None


@dataclass
class PolicyStatement(PropertyType):
    action: DslValue[str] | None = None
    conditions: list[DslValue[PolicyCondition]] = field(default_factory=list)
