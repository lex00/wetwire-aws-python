"""Template outputs."""

from . import *  # noqa: F403


class URLOutput(Output):
    value = Sub('https://${CloudFrontDistribution.DomainName}/?folder=/home/ec2-user')
