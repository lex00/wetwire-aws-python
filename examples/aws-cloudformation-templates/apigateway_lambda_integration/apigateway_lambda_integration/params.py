"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class ApiType(Parameter):
    """The Endpoint type for RESTApi"""

    type = STRING
    description = 'The Endpoint type for RESTApi'
    default = 'REGIONAL'
    allowed_values = [
    'EDGE',
    'REGIONAL',
    'PRIVATE',
]


class ApigatewayTimeout(Parameter):
    """ApiGateway Backend Integration timeout in milliseconds"""

    type = NUMBER
    description = 'ApiGateway Backend Integration timeout in milliseconds'
    default = '29000'
    min_value = 50
    max_value = 29000


class LambdaFunctionName(Parameter):
    """The Name for the Lambda Function"""

    type = STRING
    description = 'The Name for the Lambda Function'
    default = 'My-APIGW-Integ-Function'
