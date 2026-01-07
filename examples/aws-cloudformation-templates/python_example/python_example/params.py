"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Tags(Parameter):
    type = COMMA_DELIMITED_LIST
    default = 'Env=Prod,Application=MyApp,BU=ModernisationTeam'
