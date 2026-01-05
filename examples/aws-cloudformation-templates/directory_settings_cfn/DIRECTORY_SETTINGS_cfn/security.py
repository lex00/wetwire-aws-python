"""Security resources: DirectoryConsoleDelegatedAccessSecurityAuditRole, DirectorySettingsLambdaRole, DirectoryConsoleDelegatedAccessEC2ReadOnlyRole."""

from . import *  # noqa: F403


class DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ds.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectoryConsoleDelegatedAccessSecurityAuditRoleAllowStatement0]


class DirectoryConsoleDelegatedAccessSecurityAuditRole(iam.Role):
    description = 'IAM Role for Directory Service \'AWS Management Console\' Delegated Access for "Security Audit"'
    assume_role_policy_document = DirectoryConsoleDelegatedAccessSecurityAuditRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/SecurityAudit')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    condition = 'DirectoryConsoleDelegatedAccessRolesCondition'


class DirectorySettingsLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class DirectorySettingsLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectorySettingsLambdaRoleAllowStatement0]


class DirectorySettingsLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'CreateLogGroup'
    action = 'logs:CreateLogGroup'
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${DirectorySettingsLambdaLogsLogGroup}')


class DirectorySettingsLambdaRoleAllowStatement1:
    resource: PolicyStatement
    sid = 'CreateLogStreamAndEvents'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${DirectorySettingsLambdaLogsLogGroup}:log-stream:*')


class DirectorySettingsLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [DirectorySettingsLambdaRoleAllowStatement0_1, DirectorySettingsLambdaRoleAllowStatement1]


class DirectorySettingsLambdaRolePolicy:
    resource: iam.User.Policy
    policy_name = 'CloudWatchLogGroup'
    policy_document = DirectorySettingsLambdaRolePolicies0PolicyDocument


class DirectorySettingsLambdaRoleAllowStatement0_2:
    resource: PolicyStatement
    sid = 'SnsTopic'
    action = [
        'ds:RegisterEventTopic',
        'ds:DeregisterEventTopic',
        'ds:DescribeEventTopics',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:ds:${AWS::Region}:${AWS::AccountId}:directory/${DirectoryID}')


class DirectorySettingsLambdaRoleAllowStatement1_1:
    resource: PolicyStatement
    sid = 'DescribeDirectories'
    action = 'ds:DescribeDirectories'
    resource_arn = '*'


class DirectorySettingsLambdaRoleAllowStatement2:
    resource: PolicyStatement
    sid = 'AliasSso'
    action = [
        'ds:CreateAlias',
        'ds:EnableSso',
        'ds:DisableSso',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:ds:${AWS::Region}:${AWS::AccountId}:directory/${DirectoryID}')


class DirectorySettingsLambdaRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [DirectorySettingsLambdaRoleAllowStatement0_2, DirectorySettingsLambdaRoleAllowStatement1_1, DirectorySettingsLambdaRoleAllowStatement2]


class DirectorySettingsLambdaRolePolicy1:
    resource: iam.User.Policy
    policy_name = 'DirectorySettings'
    policy_document = DirectorySettingsLambdaRolePolicies1PolicyDocument


class DirectorySettingsLambdaRole(iam.Role):
    role_name = Sub('${LambdaFunctionName}-LambdaRole')
    description = Sub('Rights to Setup Directory Settings for Directory ID, ${DirectoryID}')
    assume_role_policy_document = DirectorySettingsLambdaRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [DirectorySettingsLambdaRolePolicy, DirectorySettingsLambdaRolePolicy1]


class DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ds.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAllowStatement0]


class DirectoryConsoleDelegatedAccessEC2ReadOnlyRole(iam.Role):
    description = 'IAM Role for Directory Service \'AWS Management Console\' Delegated Access for "EC2 ReadOnly"'
    assume_role_policy_document = DirectoryConsoleDelegatedAccessEC2ReadOnlyRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonEC2ReadOnlyAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    condition = 'DirectoryConsoleDelegatedAccessRolesCondition'
