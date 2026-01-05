"""Network resources: VPCPeeringConnection."""

from . import *  # noqa: F403


class VPCPeeringConnectionAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = PeerName


class VPCPeeringConnection(ec2.VPCPeeringConnection):
    vpc_id = VPCID
    peer_vpc_id = PeerVPCID
    peer_owner_id = PeerOwnerId
    peer_role_arn = If("PeerRoleCondition", PeerRoleARN, AWS_NO_VALUE)
    tags = [VPCPeeringConnectionAssociationParameter]
