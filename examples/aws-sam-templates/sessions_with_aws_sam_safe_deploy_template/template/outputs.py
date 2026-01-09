"""Template outputs."""

from . import *  # noqa: F403


class WebEndpointOutput(Output):
    """HTTP API endpoint URL"""

    value = Sub('https://${BaseAPI}.execute-api.${AWS::Region}.amazonaws.com')
    description = 'HTTP API endpoint URL'
