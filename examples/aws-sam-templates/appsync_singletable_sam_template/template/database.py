"""Database resources: DDBTable."""

from . import *  # noqa: F403


class DDBTableAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = 'PK'
    attribute_type = dynamodb.ScalarAttributeType.S


class DDBTableAttributeDefinition1(dynamodb.Table.AttributeDefinition):
    attribute_name = 'SK'
    attribute_type = dynamodb.ScalarAttributeType.S


class DDBTableKeySchema(dynamodb.Table.KeySchema):
    attribute_name = 'PK'
    key_type = dynamodb.KeyType.HASH


class DDBTableKeySchema1(dynamodb.Table.KeySchema):
    attribute_name = 'SK'
    key_type = dynamodb.KeyType.RANGE


class DDBTable(dynamodb.Table):
    billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST
    attribute_definitions = [DDBTableAttributeDefinition, DDBTableAttributeDefinition1]
    key_schema = [DDBTableKeySchema, DDBTableKeySchema1]
