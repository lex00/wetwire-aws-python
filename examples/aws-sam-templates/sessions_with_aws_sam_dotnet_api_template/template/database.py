"""Database resources: Users."""

from . import *  # noqa: F403


class UsersAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = 'id'
    attribute_type = dynamodb.ScalarAttributeType.S


class UsersKeySchema(dynamodb.Table.KeySchema):
    attribute_name = 'id'
    key_type = dynamodb.KeyType.HASH


class UsersStreamSpecification(dynamodb.GlobalTable.StreamSpecification):
    stream_view_type = 'NEW_AND_OLD_IMAGES'


class Users(dynamodb.Table):
    attribute_definitions = [UsersAttributeDefinition]
    billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST
    key_schema = [UsersKeySchema]
    stream_specification = UsersStreamSpecification
