"""Database resources: TableOfBooks."""

from . import *  # noqa: F403


class TableOfBooksAttributeDefinition(dynamodb.Table.AttributeDefinition):
    attribute_name = 'Title'
    attribute_type = dynamodb.ScalarAttributeType.S


class TableOfBooksAttributeDefinition1(dynamodb.Table.AttributeDefinition):
    attribute_name = 'Category'
    attribute_type = dynamodb.ScalarAttributeType.S


class TableOfBooksAttributeDefinition2(dynamodb.Table.AttributeDefinition):
    attribute_name = 'Language'
    attribute_type = dynamodb.ScalarAttributeType.S


class TableOfBooksKeySchema(dynamodb.Table.KeySchema):
    attribute_name = 'Category'
    key_type = dynamodb.KeyType.HASH


class TableOfBooksKeySchema1(dynamodb.Table.KeySchema):
    attribute_name = 'Title'
    key_type = dynamodb.KeyType.RANGE


class TableOfBooksProvisionedThroughput(dynamodb.Table.ProvisionedThroughput):
    read_capacity_units = ReadCapacityUnits
    write_capacity_units = WriteCapacityUnits


class TableOfBooksKeySchema2(dynamodb.Table.KeySchema):
    attribute_name = 'Category'
    key_type = dynamodb.KeyType.HASH


class TableOfBooksKeySchema3(dynamodb.Table.KeySchema):
    attribute_name = 'Language'
    key_type = dynamodb.KeyType.RANGE


class TableOfBooksProjection(dynamodb.Table.Projection):
    projection_type = 'KEYS_ONLY'


class TableOfBooksLocalSecondaryIndex(dynamodb.Table.LocalSecondaryIndex):
    index_name = 'LanguageIndex'
    key_schema = [TableOfBooksKeySchema2, TableOfBooksKeySchema3]
    projection = TableOfBooksProjection


class TableOfBooksKeySchema4(dynamodb.Table.KeySchema):
    attribute_name = 'Title'
    key_type = dynamodb.KeyType.HASH


class TableOfBooksProjection1(dynamodb.Table.Projection):
    projection_type = 'KEYS_ONLY'


class TableOfBooksProvisionedThroughput1(dynamodb.Table.ProvisionedThroughput):
    read_capacity_units = ReadCapacityUnits
    write_capacity_units = WriteCapacityUnits


class TableOfBooksGlobalSecondaryIndex(dynamodb.Table.GlobalSecondaryIndex):
    index_name = 'TitleIndex'
    key_schema = [TableOfBooksKeySchema4]
    projection = TableOfBooksProjection1
    provisioned_throughput = TableOfBooksProvisionedThroughput1


class TableOfBooksPointInTimeRecoverySpecification(dynamodb.Table.PointInTimeRecoverySpecification):
    point_in_time_recovery_enabled = True


class TableOfBooks(dynamodb.Table):
    attribute_definitions = [TableOfBooksAttributeDefinition, TableOfBooksAttributeDefinition1, TableOfBooksAttributeDefinition2]
    key_schema = [TableOfBooksKeySchema, TableOfBooksKeySchema1]
    provisioned_throughput = TableOfBooksProvisionedThroughput
    local_secondary_indexes = [TableOfBooksLocalSecondaryIndex]
    global_secondary_indexes = [TableOfBooksGlobalSecondaryIndex]
    point_in_time_recovery_specification = TableOfBooksPointInTimeRecoverySpecification
