"""Template outputs."""

from . import *  # noqa: F403


class URLOutput:
    """URL of the website"""

    resource: Output
    value = Join('', [
    'http://',
    ElasticLoadBalancer.DNSName,
])
    description = 'URL of the website'
