"""Database resources: myDynamoDBTable."""

from . import *  # noqa: F403


class myDynamoDBTableAttributeDefinition:
    resource: dynamodb.GlobalTable.AttributeDefinition
    attribute_name = HashKeyElementName
    attribute_type = HashKeyElementType


class myDynamoDBTableKeySchema:
    resource: dynamodb.GlobalTable.KeySchema
    attribute_name = HashKeyElementName
    key_type = dynamodb.KeyType.HASH


class myDynamoDBTableProvisionedThroughput:
    resource: dynamodb.Table.ProvisionedThroughput
    read_capacity_units = ReadCapacityUnits
    write_capacity_units = WriteCapacityUnits


class myDynamoDBTablePointInTimeRecoverySpecification:
    resource: dynamodb.GlobalTable.PointInTimeRecoverySpecification
    point_in_time_recovery_enabled = True


class myDynamoDBTable:
    resource: dynamodb.Table
    attribute_definitions = [myDynamoDBTableAttributeDefinition]
    key_schema = [myDynamoDBTableKeySchema]
    provisioned_throughput = myDynamoDBTableProvisionedThroughput
    point_in_time_recovery_specification = myDynamoDBTablePointInTimeRecoverySpecification
