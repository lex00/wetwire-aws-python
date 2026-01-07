"""PropertyTypes for AWS::RTBFabric::ResponderGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoScalingGroupsConfiguration(PropertyType):
    auto_scaling_group_name_list: list[DslValue[str]] = field(default_factory=list)
    role_arn: DslValue[str] | None = None


@dataclass
class EksEndpointsConfiguration(PropertyType):
    cluster_api_server_ca_certificate_chain: DslValue[str] | None = None
    cluster_api_server_endpoint_uri: DslValue[str] | None = None
    cluster_name: DslValue[str] | None = None
    endpoints_resource_name: DslValue[str] | None = None
    endpoints_resource_namespace: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class ManagedEndpointConfiguration(PropertyType):
    auto_scaling_groups_configuration: (
        DslValue[AutoScalingGroupsConfiguration] | None
    ) = None
    eks_endpoints_configuration: DslValue[EksEndpointsConfiguration] | None = None


@dataclass
class TrustStoreConfiguration(PropertyType):
    certificate_authority_certificates: list[DslValue[str]] = field(
        default_factory=list
    )
