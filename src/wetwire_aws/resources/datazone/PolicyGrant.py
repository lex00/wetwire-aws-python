"""PropertyTypes for AWS::DataZone::PolicyGrant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AddToProjectMemberPoolPolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class CreateAssetTypePolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class CreateDomainUnitPolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class CreateEnvironmentProfilePolicyGrantDetail(PropertyType):
    domain_unit_id: DslValue[str] | None = None


@dataclass
class CreateFormTypePolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class CreateGlossaryPolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class CreateProjectFromProjectProfilePolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None
    project_profiles: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CreateProjectPolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class DomainUnitFilterForProject(PropertyType):
    domain_unit: DslValue[str] | None = None
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class DomainUnitGrantFilter(PropertyType):
    all_domain_units_grant_filter: DslValue[dict[str, Any]] | None = None


@dataclass
class DomainUnitPolicyGrantPrincipal(PropertyType):
    domain_unit_designation: DslValue[str] | None = None
    domain_unit_grant_filter: DslValue[DomainUnitGrantFilter] | None = None
    domain_unit_identifier: DslValue[str] | None = None


@dataclass
class GroupPolicyGrantPrincipal(PropertyType):
    group_identifier: DslValue[str] | None = None


@dataclass
class OverrideDomainUnitOwnersPolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class OverrideProjectOwnersPolicyGrantDetail(PropertyType):
    include_child_domain_units: DslValue[bool] | None = None


@dataclass
class PolicyGrantDetail(PropertyType):
    add_to_project_member_pool: (
        DslValue[AddToProjectMemberPoolPolicyGrantDetail] | None
    ) = None
    create_asset_type: DslValue[CreateAssetTypePolicyGrantDetail] | None = None
    create_domain_unit: DslValue[CreateDomainUnitPolicyGrantDetail] | None = None
    create_environment: DslValue[dict[str, Any]] | None = None
    create_environment_from_blueprint: DslValue[dict[str, Any]] | None = None
    create_environment_profile: (
        DslValue[CreateEnvironmentProfilePolicyGrantDetail] | None
    ) = None
    create_form_type: DslValue[CreateFormTypePolicyGrantDetail] | None = None
    create_glossary: DslValue[CreateGlossaryPolicyGrantDetail] | None = None
    create_project: DslValue[CreateProjectPolicyGrantDetail] | None = None
    create_project_from_project_profile: (
        DslValue[CreateProjectFromProjectProfilePolicyGrantDetail] | None
    ) = None
    delegate_create_environment_profile: DslValue[dict[str, Any]] | None = None
    override_domain_unit_owners: (
        DslValue[OverrideDomainUnitOwnersPolicyGrantDetail] | None
    ) = None
    override_project_owners: DslValue[OverrideProjectOwnersPolicyGrantDetail] | None = (
        None
    )


@dataclass
class PolicyGrantPrincipal(PropertyType):
    domain_unit: DslValue[DomainUnitPolicyGrantPrincipal] | None = None
    group: DslValue[GroupPolicyGrantPrincipal] | None = None
    project: DslValue[ProjectPolicyGrantPrincipal] | None = None
    user: DslValue[UserPolicyGrantPrincipal] | None = None


@dataclass
class ProjectGrantFilter(PropertyType):
    domain_unit_filter: DslValue[DomainUnitFilterForProject] | None = None


@dataclass
class ProjectPolicyGrantPrincipal(PropertyType):
    project_designation: DslValue[str] | None = None
    project_grant_filter: DslValue[ProjectGrantFilter] | None = None
    project_identifier: DslValue[str] | None = None


@dataclass
class UserPolicyGrantPrincipal(PropertyType):
    all_users_grant_filter: DslValue[dict[str, Any]] | None = None
    user_identifier: DslValue[str] | None = None
