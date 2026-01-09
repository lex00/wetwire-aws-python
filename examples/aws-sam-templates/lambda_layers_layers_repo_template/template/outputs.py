"""Template outputs."""

from . import *  # noqa: F403


class NodeBaseArnOutput(Output):
    """Layer Version ARN for node base"""

    value = NodeBaseLayer
    description = 'Layer Version ARN for node base'


class NodeUtilitiesArnOutput(Output):
    """Layer Version ARN for utilities base"""

    value = NodeUtilitiesLayer
    description = 'Layer Version ARN for utilities base'


class PythonBaseArnOutput(Output):
    """Layer Version ARN for python base"""

    value = PythonBaseLayer
    description = 'Layer Version ARN for python base'
