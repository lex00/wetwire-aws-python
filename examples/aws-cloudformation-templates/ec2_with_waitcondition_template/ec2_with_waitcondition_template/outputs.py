"""Template outputs."""

from . import *  # noqa: F403


class WebsiteURLOutput:
    """URL for newly created KWOS deploy stack"""

    resource: Output
    value = Join('', [
    'http://',
    KWOSInstance.PublicDnsName,
])
    description = 'URL for newly created KWOS deploy stack'


class InstanceIdOutput:
    """Instance Id of newly created instance"""

    resource: Output
    value = KWOSInstance
    description = 'Instance Id of newly created instance'
