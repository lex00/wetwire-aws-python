"""Template outputs."""

from . import *  # noqa: F403


class VPCOutput:
    """A reference to the created VPC"""

    resource: Output
    value = VPC
    description = 'A reference to the created VPC'


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
