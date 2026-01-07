"""Security resources: UserPool, Client, Domain."""

from . import *  # noqa: F403


class UserPoolAdminCreateUserConfig(cognito.UserPool.AdminCreateUserConfig):
    allow_admin_create_user_only = True


class UserPoolSchemaAttribute(cognito.UserPool.SchemaAttribute):
    name = 'email'
    required = True


class UserPoolSchemaAttribute1(cognito.UserPool.SchemaAttribute):
    name = 'given_name'
    required = True


class UserPoolSchemaAttribute2(cognito.UserPool.SchemaAttribute):
    name = 'family_name'
    required = True


class UserPool(cognito.UserPool):
    resource: cognito.UserPool
    user_pool_name = AppName
    admin_create_user_config = UserPoolAdminCreateUserConfig
    auto_verified_attributes = ['email']
    mfa_configuration = 'OFF'
    schema = [UserPoolSchemaAttribute, UserPoolSchemaAttribute1, UserPoolSchemaAttribute2]


class Client(cognito.UserPoolClient):
    resource: cognito.UserPoolClient
    client_name = AppName
    generate_secret = False
    user_pool_id = UserPool
    callback_ur_ls = [CallbackURL]
    allowed_o_auth_flows = ['code']
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_scopes = ['phone', 'email', 'openid']
    supported_identity_providers = ['COGNITO']


class Domain(cognito.UserPoolDomain):
    resource: cognito.UserPoolDomain
    domain = AppName
    user_pool_id = UserPool
