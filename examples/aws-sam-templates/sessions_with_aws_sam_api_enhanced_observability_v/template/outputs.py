"""Template outputs."""

from . import *  # noqa: F403


class ApiEndpointOutput(Output):
    """API endpoint URL"""

    value = Sub('https://${MyApi}.execute-api.${AWS::Region}.amazonaws.com/${ApiStage}', {
    'ApiStage': MyApiProdStage  # noqa: WAW019 - SAM implicit resource,
})
    description = 'API endpoint URL'
