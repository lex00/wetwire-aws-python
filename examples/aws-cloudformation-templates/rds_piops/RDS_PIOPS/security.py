"""Security resources: DBCredential."""

from . import *  # noqa: F403


class DBCredentialGenerateSecretString:
    resource: secretsmanager.Secret.GenerateSecretString
    password_length = 16
    exclude_characters = '"@/\\'
    require_each_included_type = True


class DBCredential:
    resource: secretsmanager.Secret
    generate_secret_string = DBCredentialGenerateSecretString
