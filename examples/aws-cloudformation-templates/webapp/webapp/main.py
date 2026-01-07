"""Stack resources."""

from . import *  # noqa: F403


class RestApi(apigateway.RestApi):
    resource: apigateway.RestApi
    name = AppName


class RestApiAuthorizer(apigateway.Authorizer):
    resource: apigateway.Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [CognitoUserPool.Arn]
    rest_api_id = RestApi
    type_ = 'COGNITO_USER_POOLS'


class TestResourceResource(apigateway.Resource):
    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'test'
    rest_api_id = RestApi


class TestResourceGetIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


class TestResourceGet(apigateway.Method):
    resource: apigateway.Method
    http_method = 'GET'
    resource_id = TestResourceResource
    rest_api_id = RestApi
    authorization_type = 'COGNITO_USER_POOLS'
    authorizer_id = RestApiAuthorizer
    integration = TestResourceGetIntegration


class JwtResourceResource(apigateway.Resource):
    resource: apigateway.Resource
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'jwt'
    rest_api_id = RestApi


class JwtResourceGetIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


class JwtResourceGet(apigateway.Method):
    resource: apigateway.Method
    http_method = 'GET'
    resource_id = JwtResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    authorizer_id = 'AWS::NoValue'
    integration = JwtResourceGetIntegration


class TestResourceOptionsIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


class TestResourceOptions(apigateway.Method):
    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = TestResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    integration = TestResourceOptionsIntegration


class JwtResourceOptionsIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


class JwtResourceOptions(apigateway.Method):
    resource: apigateway.Method
    http_method = 'OPTIONS'
    resource_id = JwtResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    integration = JwtResourceOptionsIntegration


class RestApiDeployment(apigateway.Deployment):
    resource: apigateway.Deployment
    rest_api_id = RestApi
    depends_on = [TestResourceGet, TestResourceOptions, JwtResourceGet, JwtResourceOptions]


class RestApiStage(apigateway.Stage):
    resource: apigateway.Stage
    rest_api_id = RestApi
    deployment_id = RestApiDeployment
    stage_name = 'prod'
