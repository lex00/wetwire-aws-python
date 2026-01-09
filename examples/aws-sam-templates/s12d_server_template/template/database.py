"""Database resources: LinkTable."""

from . import *  # noqa: F403


class LinkTableKeySchema(dynamodb.Table.KeySchema):
    attribute_name = 'id'
    key_type = dynamodb.KeyType.HASH


class LinkTableAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = 'id'
    attribute_type = dynamodb.ScalarAttributeType.S


class LinkTableAttributeDefinition1(dynamodb.Table.AttributeDefinition):
    attribute_name = 'owner'
    attribute_type = dynamodb.ScalarAttributeType.S


class LinkTableKeySchema1(dynamodb.Table.KeySchema):
    attribute_name = 'owner'
    key_type = dynamodb.KeyType.HASH


class LinkTableProjection(dynamodb.Table.Projection):
    projection_type = 'ALL'


class LinkTableLocalSecondaryIndex(dynamodb.Table.LocalSecondaryIndex):
    index_name = 'OwnerIndex'
    key_schema = [LinkTableKeySchema1]
    projection = LinkTableProjection


class LinkTable(dynamodb.Table):
    billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST
    key_schema = [LinkTableKeySchema]
    attribute_definitions = [LinkTableAttributeDefinition, LinkTableAttributeDefinition1]
    global_secondary_indexes = [LinkTableLocalSecondaryIndex]
