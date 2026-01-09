"""Security resources: LoggingRole, UserPool, UserPoolDomain, DDBReadRole, UserPoolClient, DDBCrudRole."""

from . import *  # noqa: F403


class LoggingRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'cloudfront.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class LoggingRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [LoggingRoleAllowStatement0]


class LoggingRolePolicy(iam.User.Policy):
    policy_name = 'CloudFrontLogToKinesis'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': [
                'kinesis:Put*',
                'kinesis:List*',
            ],
            'Effect': 'Allow',
            'Resource': LoggingStream.Arn,
        },
    }


class LoggingRole(iam.Role):
    assume_role_policy_document = LoggingRoleAssumeRolePolicyDocument
    policies = [LoggingRolePolicy]


class UserPoolPasswordPolicy(cognito.UserPool.PasswordPolicy):
    minimum_length = 8


class UserPoolPolicies(cognito.UserPool.Policies):
    password_policy = UserPoolPasswordPolicy


class UserPoolSchemaAttribute(cognito.UserPool.SchemaAttribute):
    attribute_data_type = 'String'
    name = 'email'
    required = False


class UserPool(cognito.UserPool):
    user_pool_name = Sub('${AppName}-UserPool')
    policies = UserPoolPolicies
    auto_verified_attributes = ['email']
    username_attributes = ['email']
    schema = [UserPoolSchemaAttribute]


class UserPoolDomain(cognito.UserPoolDomain):
    domain = Sub('${AppName}-${AWS::AccountId}')
    user_pool_id = UserPool


class DDBReadRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'apigateway.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class DDBReadRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [DDBReadRoleAllowStatement0]


class DDBReadRolePolicy(iam.User.Policy):
    policy_name = 'DDBReadPolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': [
                'dynamodb:GetItem',
                'dynamodb:Scan',
                'dynamodb:Query',
            ],
            'Effect': 'Allow',
            'Resource': [
                LinkTable.Arn,
                Sub('${TableArn}/index/*', {
    'TableArn': LinkTable.Arn,
}),
            ],
        },
    }


class DDBReadRole(iam.Role):
    assume_role_policy_document = DDBReadRoleAssumeRolePolicyDocument
    policies = [DDBReadRolePolicy]


class UserPoolClient(cognito.UserPoolClient):
    user_pool_id = UserPool
    client_name = Sub('${AppName}-UserPoolClient')
    generate_secret = False
    supported_identity_providers = ['COGNITO']
    callback_ur_ls = [Sub('https://${CustomDomain}'), If("IsLocal", 'http://localhost:8080', AWS_NO_VALUE)]
    logout_ur_ls = [Sub('https://${CustomDomain}'), If("IsLocal", 'http://localhost:8080', AWS_NO_VALUE)]
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_flows = ['code']
    allowed_o_auth_scopes = ['email', 'openid']


class DDBCrudRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'apigateway.amazonaws.com',
    }
    action = ['sts:AssumeRole']


class DDBCrudRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [DDBCrudRoleAllowStatement0]


class DDBCrudRolePolicy(iam.User.Policy):
    policy_name = 'DDBCrudPolicy'
    policy_document = {
        'Version': '2012-10-17',
        'Statement': {
            'Action': [
                'dynamodb:DeleteItem',
                'dynamodb:UpdateItem',
            ],
            'Effect': 'Allow',
            'Resource': LinkTable.Arn,
        },
    }


class DDBCrudRole(iam.Role):
    assume_role_policy_document = DDBCrudRoleAssumeRolePolicyDocument
    policies = [DDBCrudRolePolicy]
