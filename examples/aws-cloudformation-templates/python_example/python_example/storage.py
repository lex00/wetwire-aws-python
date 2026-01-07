"""Storage resources: S3Bucket."""

from . import *  # noqa: F403


class S3Bucket(s3.Bucket):
    resource: s3.Bucket
    tags = """#!PyPlate
output = []
for tag in params['Tags']:
   key, value = tag.split('=')
   output.append({"Key": key, "Value": value})"""
