"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class ECRURL(Parameter):
    """URL of the ECR Repository."""

    type = STRING
    description = 'URL of the ECR Repository.'
    default = '123456789012.dkr.ecr.us-east-2.amazonaws.com/cfntest:apache'


class TCPPORT(Parameter):
    """Port on which the container is listening."""

    type = NUMBER
    description = 'Port on which the container is listening.'
    default = 80
