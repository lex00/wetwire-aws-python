"""Stack resources."""

from . import *  # noqa: F403


class DynamoDBInputS3OutputHiveField(datapipeline.Pipeline.Field):
    key = 'releaseLabel'
    string_value = 'emr-4.1.0'


class DynamoDBInputS3OutputHiveField1(datapipeline.Pipeline.Field):
    key = 'applications'
    string_value = 'spark'


class DynamoDBInputS3OutputHiveField2(datapipeline.Pipeline.Field):
    key = 'applications'
    string_value = 'hive'


class DynamoDBInputS3OutputHiveField3(datapipeline.Pipeline.Field):
    key = 'applications'
    string_value = 'pig'


class DynamoDBInputS3OutputHiveField4(datapipeline.Pipeline.Field):
    key = 'type'
    string_value = 'EmrCluster'


class DynamoDBInputS3OutputHiveField5(datapipeline.Pipeline.Field):
    key = 'configuration'
    ref_value = 'coresite'


class DynamoDBInputS3OutputHivePipelineObject(datapipeline.Pipeline.PipelineObject):
    id = 'ResourceId_I1mCc'
    name = 'ReleaseLabelCluster'
    fields = [DynamoDBInputS3OutputHiveField, DynamoDBInputS3OutputHiveField1, DynamoDBInputS3OutputHiveField2, DynamoDBInputS3OutputHiveField3, DynamoDBInputS3OutputHiveField4, DynamoDBInputS3OutputHiveField5]


class DynamoDBInputS3OutputHiveField6(datapipeline.Pipeline.Field):
    key = 'type'
    string_value = 'EmrConfiguration'


class DynamoDBInputS3OutputHiveField7(datapipeline.Pipeline.Field):
    key = 'classification'
    string_value = 'core-site'


class DynamoDBInputS3OutputHiveField8(datapipeline.Pipeline.Field):
    key = 'property'
    ref_value = 'io-file-buffer-size'


class DynamoDBInputS3OutputHiveField9(datapipeline.Pipeline.Field):
    key = 'property'
    ref_value = 'fs-s3-block-size'


class DynamoDBInputS3OutputHivePipelineObject1(datapipeline.Pipeline.PipelineObject):
    id = 'coresite'
    name = 'coresite'
    fields = [DynamoDBInputS3OutputHiveField6, DynamoDBInputS3OutputHiveField7, DynamoDBInputS3OutputHiveField8, DynamoDBInputS3OutputHiveField9]


class DynamoDBInputS3OutputHiveField10(datapipeline.Pipeline.Field):
    key = 'type'
    string_value = 'Property'


class DynamoDBInputS3OutputHiveField11(datapipeline.Pipeline.Field):
    key = 'value'
    string_value = '4096'


class DynamoDBInputS3OutputHiveField12(datapipeline.Pipeline.Field):
    key = 'key'
    string_value = 'io.file.buffer.size'


class DynamoDBInputS3OutputHivePipelineObject2(datapipeline.Pipeline.PipelineObject):
    id = 'io-file-buffer-size'
    name = 'io-file-buffer-size'
    fields = [DynamoDBInputS3OutputHiveField10, DynamoDBInputS3OutputHiveField11, DynamoDBInputS3OutputHiveField12]


class DynamoDBInputS3OutputHiveField13(datapipeline.Pipeline.Field):
    key = 'type'
    string_value = 'Property'


class DynamoDBInputS3OutputHiveField14(datapipeline.Pipeline.Field):
    key = 'value'
    string_value = '67108864'


class DynamoDBInputS3OutputHiveField15(datapipeline.Pipeline.Field):
    key = 'key'
    string_value = 'fs.s3.block.size'


class DynamoDBInputS3OutputHivePipelineObject3(datapipeline.Pipeline.PipelineObject):
    id = 'fs-s3-block-size'
    name = 'fs-s3-block-size'
    fields = [DynamoDBInputS3OutputHiveField13, DynamoDBInputS3OutputHiveField14, DynamoDBInputS3OutputHiveField15]


class DynamoDBInputS3OutputHiveField16(datapipeline.Pipeline.Field):
    key = 'occurrences'
    string_value = '1'


class DynamoDBInputS3OutputHiveField17(datapipeline.Pipeline.Field):
    key = 'startAt'
    string_value = 'FIRST_ACTIVATION_DATE_TIME'


class DynamoDBInputS3OutputHiveField18(datapipeline.Pipeline.Field):
    key = 'type'
    string_value = 'Schedule'


class DynamoDBInputS3OutputHiveField19(datapipeline.Pipeline.Field):
    key = 'period'
    string_value = '1 Day'


class DynamoDBInputS3OutputHivePipelineObject4(datapipeline.Pipeline.PipelineObject):
    id = 'DefaultSchedule'
    name = 'RunOnce'
    fields = [DynamoDBInputS3OutputHiveField16, DynamoDBInputS3OutputHiveField17, DynamoDBInputS3OutputHiveField18, DynamoDBInputS3OutputHiveField19]


class DynamoDBInputS3OutputHiveField20(datapipeline.Pipeline.Field):
    key = 'resourceRole'
    string_value = 'DataPipelineDefaultResourceRole'


class DynamoDBInputS3OutputHiveField21(datapipeline.Pipeline.Field):
    key = 'role'
    string_value = 'DataPipelineDefaultRole'


class DynamoDBInputS3OutputHiveField22(datapipeline.Pipeline.Field):
    key = 'scheduleType'
    string_value = 'cron'


class DynamoDBInputS3OutputHiveField23(datapipeline.Pipeline.Field):
    key = 'type'
    string_value = 'Default'


class DynamoDBInputS3OutputHiveField24(datapipeline.Pipeline.Field):
    key = 'schedule'
    ref_value = 'DefaultSchedule'


class DynamoDBInputS3OutputHivePipelineObject5(datapipeline.Pipeline.PipelineObject):
    id = 'Default'
    name = 'Default'
    fields = [DynamoDBInputS3OutputHiveField20, DynamoDBInputS3OutputHiveField21, DynamoDBInputS3OutputHiveField22, DynamoDBInputS3OutputHiveField23, DynamoDBInputS3OutputHiveField24]


class DynamoDBInputS3OutputHive(datapipeline.Pipeline):
    name = 'DynamoDBInputS3OutputHive'
    description = 'Pipeline to backup DynamoDB data to S3'
    activate = 'true'
    pipeline_objects = [DynamoDBInputS3OutputHivePipelineObject, DynamoDBInputS3OutputHivePipelineObject1, DynamoDBInputS3OutputHivePipelineObject2, DynamoDBInputS3OutputHivePipelineObject3, DynamoDBInputS3OutputHivePipelineObject4, DynamoDBInputS3OutputHivePipelineObject5]
