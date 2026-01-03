"""Template outputs."""

from . import *  # noqa: F403


class LoadBalancerDNSOutput:
    resource: Output
    value = LoadBalancer.DNSName
