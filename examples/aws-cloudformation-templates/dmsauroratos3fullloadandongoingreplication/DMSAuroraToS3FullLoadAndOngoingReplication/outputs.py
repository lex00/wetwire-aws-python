"""Template outputs."""

from . import *  # noqa: F403


class StackNameOutput:
    resource: Output
    value = AWS_STACK_NAME


class RegionNameOutput:
    resource: Output
    value = AWS_REGION


class S3BucketNameOutput:
    resource: Output
    value = S3Bucket


class AuroraEndpointOutput:
    resource: Output
    value = GetAtt("AuroraCluster", "Endpoint.Address")
