"""Security resources: EKSClusterRole, NodeInstanceRole."""

from . import *  # noqa: F403


class EKSClusterRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': FindInMap("ServicePrincipalPartitionMap", AWS_PARTITION, 'EKS'),
    }
    action = ['sts:AssumeRole']


class EKSClusterRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EKSClusterRoleAllowStatement0]


class EKSClusterRole:
    resource: iam.Role
    assume_role_policy_document = EKSClusterRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSClusterPolicy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSVPCResourceController')]


class NodeInstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': FindInMap("ServicePrincipalPartitionMap", AWS_PARTITION, 'EC2'),
    }
    action = ['sts:AssumeRole']


class NodeInstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [NodeInstanceRoleAllowStatement0]


class NodeInstanceRole:
    resource: iam.Role
    role_name = Sub('${AWS::StackName}-eks-node-role')
    assume_role_policy_document = NodeInstanceRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKSWorkerNodePolicy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEKS_CNI_Policy'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore')]
    path = '/'
