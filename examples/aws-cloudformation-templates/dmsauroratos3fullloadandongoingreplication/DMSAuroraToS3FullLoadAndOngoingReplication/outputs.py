"""Template outputs."""

from . import *  # noqa: F403


class StackNameOutput(Output):
    value = AWS_STACK_NAME


class RegionNameOutput(Output):
    value = AWS_REGION


class S3BucketNameOutput(Output):
    value = S3Bucket


class AuroraEndpointOutput(Output):
    value = AuroraCluster.Endpoint.Address
