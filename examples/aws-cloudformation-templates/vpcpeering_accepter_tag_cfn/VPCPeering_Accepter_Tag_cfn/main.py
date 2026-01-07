"""Stack resources."""

from . import *  # noqa: F403


class TagVpcPeeringConnectionsResource(CloudFormationResource):
    # Unknown resource type: Custom::TagVpcPeeringConnection
    resource: CloudFormationResource
    service_token = TagVpcPeeringConnectionsLambdaFunction.Arn
    resource = VPCPeeringConnectionId
    name = PeerName
