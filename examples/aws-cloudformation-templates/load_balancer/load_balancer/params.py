"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CertificateArn:
    resource: Parameter
    type = STRING


class VPCId:
    resource: Parameter
    type = STRING


class PublicSubnet1:
    resource: Parameter
    type = STRING


class PublicSubnet2:
    resource: Parameter
    type = STRING


class DestinationSecurityGroupId:
    resource: Parameter
    type = STRING
