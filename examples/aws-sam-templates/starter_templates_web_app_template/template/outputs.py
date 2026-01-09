"""Template outputs."""

from . import *  # noqa: F403


class WebEndpointOutput(Output):
    """API Gateway endpoint URL for Prod stage"""

    value = Sub('https://${ServerlessHttpApi}.execute-api.${AWS::Region}.amazonaws.com')
    description = 'API Gateway endpoint URL for Prod stage'
