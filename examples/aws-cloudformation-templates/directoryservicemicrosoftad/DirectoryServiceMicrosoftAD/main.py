"""Stack resources."""

from . import *  # noqa: F403


class rMSDirectoryVpcSettings(directoryservice.SimpleAD.VpcSettings):
    subnet_ids = [pPrivateSubnet1, pPrivateSubnet2]
    vpc_id = pVPCID


class rMSDirectory(directoryservice.MicrosoftAD):
    create_alias = pCreateAlias
    edition = pEdition
    enable_sso = pEnableSingleSignOn
    name = pDomainName
    password = '{{resolve:secretsmanager:microsoft-ad-pw:SecretString:password}}'
    short_name = pMicrosoftADShortName
    vpc_settings = rMSDirectoryVpcSettings
