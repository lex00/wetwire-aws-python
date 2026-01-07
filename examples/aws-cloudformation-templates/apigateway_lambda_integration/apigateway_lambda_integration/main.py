"""Stack resources."""

from . import *  # noqa: F403


class RestApiEndpointConfiguration(apigateway.DomainName.EndpointConfiguration):
    types = [ApiType]


class RestApi(apigateway.RestApi):
    resource: apigateway.RestApi
    description = 'My Rest API'
    name = 'MyApi'
    endpoint_configuration = RestApiEndpointConfiguration


class ApiResource(apigateway.Resource):
    resource: apigateway.Resource
    parent_id = RestApi.RootResourceId
    rest_api_id = RestApi
    path_part = '{city}'


class RequestModel(apigateway.Model):
    resource: apigateway.Model
    content_type = 'application/json'
    name = 'MyModel'
    rest_api_id = RestApi
    schema = {
        '$schema': 'http://json-schema.org/draft-04/schema#',
        'title': 'MyModel',
        'type': 'object',
        'properties': {
            'callerName': {
                'type': 'string',
            },
        },
    }


class ApiMethodMethodResponse(apigateway.Method.MethodResponse):
    status_code = '200'


class ApiMethodIntegrationResponse(apigateway.Method.IntegrationResponse):
    status_code = '200'


class ApiMethodIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS'
    timeout_in_millis = ApigatewayTimeout
    uri = Join('', [
    'arn:',
    AWS_PARTITION,
    ':apigateway:',
    AWS_REGION,
    ':lambda:path/2015-03-31/functions/',
    LambdaFunction.Arn,
    '/invocations',
])
    request_templates = {
        'application/json': """#set($inputRoot = $input.path('$'))
    {
      "city": "$input.params('city')",
      "time": "$input.params('time')",
      "day":  "$input.params('day')",
      "name": "$inputRoot.callerName"
    }
""",
    }
    integration_responses = [ApiMethodIntegrationResponse]


class ApiMethod(apigateway.Method):
    resource: apigateway.Method
    http_method = 'ANY'
    authorization_type = 'NONE'
    request_parameters = {
        'method.request.path.city': 'true',
        'method.request.querystring.time': 'true',
        'method.request.header.day': 'true',
    }
    method_responses = [ApiMethodMethodResponse]
    integration = ApiMethodIntegration
    resource_id = ApiResource
    rest_api_id = RestApi
    request_models = {
        'application/json': RequestModel,
    }
