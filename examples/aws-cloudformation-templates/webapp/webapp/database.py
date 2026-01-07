"""Database resources: TestTable."""

from . import *  # noqa: F403


class TestTableAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = 'id'
    attribute_type = dynamodb.ScalarAttributeType.S


class TestTableKeySchema(dynamodb.Table.KeySchema):
    attribute_name = 'id'
    key_type = dynamodb.KeyType.HASH


class TestTable(dynamodb.Table):
    billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST
    table_name = Sub('${AppName}-test')
    attribute_definitions = [TestTableAttributeDefinition]
    key_schema = [TestTableKeySchema]
