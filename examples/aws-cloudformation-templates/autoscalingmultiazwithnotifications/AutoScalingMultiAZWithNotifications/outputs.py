"""Template outputs."""

from . import *  # noqa: F403


class URLOutput(Output):
    """The URL of the website"""

    value = Join('', [
    'https://',
    ElasticLoadBalancer.DNSName,
])
    description = 'The URL of the website'
