"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class ClientDomains(Parameter):
    """Array of domains for CORS"""

    type = COMMA_DELIMITED_LIST
    description = 'Array of domains for CORS'
