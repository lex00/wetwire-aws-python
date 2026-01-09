"""Security resources: UserPool, AdminUser, AdminUserGroup, AddUserToGroup, UserPoolDomain, UserPoolClient."""

from . import *  # noqa: F403


class UserPoolPasswordPolicy(cognito.UserPool.PasswordPolicy):
    minimum_length = 8


class UserPoolPolicies(cognito.UserPool.Policies):
    password_policy = UserPoolPasswordPolicy


class UserPoolSchemaAttribute(cognito.UserPool.SchemaAttribute):
    attribute_data_type = 'String'
    name = 'email'
    required = False


class UserPool(cognito.UserPool):
    user_pool_name = Sub('${AppName}-UserPool')
    policies = UserPoolPolicies
    auto_verified_attributes = ['email']
    username_attributes = ['email']
    schema = [UserPoolSchemaAttribute]


class AdminUserAttributeType(cognito.UserPoolUser.AttributeType):
    name = 'email'
    value = AdminEmail


class AdminUser(cognito.UserPoolUser):
    username = AdminEmail
    desired_delivery_mediums = ['EMAIL']
    force_alias_creation = True
    user_attributes = [AdminUserAttributeType]
    user_pool_id = UserPool


class AdminUserGroup(cognito.UserPoolGroup):
    group_name = 'Admins'
    description = 'Admin user group'
    precedence = 0
    user_pool_id = UserPool


class AddUserToGroup(cognito.UserPoolUserToGroupAttachment):
    group_name = AdminUserGroup
    username = AdminUser
    user_pool_id = UserPool


class UserPoolDomain(cognito.UserPoolDomain):
    domain = Sub('${AppName}-${AWS::AccountId}')
    user_pool_id = UserPool


class UserPoolClient(cognito.UserPoolClient):
    user_pool_id = UserPool
    client_name = Sub('${AppName}-UserPoolClient')
    generate_secret = False
    supported_identity_providers = ['COGNITO']
    callback_ur_ls = ClientDomains
    logout_ur_ls = ClientDomains
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_flows = ['code', 'implicit']
    allowed_o_auth_scopes = ['email', 'openid', 'profile']
