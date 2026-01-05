"""Stack resources."""

from . import *  # noqa: F403


class Api:
    resource: apigateway.RestApi
    name = AppName


class ApiDeployment:
    resource: apigateway.Deployment
    rest_api_id = Api


class ApiStage:
    resource: apigateway.Stage
    rest_api_id = Api
    deployment_id = ApiDeployment
    stage_name = 'prod'


class ApiAuthorizer:
    resource: apigateway.Authorizer
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [UserPoolArn]
    rest_api_id = Api
    type_ = 'COGNITO_USER_POOLS'
