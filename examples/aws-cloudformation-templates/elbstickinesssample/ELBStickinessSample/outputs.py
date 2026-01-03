"""Template outputs."""

from . import *  # noqa: F403


class URLOutput:
    """URL of the sample website"""

    resource: Output
    value = Join('', [
    'http://',
    ElasticLoadBalancer.DNSName,
])
    description = 'URL of the sample website'
