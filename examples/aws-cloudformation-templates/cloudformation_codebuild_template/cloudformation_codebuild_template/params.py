"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DockerImage(Parameter):
    """Docker image to use for the build phase"""

    type = STRING
    description = 'Docker image to use for the build phase'
    default = 'aws/codebuild/standard:7.0'
