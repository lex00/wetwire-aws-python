"""Template outputs."""

from . import *  # noqa: F403


class apiUrlOutOutput(Output):
    value = Sub('https://${httpApi}.execute-api.${AWS::Region}.amazonaws.com')
