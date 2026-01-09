"""Stack resources."""

from . import *  # noqa: F403


class AppSyncApi(appsync.GraphQLApi):
    name = 'SingleTableApi'
    xray_enabled = True
    authentication_type = 'API_KEY'


class AppSyncSchema(appsync.GraphQLSchema):
    api_id = AppSyncApi.ApiId
    definition = """type Parent{
  PK: String!
  SK: String!
  children: [Child]
  data: String!
  type: String!
}

type Child {
  PK: String!
  SK: String!
  data: String!
  type: String!
}

type Mutation {
  createParentItem(
    PK: ID!,
    SK: String!,
    data: String!,
    type: String!
  ): Parent

  createChildItem(
    PK: ID!,
    SK: String!,
    data: String!,
    type: String!
  ): Child
}

type Query{
  getParentWithChildren(PK: ID!): Parent
}
"""


class DDBDataSourceDynamoDBConfig(appsync.DataSource.DynamoDBConfig):
    table_name = DDBTable
    aws_region = AWS_REGION


class DDBDataSource(appsync.DataSource):
    name = 'SingleTableDataSource'
    api_id = AppSyncApi.ApiId
    description = 'The Single Table AppSync Data Source'
    type_ = 'AMAZON_DYNAMODB'
    service_role_arn = DDBRole.Arn
    dynamo_db_config = DDBDataSourceDynamoDBConfig


class GetParentAndChildResolver(appsync.Resolver):
    api_id = AppSyncApi.ApiId
    type_name = 'Query'
    field_name = 'getParentWithChildren'
    data_source_name = DDBDataSource.Name
    request_mapping_template = """{
  "version" : "2017-02-28",
  "operation" : "Query",
  "query" : {
    "expression": "PK = :pk",
    "expressionValues" : {
        ":pk" : $util.dynamodb.toDynamoDBJson($ctx.args.PK)
    }
  }
}
"""
    response_mapping_template = """#set($children = [])

#foreach($item in $ctx.result.items)
  #if($item['type'] == "parent")
    #set($PK = $item['PK'])
    #set($SK = $item['SK'])
    #set($data = $item['data'])
    #set($type = $item['type'])
  #end
  #if($item['type'] == "child")
    $util.qr($children.add($item))
  #end
#end

{
  "PK": "${PK}",
    "SK": "${SK}",
    "children": $utils.toJson($children),
    "data": "${data}",
    "type": "${type}"
}
"""
    depends_on = [AppSyncSchema]


class CreateParentMutationResolver(appsync.Resolver):
    api_id = AppSyncApi.ApiId
    type_name = 'Mutation'
    field_name = 'createParentItem'
    data_source_name = DDBDataSource.Name
    request_mapping_template = """{
  "version": "2018-05-29",
  "operation": "PutItem",
  "key": {
    "PK": $util.dynamodb.toDynamoDBJson($ctx.args.PK),
    "SK": $util.dynamodb.toDynamoDBJson($ctx.args.SK)
  },
  "attributeValues": {
    "data": $util.dynamodb.toDynamoDBJson($ctx.args.data),
    "type": $util.dynamodb.toDynamoDBJson($ctx.args.type)
  }
}
"""
    response_mapping_template = '$util.toJson($ctx.result)'
    depends_on = [AppSyncSchema]


class AppSyncApiKey(appsync.ApiKey):
    api_id = AppSyncApi.ApiId


class CreateChildMutationResolver(appsync.Resolver):
    api_id = AppSyncApi.ApiId
    type_name = 'Mutation'
    field_name = 'createChildItem'
    data_source_name = DDBDataSource.Name
    request_mapping_template = """{
  "version": "2018-05-29",
  "operation": "PutItem",
  "key": {
    "PK": $util.dynamodb.toDynamoDBJson($ctx.args.PK),
    "SK": $util.dynamodb.toDynamoDBJson($ctx.args.SK)
  },
  "attributeValues": {
    "data": $util.dynamodb.toDynamoDBJson($ctx.args.data),
    "type": $util.dynamodb.toDynamoDBJson($ctx.args.type)
  }
}
"""
    response_mapping_template = '$util.toJson($ctx.result)'
    depends_on = [AppSyncSchema]
