"""Template outputs."""

from . import *  # noqa: F403


class ApiEndpointOutput(Output):
    """API endpoint URL"""

    value = Sub('https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod')
    description = 'API endpoint URL'
