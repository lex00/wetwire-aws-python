"""Template outputs."""

from . import *  # noqa: F403


class AppRunnerOutput(Output):
    """URL of the deployed App Runner Service"""

    value = Join('', [
    'https://',
    AppRunner.ServiceUrl,
])
    description = 'URL of the deployed App Runner Service'
