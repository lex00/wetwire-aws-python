"""Template outputs."""

from . import *  # noqa: F403


class URLOutput(Output):
    """URL of the sample website"""

    value = Join('', [
    'http://',
    ElasticLoadBalancer.DNSName,
])
    description = 'URL of the sample website'
