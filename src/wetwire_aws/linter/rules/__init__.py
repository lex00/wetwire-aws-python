"""Lint rules for wetwire-aws.

This module provides 20 lint rules (WAW001-WAW021, no WAW009) for detecting
anti-patterns in wetwire-aws code and suggesting improvements.

Rules are organized by category:
- parameter_rules: WAW001 (parameter types)
- pseudo_rules: WAW002 (pseudo-parameters)
- enum_rules: WAW003 (enum constants)
- intrinsic_rules: WAW004, WAW005, WAW019, WAW020 (intrinsic functions)
- reference_rules: WAW006 (no-parens references)
- import_rules: WAW007, WAW008, WAW018 (imports)
- file_rules: WAW010, WAW012 (file-level)
- style_rules: WAW011, WAW013-WAW017 (declarative style)
- security_rules: WAW021 (hardcoded secrets)
"""

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule
from wetwire_aws.linter.rules.enum_rules import StringShouldBeEnum
from wetwire_aws.linter.rules.file_rules import DuplicateResource, FileTooLarge
from wetwire_aws.linter.rules.import_rules import (
    ExplicitResourceImport,
    RedundantRelativeImport,
    VerboseInitImports,
)
from wetwire_aws.linter.rules.intrinsic_rules import (
    DictShouldBeIntrinsic,
    ExplicitGetAttIntrinsic,
    ExplicitRefIntrinsic,
    UnnecessaryToDict,
)
from wetwire_aws.linter.rules.parameter_rules import StringShouldBeParameterType
from wetwire_aws.linter.rules.pseudo_rules import RefShouldBePseudoParameter
from wetwire_aws.linter.rules.reference_rules import RefShouldBeNoParens
from wetwire_aws.linter.rules.security_rules import HardcodedSecret
from wetwire_aws.linter.rules.style_rules import (
    InlineConstructor,
    InlinePolicyDocument,
    InlinePolicyStatement,
    InlinePropertyType,
    InlineSecurityGroupRules,
    PropertyTypeAsRef,
)

# All available rules
ALL_RULES: list[type[LintRule]] = [
    StringShouldBeParameterType,  # WAW001
    RefShouldBePseudoParameter,  # WAW002
    StringShouldBeEnum,  # WAW003
    DictShouldBeIntrinsic,  # WAW004
    UnnecessaryToDict,  # WAW005
    RefShouldBeNoParens,  # WAW006
    ExplicitResourceImport,  # WAW007
    VerboseInitImports,  # WAW008
    # WAW009 removed - forward reference issues
    FileTooLarge,  # WAW010
    PropertyTypeAsRef,  # WAW011
    DuplicateResource,  # WAW012
    InlineConstructor,  # WAW013
    InlinePolicyDocument,  # WAW014
    InlineSecurityGroupRules,  # WAW015
    InlinePolicyStatement,  # WAW016
    InlinePropertyType,  # WAW017
    RedundantRelativeImport,  # WAW018
    ExplicitRefIntrinsic,  # WAW019
    ExplicitGetAttIntrinsic,  # WAW020
    HardcodedSecret,  # WAW021
]


def get_all_rules() -> list[LintRule]:
    """Get instances of all available lint rules.

    Returns:
        List of instantiated LintRule objects, one for each rule.
    """
    return [rule_cls() for rule_cls in ALL_RULES]


__all__ = [
    # Base classes
    "LintContext",
    "LintIssue",
    "LintRule",
    # All rule classes
    "StringShouldBeParameterType",
    "RefShouldBePseudoParameter",
    "StringShouldBeEnum",
    "DictShouldBeIntrinsic",
    "UnnecessaryToDict",
    "RefShouldBeNoParens",
    "ExplicitResourceImport",
    "VerboseInitImports",
    "FileTooLarge",
    "PropertyTypeAsRef",
    "DuplicateResource",
    "InlineConstructor",
    "InlinePolicyDocument",
    "InlineSecurityGroupRules",
    "InlinePolicyStatement",
    "InlinePropertyType",
    "RedundantRelativeImport",
    "ExplicitRefIntrinsic",
    "ExplicitGetAttIntrinsic",
    "HardcodedSecret",
    # Aggregates
    "ALL_RULES",
    "get_all_rules",
]
