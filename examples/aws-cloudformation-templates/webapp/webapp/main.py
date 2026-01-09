"""Stack resources."""

from . import *  # noqa: F403


class RestApi(apigateway.RestApi):
    name = AppName


class CognitoUserPoolAdminCreateUserConfig(cognito.UserPool.AdminCreateUserConfig):
    allow_admin_create_user_only = True


class CognitoUserPoolSchemaAttribute(cognito.UserPool.SchemaAttribute):
    name = 'email'
    required = True


class CognitoUserPoolSchemaAttribute1(cognito.UserPool.SchemaAttribute):
    name = 'given_name'
    required = True


class CognitoUserPoolSchemaAttribute2(cognito.UserPool.SchemaAttribute):
    name = 'family_name'
    required = True


class CognitoUserPool(cognito.UserPool):
    user_pool_name = AppName
    admin_create_user_config = CognitoUserPoolAdminCreateUserConfig
    auto_verified_attributes = ['email']
    schema = [CognitoUserPoolSchemaAttribute, CognitoUserPoolSchemaAttribute1, CognitoUserPoolSchemaAttribute2]
    depends_on = [SiteDistribution]


class CognitoClient(cognito.UserPoolClient):
    client_name = AppName
    generate_secret = False
    user_pool_id = CognitoUserPool
    callback_ur_ls = [Sub('https://${SiteDistribution.DomainName}/index.html')]
    allowed_o_auth_flows = ['code']
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_scopes = ['phone', 'email', 'openid']
    supported_identity_providers = ['COGNITO']


class SiteContentBucketAccessPolicyAllowStatement0(PolicyStatement):
    principal = {
        'Service': 'cloudfront.amazonaws.com',
    }
    action = 's3:GetObject'
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')
    condition = {
        STRING_EQUALS: {
            'AWS:SourceArn': Sub('arn:${AWS::Partition}:cloudfront::${AWS::AccountId}:distribution/${SiteDistribution.Id}'),
        },
    }


class SiteContentBucketAccessPolicyDenyStatement1(DenyStatement):
    principal = {
        'AWS': '*',
    }
    action = 's3:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*'),
    ]
    condition = {
        BOOL: {
            'aws:SecureTransport': False,
        },
    }


class SiteContentBucketAccessPolicyAllowStatement2(PolicyStatement):
    principal = {
        'Service': 'logging.s3.amazonaws.com',
    }
    action = 's3:PutObject'
    resource_arn = [Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')]
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}'),
        },
        STRING_EQUALS: {
            'aws:SourceAccount': AWS_ACCOUNT_ID,
        },
    }


class SiteContentBucketAccessPolicyPolicyDocument(PolicyDocument):
    statement = [SiteContentBucketAccessPolicyAllowStatement0, SiteContentBucketAccessPolicyDenyStatement1, SiteContentBucketAccessPolicyAllowStatement2]


class SiteContentBucketAccessPolicy(s3.BucketPolicy):
    bucket = SiteContentBucket
    policy_document = SiteContentBucketAccessPolicyPolicyDocument


class TestResourceResource(apigateway.Resource):
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'test'
    rest_api_id = RestApi


class RestApiAuthorizer(apigateway.Authorizer):
    identity_source = 'method.request.header.authorization'
    name = 'CognitoApiAuthorizer'
    provider_ar_ns = [CognitoUserPool.Arn]
    rest_api_id = RestApi
    type_ = 'COGNITO_USER_POOLS'


class TestResourceGetIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


class TestResourceGet(apigateway.Method):
    http_method = 'GET'
    resource_id = TestResourceResource
    rest_api_id = RestApi
    authorization_type = 'COGNITO_USER_POOLS'
    authorizer_id = RestApiAuthorizer
    integration = TestResourceGetIntegration


class JwtResourceResource(apigateway.Resource):
    parent_id = Sub('${RestApi.RootResourceId}')
    path_part = 'jwt'
    rest_api_id = RestApi


class JwtResourceGetIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


class JwtResourceGet(apigateway.Method):
    http_method = 'GET'
    resource_id = JwtResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    authorizer_id = 'AWS::NoValue'
    integration = JwtResourceGetIntegration


class JwtResourceOptionsIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${JwtResourceHandler.Arn}/invocations')


class JwtResourceOptions(apigateway.Method):
    http_method = 'OPTIONS'
    resource_id = JwtResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    integration = JwtResourceOptionsIntegration


class TestResourceOptionsIntegration(apigateway.Method.Integration):
    integration_http_method = 'POST'
    type_ = 'AWS_PROXY'
    uri = Sub('arn:${AWS::Partition}:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${TestResourceHandler.Arn}/invocations')


class TestResourceOptions(apigateway.Method):
    http_method = 'OPTIONS'
    resource_id = TestResourceResource
    rest_api_id = RestApi
    authorization_type = 'NONE'
    integration = TestResourceOptionsIntegration


class RestApiDeployment(apigateway.Deployment):
    rest_api_id = RestApi
    depends_on = [TestResourceGet, TestResourceOptions, JwtResourceGet, JwtResourceOptions]


class RestApiStage(apigateway.Stage):
    rest_api_id = RestApi
    deployment_id = RestApiDeployment
    stage_name = 'prod'


class CognitoDomain(cognito.UserPoolDomain):
    domain = AppName
    user_pool_id = CognitoUserPool
