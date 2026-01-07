"""Database resources: myDynamoDBTable."""

from . import *  # noqa: F403


class myDynamoDBTableAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = HashKeyElementName
    attribute_type = HashKeyElementType


class myDynamoDBTableKeySchema(dynamodb.Table.KeySchema):
    attribute_name = HashKeyElementName
    key_type = dynamodb.KeyType.HASH


class myDynamoDBTableProvisionedThroughput(dynamodb.Table.ProvisionedThroughput):
    read_capacity_units = ReadCapacityUnits
    write_capacity_units = WriteCapacityUnits


class myDynamoDBTablePointInTimeRecoverySpecification(dynamodb.Table.PointInTimeRecoverySpecification):
    point_in_time_recovery_enabled = True


class myDynamoDBTable(dynamodb.Table):
    resource: dynamodb.Table
    attribute_definitions = [myDynamoDBTableAttributeDefinition]
    key_schema = [myDynamoDBTableKeySchema]
    provisioned_throughput = myDynamoDBTableProvisionedThroughput
    point_in_time_recovery_specification = myDynamoDBTablePointInTimeRecoverySpecification
