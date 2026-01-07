"""Compute resources: JwtResourceHandler, TestResourceHandler, TestResourceRootPermission, JwtResourcePermission, JwtResourceRootPermission, TestResourcePermission."""

from . import *  # noqa: F403


class JwtResourceHandlerContent(lambda_.LayerVersion.Content):
    s3_bucket = 'rain-artifacts-207567786752-us-east-1'
    s3_key = '15d7c92b571beed29cf6c012a96022482eee1df1b477ad528ddc03a4be52c076'


class JwtResourceHandlerEnvironment(lambda_.Function.Environment):
    variables = {
        'COGNITO_REGION': 'us-east-1',
        'COGNITO_POOL_ID': CognitoUserPool,
        'COGNITO_REDIRECT_URI': Sub('https://${SiteDistribution.DomainName}/index.html'),
        'COGNITO_DOMAIN_PREFIX': AppName,
        'COGNITO_APP_CLIENT_ID': CognitoClient,
    }


class JwtResourceHandler(lambda_.Function):
    resource: lambda_.Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-jwt-handler')
    runtime = lambda_.Runtime.PROVIDED_AL2023
    code = JwtResourceHandlerContent
    role = JwtResourceHandlerRole.Arn
    environment = JwtResourceHandlerEnvironment


class TestResourceHandlerContent(lambda_.LayerVersion.Content):
    s3_bucket = LambdaCodeS3Bucket
    s3_key = LambdaCodeS3Key


class TestResourceHandlerEnvironment(lambda_.Function.Environment):
    variables = {
        'TABLE_NAME': TestTable,
    }


class TestResourceHandler(lambda_.Function):
    resource: lambda_.Function
    handler = 'bootstrap'
    function_name = Sub('${AppName}-test-handler')
    runtime = lambda_.Runtime.PROVIDED_AL2023
    code = TestResourceHandlerContent
    role = TestResourceHandlerRole.Arn
    environment = TestResourceHandlerEnvironment


class TestResourceRootPermission(lambda_.Permission):
    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = TestResourceHandler.Arn
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')


class JwtResourcePermission(lambda_.Permission):
    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = JwtResourceHandler.Arn
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')


class JwtResourceRootPermission(lambda_.Permission):
    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = JwtResourceHandler.Arn
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/')


class TestResourcePermission(lambda_.Permission):
    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = TestResourceHandler.Arn
    principal = 'apigateway.amazonaws.com'
    source_arn = Sub('arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*')
