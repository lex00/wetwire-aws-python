"""Template outputs."""

from . import *  # noqa: F403


class AppRunnerOutput:
    """URL of the deployed App Runner Service"""

    resource: Output
    value = Join('', [
    'https://',
    AppRunner.ServiceUrl,
])
    description = 'URL of the deployed App Runner Service'
