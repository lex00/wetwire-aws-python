"""Template outputs."""

from . import *  # noqa: F403


class ApiEndpointOutput(Output):
    """HTTP API endpoint URL"""

    value = Sub('https://${MyHttpApi}.execute-api.${AWS::Region}.amazonaws.com')
    description = 'HTTP API endpoint URL'
