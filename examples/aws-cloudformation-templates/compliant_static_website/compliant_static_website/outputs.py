"""Template outputs."""

from . import *  # noqa: F403


class SiteURLOutput(Output):
    value = Sub('https://${Distribution.DomainName}')
