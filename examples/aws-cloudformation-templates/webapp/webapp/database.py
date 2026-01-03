"""Database resources: TestTable."""

from . import *  # noqa: F403


class TestTableAttributeDefinition:
    resource: dynamodb.GlobalTable.AttributeDefinition
    attribute_name = 'id'
    attribute_type = dynamodb.ScalarAttributeType.S


class TestTableKeySchema:
    resource: dynamodb.GlobalTable.KeySchema
    attribute_name = 'id'
    key_type = dynamodb.KeyType.HASH


class TestTable:
    resource: dynamodb.Table
    billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST
    table_name = Sub('${AppName}-test')
    attribute_definitions = [TestTableAttributeDefinition]
    key_schema = [TestTableKeySchema]
