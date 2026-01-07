"""Template outputs."""

from . import *  # noqa: F403


class VPCOutput(Output):
    """A reference to the created VPC"""

    value = VPC
    description = 'A reference to the created VPC'


class PublicSubnetsOutput(Output):
    """A list of the public subnets"""

    value = Join(',', [
    PublicSubnet1,
    PublicSubnet2,
])
    description = 'A list of the public subnets'


class PrivateSubnetsOutput(Output):
    """A list of the private subnets"""

    value = Join(',', [
    PrivateSubnet1,
    PrivateSubnet2,
])
    description = 'A list of the private subnets'


class CfnEndpointOutput(Output):
    """A reference to the CloudFormation Endpoint used for signaling from the private instance"""

    value = CfnEndpoint
    description = 'A reference to the CloudFormation Endpoint used for signaling from the private instance'
