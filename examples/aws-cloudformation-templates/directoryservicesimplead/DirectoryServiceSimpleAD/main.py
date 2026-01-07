"""Stack resources."""

from . import *  # noqa: F403


class SimpleADVpcSettings(directoryservice.SimpleAD.VpcSettings):
    subnet_ids = [Select(0, PrivateSubnet1), Select(0, PrivateSubnet2)]
    vpc_id = Select(0, VPCID)


class SimpleAD(directoryservice.SimpleAD):
    resource: directoryservice.SimpleAD
    create_alias = False
    enable_sso = False
    name = DomainName
    password = '{{resolve:secretsmanager:simple-ad-pw:SecretString:pasword}}'
    short_name = SimpleADShortName
    size = Size
    vpc_settings = SimpleADVpcSettings
