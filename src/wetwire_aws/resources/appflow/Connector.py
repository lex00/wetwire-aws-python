"""PropertyTypes for AWS::AppFlow::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectorProvisioningConfig(PropertyType):
    lambda_: LambdaConnectorProvisioningConfig | None = None


@dataclass
class LambdaConnectorProvisioningConfig(PropertyType):
    lambda_arn: str | None = None
