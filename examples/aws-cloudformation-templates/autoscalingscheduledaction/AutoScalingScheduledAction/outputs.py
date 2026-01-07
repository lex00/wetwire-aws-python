"""Template outputs."""

from . import *  # noqa: F403


class URLOutput(Output):
    """URL of the website"""

    value = Join('', [
    'http://',
    ElasticLoadBalancer.DNSName,
])
    description = 'URL of the website'
