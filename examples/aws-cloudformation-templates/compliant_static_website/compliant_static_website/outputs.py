"""Template outputs."""

from . import *  # noqa: F403


class SiteURLOutput:
    resource: Output
    value = Sub('https://${Distribution.DomainName}')
