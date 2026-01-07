"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class PeerName(Parameter):
    """Name of the VPC Peer"""

    type = STRING
    description = 'Name of the VPC Peer'
    max_length = 255


class PeerOwnerId(Parameter):
    """AWS account ID of the owner of the accepter VPC"""

    type = STRING
    description = 'AWS account ID of the owner of the accepter VPC'
    allowed_pattern = '^\\d{12}$'
    constraint_description = 'Must be 12 digits.'


class PeerRoleARN(Parameter):
    """ARN of the VPC peer role for the peering connection in another AWS account. Required when you are peering a VPC in a different AWS account."""

    type = STRING
    description = 'ARN of the VPC peer role for the peering connection in another AWS account. Required when you are peering a VPC in a different AWS account.'
    allowed_pattern = '^arn:(aws[a-zA-Z-]*)?:iam::\\d{12}:role\\/([\\w+=,.@-]*\\/)*[\\w+=,.@-]+'


class PeerVPCID(Parameter):
    """ID of the VPC with which you are creating the VPC peering connection"""

    type = STRING
    description = 'ID of the VPC with which you are creating the VPC peering connection'
    allowed_pattern = '^vpc-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "vpc-". Followed by 17 characters (numbers, letters "a-f")'


class VPCID(Parameter):
    """ID of the VPC"""

    type = VPC_ID
    description = 'ID of the VPC'


class PeerRoleConditionCondition(TemplateCondition):
    logical_id = 'PeerRoleCondition'
    expression = Not(Equals(PeerRoleARN, ''))
