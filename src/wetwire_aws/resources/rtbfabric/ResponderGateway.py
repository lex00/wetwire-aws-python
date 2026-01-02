"""PropertyTypes for AWS::RTBFabric::ResponderGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoScalingGroupsConfiguration(PropertyType):
    auto_scaling_group_name_list: list[String] = field(default_factory=list)
    role_arn: str | None = None


@dataclass
class EksEndpointsConfiguration(PropertyType):
    cluster_api_server_ca_certificate_chain: str | None = None
    cluster_api_server_endpoint_uri: str | None = None
    cluster_name: str | None = None
    endpoints_resource_name: str | None = None
    endpoints_resource_namespace: str | None = None
    role_arn: str | None = None


@dataclass
class ManagedEndpointConfiguration(PropertyType):
    auto_scaling_groups_configuration: AutoScalingGroupsConfiguration | None = None
    eks_endpoints_configuration: EksEndpointsConfiguration | None = None


@dataclass
class TrustStoreConfiguration(PropertyType):
    certificate_authority_certificates: list[String] = field(default_factory=list)
