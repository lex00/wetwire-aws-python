"""Stack resources."""

from . import *  # noqa: F403


class Api(apigateway.RestApi):
    resource: apigateway.RestApi
    name = AppName


class ApiDeployment(apigateway.Deployment):
    resource: apigateway.Deployment
    rest_api_id = Api


class ApiStage(apigateway.Stage):
    resource: apigateway.Stage
    rest_api_id = Api
    deployment_id = ApiDeployment
    stage_name = 'prod'


class ApiAuthorizer(apigateway.Authorizer):
    resource: apigateway.Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [UserPoolArn]
    rest_api_id = Api
    type_ = 'COGNITO_USER_POOLS'
