"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Tags:
    resource: Parameter
    type = COMMA_DELIMITED_LIST
    default = 'Env=Prod,Application=MyApp,BU=ModernisationTeam'
