"""Storage resources: Bucket, Object1, Object3, Object2, Object4."""

from . import *  # noqa: F403


class Bucket:
    resource: s3.Bucket


class Object1:
    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = {
        'Bucket': Bucket,
        'Key': 'README.md',
        'ContentType': 'text/markdown',
    }
    body = """# My text file

This is my text file;
there are many like it,
but this one is mine.
"""
    depends_on = [Bucket]


class Object3S3Location:
    resource: databrew.Recipe.S3Location
    bucket = Object1.Bucket
    key = Object1.Key


class Object3S3Location1:
    resource: databrew.Recipe.S3Location
    bucket = Bucket
    key = 'README-copy.md'


class Object3:
    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    source = Object3S3Location
    target = Object3S3Location1
    depends_on = [Bucket]


class Object2:
    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = {
        'Bucket': Bucket,
        'Key': '1-pixel.gif',
        'ContentType': 'image/png',
    }
    base64_body = 'R0lGODdhAQABAIABAP///0qIbCwAAAAAAQABAAACAkQBADs='
    depends_on = [Bucket]


class Object4S3Location:
    resource: databrew.Recipe.S3Location
    bucket = Bucket
    key = 'readme.md'


class Object4:
    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = Object4S3Location
    url = 'https://raw.githubusercontent.com/aws-cloudformation/aws-cloudformation-templates/main/README.md'
    depends_on = [Bucket]
