"""Storage resources: Bucket, Object1, Object2, Object3, Object4."""

from . import *  # noqa: F403


class Bucket(s3.Bucket):
    resource: s3.Bucket


class Object1(CloudFormationResource):
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


class Object2(CloudFormationResource):
    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = {
        'Bucket': Bucket,
        'Key': '1-pixel.gif',
        'ContentType': 'image/png',
    }
    base64_body = 'R0lGODdhAQABAIABAP///0qIbCwAAAAAAQABAAACAkQBADs='
    depends_on = [Bucket]


class Object3ManifestFileLocation(quicksight.DataSource.ManifestFileLocation):
    bucket = Object1.Bucket
    key = Object1.Key


class Object3ManifestFileLocation1(quicksight.DataSource.ManifestFileLocation):
    bucket = Bucket
    key = 'README-copy.md'


class Object3(CloudFormationResource):
    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    source = Object3ManifestFileLocation
    target = Object3ManifestFileLocation1
    depends_on = [Bucket]


class Object4ManifestFileLocation(quicksight.DataSource.ManifestFileLocation):
    bucket = Bucket
    key = 'readme.md'


class Object4(CloudFormationResource):
    # Unknown resource type: AWS::S3::Object
    resource: CloudFormationResource
    target = Object4ManifestFileLocation
    url = 'https://raw.githubusercontent.com/aws-cloudformation/aws-cloudformation-templates/main/README.md'
    depends_on = [Bucket]
