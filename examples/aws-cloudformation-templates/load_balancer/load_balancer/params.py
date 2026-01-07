"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CertificateArn(Parameter):
    type = STRING


class VPCId(Parameter):
    type = STRING


class PublicSubnet1(Parameter):
    type = STRING


class PublicSubnet2(Parameter):
    type = STRING


class DestinationSecurityGroupId(Parameter):
    type = STRING
