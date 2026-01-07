"""Security resources: CodeBuildRole."""

from . import *  # noqa: F403


class CodeBuildRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'codebuild.amazonaws.com',
    }
    action = 'sts:AssumeRole'


class CodeBuildRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [CodeBuildRoleAllowStatement0]


class CodeBuildRoleAllowStatement0_1(PolicyStatement):
    action = [
        'logs:CreateLogStream',
        'logs:CreateLogGroup',
        'logs:PutLogEvents',
    ]
    resource_arn = [Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/codebuild/${AWS::StackName}*:log-stream:*')]


class CodeBuildRoleAllowStatement1(PolicyStatement):
    action = [
        's3:GetObject',
        's3:PutObject',
    ]
    resource_arn = [
        PipelineS3Bucket.Arn,
        Sub('${PipelineS3Bucket.Arn}/*'),
    ]


class CodeBuildRolePolicies0PolicyDocument(PolicyDocument):
    statement = [CodeBuildRoleAllowStatement0_1, CodeBuildRoleAllowStatement1]


class CodeBuildRolePolicy(iam.User.Policy):
    policy_name = 'CanLog'
    policy_document = CodeBuildRolePolicies0PolicyDocument


class CodeBuildRoleAllowStatement0_2(PolicyStatement):
    action = ['s3:GetObject']
    resource_arn = [PipelineS3Bucket.Arn]


class CodeBuildRolePolicies1PolicyDocument(PolicyDocument):
    statement = [CodeBuildRoleAllowStatement0_2]


class CodeBuildRolePolicy1(iam.User.Policy):
    policy_name = 'CanAccessS3'
    policy_document = CodeBuildRolePolicies1PolicyDocument


class CodeBuildRoleAllowStatement0_3(PolicyStatement):
    action = ['codebuild:*']
    resource_arn = [Sub('arn:${AWS::Partition}:codebuild:${AWS::Region}:${AWS::AccountId}:report-group/${AWS::StackName}*')]


class CodeBuildRolePolicies2PolicyDocument(PolicyDocument):
    statement = [CodeBuildRoleAllowStatement0_3]


class CodeBuildRolePolicy2(iam.User.Policy):
    policy_name = 'CanCreateReports'
    policy_document = CodeBuildRolePolicies2PolicyDocument


class CodeBuildRole(iam.Role):
    resource: iam.Role
    assume_role_policy_document = CodeBuildRoleAssumeRolePolicyDocument
    policies = [CodeBuildRolePolicy, CodeBuildRolePolicy1, CodeBuildRolePolicy2]
