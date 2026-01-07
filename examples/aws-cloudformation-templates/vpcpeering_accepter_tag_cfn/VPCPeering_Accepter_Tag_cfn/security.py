"""Security resources: TagVpcPeeringConnectionsLambdaRole."""

from . import *  # noqa: F403


class TagVpcPeeringConnectionsLambdaRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0]


class TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1(PolicyStatement):
    sid = 'CreateLogGroup'
    action = 'logs:CreateLogGroup'
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${TagVpcPeeringConnectionsLambdaLogsLogGroup}')


class TagVpcPeeringConnectionsLambdaRoleAllowStatement1(PolicyStatement):
    sid = 'CreateLogStreamAndEvents'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${TagVpcPeeringConnectionsLambdaLogsLogGroup}:log-stream:*')


class TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument(PolicyDocument):
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0_1, TagVpcPeeringConnectionsLambdaRoleAllowStatement1]


class TagVpcPeeringConnectionsLambdaRolePolicy(iam.User.Policy):
    policy_name = 'CloudWatchLogGroup'
    policy_document = TagVpcPeeringConnectionsLambdaRolePolicies0PolicyDocument


class TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2(PolicyStatement):
    sid = 'Tagging'
    action = [
        'ec2:CreateTags',
        'ec2:DeleteTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:ec2:${AWS::Region}:${AWS::AccountId}:vpc-peering-connection/*')


class TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument(PolicyDocument):
    statement = [TagVpcPeeringConnectionsLambdaRoleAllowStatement0_2]


class TagVpcPeeringConnectionsLambdaRolePolicy1(iam.User.Policy):
    policy_name = 'TagVpcPeeringConnections'
    policy_document = TagVpcPeeringConnectionsLambdaRolePolicies1PolicyDocument


class TagVpcPeeringConnectionsLambdaRole(iam.Role):
    resource: iam.Role
    role_name = Sub('${LambdaFunctionName}-LambdaRole')
    description = 'Rights to Tag VPC Peering Connection'
    assume_role_policy_document = TagVpcPeeringConnectionsLambdaRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [TagVpcPeeringConnectionsLambdaRolePolicy, TagVpcPeeringConnectionsLambdaRolePolicy1]
