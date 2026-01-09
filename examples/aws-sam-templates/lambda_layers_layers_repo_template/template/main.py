"""Stack resources."""

from . import *  # noqa: F403


class NodeUtilitiesLayer(serverless.LayerVersion):
    description = 'Utilities layer for node apps (lodash, moment)'
    content_uri = 'node-utilities/'
    retention_policy = 'Retain'


class NodeBaseLayer(serverless.LayerVersion):
    description = 'Base layer for node apps (AWS-SDK, Axios)'
    content_uri = 'node-base/'
    retention_policy = 'Retain'


class PythonBaseLayer(serverless.LayerVersion):
    description = 'Base layer for python apps (boto3, requests)'
    content_uri = 'python-base/'
    retention_policy = 'Retain'
