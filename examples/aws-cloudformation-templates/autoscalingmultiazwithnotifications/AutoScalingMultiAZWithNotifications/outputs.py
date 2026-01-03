"""Template outputs."""

from . import *  # noqa: F403


class URLOutput:
    """The URL of the website"""

    resource: Output
    value = Join('', [
    'https://',
    ElasticLoadBalancer.DNSName,
])
    description = 'The URL of the website'
