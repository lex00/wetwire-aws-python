"""Database resources: urlTable."""

from . import *  # noqa: F403


class urlTableKeySchema(dynamodb.Table.KeySchema):
    attribute_name = 'id'
    key_type = dynamodb.KeyType.HASH


class urlTableAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = 'id'
    attribute_type = dynamodb.ScalarAttributeType.S


class urlTableTimeToLiveSpecification(dynamodb.Table.TimeToLiveSpecification):
    attribute_name = 'TTL'
    enabled = True


class urlTable(dynamodb.Table):
    billing_mode = dynamodb.BillingMode.PAY_PER_REQUEST
    key_schema = [urlTableKeySchema]
    attribute_definitions = [urlTableAttributeDefinition]
    time_to_live_specification = urlTableTimeToLiveSpecification
