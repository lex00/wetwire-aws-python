"""Template outputs."""

from . import *  # noqa: F403


class LoadBalancerDNSOutput(Output):
    value = LoadBalancer.DNSName
