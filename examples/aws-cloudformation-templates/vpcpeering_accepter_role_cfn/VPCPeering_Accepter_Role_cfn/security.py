"""Security resources: PeerRole."""

from . import *  # noqa: F403


class PeerRoleAllowStatement0(PolicyStatement):
    principal = {
        'AWS': Split(',', PeerOwnerIds),
    }
    action = 'sts:AssumeRole'


class PeerRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [PeerRoleAllowStatement0]


class PeerRoleAllowStatement0_1(PolicyStatement):
    action = 'ec2:AcceptVpcPeeringConnection'
    resource_arn = '*'


class PeerRolePolicies0PolicyDocument(PolicyDocument):
    statement = [PeerRoleAllowStatement0_1]


class PeerRolePolicy(iam.User.Policy):
    policy_name = 'AcceptVPCPeering'
    policy_document = PeerRolePolicies0PolicyDocument


class PeerRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = PeerRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [PeerRolePolicy]
