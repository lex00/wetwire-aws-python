"""Database resources: ProcessedDataTable."""

from . import *  # noqa: F403


class ProcessedDataTableKeySchema(dynamodb.Table.KeySchema):
    attribute_name = 'id'
    key_type = dynamodb.KeyType.HASH


class ProcessedDataTableAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = 'id'
    attribute_type = dynamodb.ScalarAttributeType.S


class ProcessedDataTableTimeToLiveSpecification(dynamodb.Table.TimeToLiveSpecification):
    attribute_name = 'ttl'
    enabled = True


class ProcessedDataTable(dynamodb.Table):
    billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST
    key_schema = [ProcessedDataTableKeySchema]
    attribute_definitions = [ProcessedDataTableAttributeDefinition]
    time_to_live_specification = ProcessedDataTableTimeToLiveSpecification
