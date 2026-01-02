"""PropertyTypes for AWS::SES::MailManagerTrafficPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IngressAnalysis(PropertyType):
    analyzer: str | None = None
    result_field: str | None = None


@dataclass
class IngressBooleanExpression(PropertyType):
    evaluate: IngressBooleanToEvaluate | None = None
    operator: str | None = None


@dataclass
class IngressBooleanToEvaluate(PropertyType):
    analysis: IngressAnalysis | None = None
    is_in_address_list: IngressIsInAddressList | None = None


@dataclass
class IngressIpToEvaluate(PropertyType):
    attribute: str | None = None


@dataclass
class IngressIpv4Expression(PropertyType):
    evaluate: IngressIpToEvaluate | None = None
    operator: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class IngressIpv6Expression(PropertyType):
    evaluate: IngressIpv6ToEvaluate | None = None
    operator: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class IngressIpv6ToEvaluate(PropertyType):
    attribute: str | None = None


@dataclass
class IngressIsInAddressList(PropertyType):
    address_lists: list[String] = field(default_factory=list)
    attribute: str | None = None


@dataclass
class IngressStringExpression(PropertyType):
    evaluate: IngressStringToEvaluate | None = None
    operator: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class IngressStringToEvaluate(PropertyType):
    analysis: IngressAnalysis | None = None
    attribute: str | None = None


@dataclass
class IngressTlsProtocolExpression(PropertyType):
    evaluate: IngressTlsProtocolToEvaluate | None = None
    operator: str | None = None
    value: str | None = None


@dataclass
class IngressTlsProtocolToEvaluate(PropertyType):
    attribute: str | None = None


@dataclass
class PolicyCondition(PropertyType):
    boolean_expression: IngressBooleanExpression | None = None
    ip_expression: IngressIpv4Expression | None = None
    ipv6_expression: IngressIpv6Expression | None = None
    string_expression: IngressStringExpression | None = None
    tls_expression: IngressTlsProtocolExpression | None = None


@dataclass
class PolicyStatement(PropertyType):
    action: str | None = None
    conditions: list[PolicyCondition] = field(default_factory=list)
