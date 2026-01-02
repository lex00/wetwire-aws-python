"""PropertyTypes for AWS::DataZone::PolicyGrant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AddToProjectMemberPoolPolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class CreateAssetTypePolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class CreateDomainUnitPolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class CreateEnvironmentProfilePolicyGrantDetail(PropertyType):
    domain_unit_id: str | None = None


@dataclass
class CreateFormTypePolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class CreateGlossaryPolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class CreateProjectFromProjectProfilePolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None
    project_profiles: list[String] = field(default_factory=list)


@dataclass
class CreateProjectPolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class DomainUnitFilterForProject(PropertyType):
    domain_unit: str | None = None
    include_child_domain_units: bool | None = None


@dataclass
class DomainUnitGrantFilter(PropertyType):
    all_domain_units_grant_filter: dict[str, Any] | None = None


@dataclass
class DomainUnitPolicyGrantPrincipal(PropertyType):
    domain_unit_designation: str | None = None
    domain_unit_grant_filter: DomainUnitGrantFilter | None = None
    domain_unit_identifier: str | None = None


@dataclass
class GroupPolicyGrantPrincipal(PropertyType):
    group_identifier: str | None = None


@dataclass
class OverrideDomainUnitOwnersPolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class OverrideProjectOwnersPolicyGrantDetail(PropertyType):
    include_child_domain_units: bool | None = None


@dataclass
class PolicyGrantDetail(PropertyType):
    add_to_project_member_pool: AddToProjectMemberPoolPolicyGrantDetail | None = None
    create_asset_type: CreateAssetTypePolicyGrantDetail | None = None
    create_domain_unit: CreateDomainUnitPolicyGrantDetail | None = None
    create_environment: dict[str, Any] | None = None
    create_environment_from_blueprint: dict[str, Any] | None = None
    create_environment_profile: CreateEnvironmentProfilePolicyGrantDetail | None = None
    create_form_type: CreateFormTypePolicyGrantDetail | None = None
    create_glossary: CreateGlossaryPolicyGrantDetail | None = None
    create_project: CreateProjectPolicyGrantDetail | None = None
    create_project_from_project_profile: (
        CreateProjectFromProjectProfilePolicyGrantDetail | None
    ) = None
    delegate_create_environment_profile: dict[str, Any] | None = None
    override_domain_unit_owners: OverrideDomainUnitOwnersPolicyGrantDetail | None = None
    override_project_owners: OverrideProjectOwnersPolicyGrantDetail | None = None


@dataclass
class PolicyGrantPrincipal(PropertyType):
    domain_unit: DomainUnitPolicyGrantPrincipal | None = None
    group: GroupPolicyGrantPrincipal | None = None
    project: ProjectPolicyGrantPrincipal | None = None
    user: UserPolicyGrantPrincipal | None = None


@dataclass
class ProjectGrantFilter(PropertyType):
    domain_unit_filter: DomainUnitFilterForProject | None = None


@dataclass
class ProjectPolicyGrantPrincipal(PropertyType):
    project_designation: str | None = None
    project_grant_filter: ProjectGrantFilter | None = None
    project_identifier: str | None = None


@dataclass
class UserPolicyGrantPrincipal(PropertyType):
    all_users_grant_filter: dict[str, Any] | None = None
    user_identifier: str | None = None
