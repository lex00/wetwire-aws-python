"""Template outputs."""

from . import *  # noqa: F403


class VPCOutput:
    """A reference to the created VPC"""

    resource: Output
    value = VPC
    description = 'A reference to the created VPC'


class PublicSubnetsOutput:
    """A list of the public subnets"""

    resource: Output
    value = Join(',', [
    PublicSubnet1,
    PublicSubnet2,
])
    description = 'A list of the public subnets'


class PrivateSubnetsOutput:
    """A list of the private subnets"""

    resource: Output
    value = Join(',', [
    PrivateSubnet1,
    PrivateSubnet2,
])
    description = 'A list of the private subnets'


class CfnEndpointOutput:
    """A reference to the CloudFormation Endpoint used for signaling from the private instance"""

    resource: Output
    value = CfnEndpoint
    description = 'A reference to the CloudFormation Endpoint used for signaling from the private instance'
