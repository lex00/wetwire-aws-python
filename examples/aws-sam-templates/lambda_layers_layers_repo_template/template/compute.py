"""Compute resources: NodeBaseLayerPermission, PythonBaseLayerPermission, NodeUtilitiesLayerPermission."""

from . import *  # noqa: F403


class NodeBaseLayerPermission(lambda_.LayerVersionPermission):
    action = 'lambda:GetLayerVersion'
    layer_version_arn = NodeBaseLayer
    principal = AWS_ACCOUNT_ID


class PythonBaseLayerPermission(lambda_.LayerVersionPermission):
    action = 'lambda:GetLayerVersion'
    layer_version_arn = PythonBaseLayer
    principal = AWS_ACCOUNT_ID


class NodeUtilitiesLayerPermission(lambda_.LayerVersionPermission):
    action = 'lambda:GetLayerVersion'
    layer_version_arn = NodeUtilitiesLayer
    principal = AWS_ACCOUNT_ID
