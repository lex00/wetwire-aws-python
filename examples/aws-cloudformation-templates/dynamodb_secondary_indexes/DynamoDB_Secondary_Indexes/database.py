"""Database resources: TableOfBooks."""

from . import *  # noqa: F403


class TableOfBooksAttributeDefinition:
    resource: dynamodb.GlobalTable.AttributeDefinition
    attribute_name = 'Title'
    attribute_type = dynamodb.ScalarAttributeType.S


class TableOfBooksAttributeDefinition1:
    resource: dynamodb.GlobalTable.AttributeDefinition
    attribute_name = 'Category'
    attribute_type = dynamodb.ScalarAttributeType.S


class TableOfBooksAttributeDefinition2:
    resource: dynamodb.GlobalTable.AttributeDefinition
    attribute_name = 'Language'
    attribute_type = dynamodb.ScalarAttributeType.S


class TableOfBooksKeySchema:
    resource: dynamodb.GlobalTable.KeySchema
    attribute_name = 'Category'
    key_type = dynamodb.KeyType.HASH


class TableOfBooksKeySchema1:
    resource: dynamodb.GlobalTable.KeySchema
    attribute_name = 'Title'
    key_type = dynamodb.KeyType.RANGE


class TableOfBooksProvisionedThroughput:
    resource: dynamodb.Table.ProvisionedThroughput
    read_capacity_units = ReadCapacityUnits
    write_capacity_units = WriteCapacityUnits


class TableOfBooksKeySchema2:
    resource: dynamodb.GlobalTable.KeySchema
    attribute_name = 'Category'
    key_type = dynamodb.KeyType.HASH


class TableOfBooksKeySchema3:
    resource: dynamodb.GlobalTable.KeySchema
    attribute_name = 'Language'
    key_type = dynamodb.KeyType.RANGE


class TableOfBooksProjection:
    resource: dynamodb.GlobalTable.Projection
    projection_type = 'KEYS_ONLY'


class TableOfBooksLocalSecondaryIndex:
    resource: dynamodb.GlobalTable.LocalSecondaryIndex
    index_name = 'LanguageIndex'
    key_schema = [TableOfBooksKeySchema2, TableOfBooksKeySchema3]
    projection = TableOfBooksProjection


class TableOfBooksKeySchema4:
    resource: dynamodb.Table.KeySchema
    attribute_name = 'Title'
    key_type = dynamodb.KeyType.HASH


class TableOfBooksProjection1:
    resource: dynamodb.Table.Projection
    projection_type = 'KEYS_ONLY'


class TableOfBooksProvisionedThroughput1:
    resource: dynamodb.Table.ProvisionedThroughput
    read_capacity_units = ReadCapacityUnits
    write_capacity_units = WriteCapacityUnits


class TableOfBooksGlobalSecondaryIndex:
    resource: dynamodb.Table.GlobalSecondaryIndex
    index_name = 'TitleIndex'
    key_schema = [TableOfBooksKeySchema4]
    projection = TableOfBooksProjection1
    provisioned_throughput = TableOfBooksProvisionedThroughput1


class TableOfBooksPointInTimeRecoverySpecification:
    resource: dynamodb.GlobalTable.PointInTimeRecoverySpecification
    point_in_time_recovery_enabled = True


class TableOfBooks:
    resource: dynamodb.Table
    attribute_definitions = [TableOfBooksAttributeDefinition, TableOfBooksAttributeDefinition1, TableOfBooksAttributeDefinition2]
    key_schema = [TableOfBooksKeySchema, TableOfBooksKeySchema1]
    provisioned_throughput = TableOfBooksProvisionedThroughput
    local_secondary_indexes = [TableOfBooksLocalSecondaryIndex]
    global_secondary_indexes = [TableOfBooksGlobalSecondaryIndex]
    point_in_time_recovery_specification = TableOfBooksPointInTimeRecoverySpecification
