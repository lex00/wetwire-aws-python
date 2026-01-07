"""Template outputs."""

from . import *  # noqa: F403


class WebsiteURLOutput(Output):
    """URL for newly created KWOS deploy stack"""

    value = Join('', [
    'http://',
    KWOSInstance.PublicDnsName,
])
    description = 'URL for newly created KWOS deploy stack'


class InstanceIdOutput(Output):
    """Instance Id of newly created instance"""

    value = KWOSInstance
    description = 'Instance Id of newly created instance'
