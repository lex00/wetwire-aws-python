"""Template outputs."""

from . import *  # noqa: F403


class WebEndpointOutput(Output):
    """API Gateway endpoint URL for Prod stage"""

    value = Sub('https://${ServerlessRestApi}.execute-api.${AWS::Region}.${AWS::URLSuffix}/Prod/')
    description = 'API Gateway endpoint URL for Prod stage'
