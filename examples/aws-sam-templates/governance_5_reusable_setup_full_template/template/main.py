"""Stack resources."""

from . import *  # noqa: F403


class ManagedRules(serverless.Application):
    location = '../2-managed-rules/template.yaml'
    depends_on = [ConfigRecorder]


class CustomRules(serverless.Application):
    location = '../3-custom-rules/template.yaml'
    depends_on = [ConfigRecorder]
