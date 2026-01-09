"""Network resources: GeneratedZone."""

from . import *  # noqa: F403


class GeneratedZone(route53.HostedZone):
    name = DomainName
    condition = 'CreateZone'
