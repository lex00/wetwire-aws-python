"""Stack resources."""

from . import *  # noqa: F403


class DynamoDBInputS3OutputHiveParameterAttribute(datapipeline.Pipeline.ParameterAttribute):
    key = 'releaseLabel'
    string_value = 'emr-4.1.0'


class DynamoDBInputS3OutputHiveParameterAttribute1(datapipeline.Pipeline.ParameterAttribute):
    key = 'applications'
    string_value = 'spark'


class DynamoDBInputS3OutputHiveParameterAttribute2(datapipeline.Pipeline.ParameterAttribute):
    key = 'applications'
    string_value = 'hive'


class DynamoDBInputS3OutputHiveParameterAttribute3(datapipeline.Pipeline.ParameterAttribute):
    key = 'applications'
    string_value = 'pig'


class DynamoDBInputS3OutputHiveParameterAttribute4(datapipeline.Pipeline.ParameterAttribute):
    key = 'type'
    string_value = 'EmrCluster'


class DynamoDBInputS3OutputHiveField(datapipeline.Pipeline.Field):
    key = 'configuration'
    ref_value = 'coresite'


class DynamoDBInputS3OutputHivePipelineObject(datapipeline.Pipeline.PipelineObject):
    id = 'ResourceId_I1mCc'
    name = 'ReleaseLabelCluster'
    fields = [DynamoDBInputS3OutputHiveParameterAttribute, DynamoDBInputS3OutputHiveParameterAttribute1, DynamoDBInputS3OutputHiveParameterAttribute2, DynamoDBInputS3OutputHiveParameterAttribute3, DynamoDBInputS3OutputHiveParameterAttribute4, DynamoDBInputS3OutputHiveField]


class DynamoDBInputS3OutputHiveParameterAttribute5(datapipeline.Pipeline.ParameterAttribute):
    key = 'type'
    string_value = 'EmrConfiguration'


class DynamoDBInputS3OutputHiveParameterAttribute6(datapipeline.Pipeline.ParameterAttribute):
    key = 'classification'
    string_value = 'core-site'


class DynamoDBInputS3OutputHiveField1(datapipeline.Pipeline.Field):
    key = 'property'
    ref_value = 'io-file-buffer-size'


class DynamoDBInputS3OutputHiveField2(datapipeline.Pipeline.Field):
    key = 'property'
    ref_value = 'fs-s3-block-size'


class DynamoDBInputS3OutputHivePipelineObject1(datapipeline.Pipeline.PipelineObject):
    id = 'coresite'
    name = 'coresite'
    fields = [DynamoDBInputS3OutputHiveParameterAttribute5, DynamoDBInputS3OutputHiveParameterAttribute6, DynamoDBInputS3OutputHiveField1, DynamoDBInputS3OutputHiveField2]


class DynamoDBInputS3OutputHiveParameterAttribute7(datapipeline.Pipeline.ParameterAttribute):
    key = 'type'
    string_value = 'Property'


class DynamoDBInputS3OutputHiveParameterAttribute8(datapipeline.Pipeline.ParameterAttribute):
    key = 'value'
    string_value = '4096'


class DynamoDBInputS3OutputHiveParameterAttribute9(datapipeline.Pipeline.ParameterAttribute):
    key = 'key'
    string_value = 'io.file.buffer.size'


class DynamoDBInputS3OutputHivePipelineObject2(datapipeline.Pipeline.PipelineObject):
    id = 'io-file-buffer-size'
    name = 'io-file-buffer-size'
    fields = [DynamoDBInputS3OutputHiveParameterAttribute7, DynamoDBInputS3OutputHiveParameterAttribute8, DynamoDBInputS3OutputHiveParameterAttribute9]


class DynamoDBInputS3OutputHiveParameterAttribute10(datapipeline.Pipeline.ParameterAttribute):
    key = 'type'
    string_value = 'Property'


class DynamoDBInputS3OutputHiveParameterAttribute11(datapipeline.Pipeline.ParameterAttribute):
    key = 'value'
    string_value = '67108864'


class DynamoDBInputS3OutputHiveParameterAttribute12(datapipeline.Pipeline.ParameterAttribute):
    key = 'key'
    string_value = 'fs.s3.block.size'


class DynamoDBInputS3OutputHivePipelineObject3(datapipeline.Pipeline.PipelineObject):
    id = 'fs-s3-block-size'
    name = 'fs-s3-block-size'
    fields = [DynamoDBInputS3OutputHiveParameterAttribute10, DynamoDBInputS3OutputHiveParameterAttribute11, DynamoDBInputS3OutputHiveParameterAttribute12]


class DynamoDBInputS3OutputHiveParameterAttribute13(datapipeline.Pipeline.ParameterAttribute):
    key = 'occurrences'
    string_value = '1'


class DynamoDBInputS3OutputHiveParameterAttribute14(datapipeline.Pipeline.ParameterAttribute):
    key = 'startAt'
    string_value = 'FIRST_ACTIVATION_DATE_TIME'


class DynamoDBInputS3OutputHiveParameterAttribute15(datapipeline.Pipeline.ParameterAttribute):
    key = 'type'
    string_value = 'Schedule'


class DynamoDBInputS3OutputHiveParameterAttribute16(datapipeline.Pipeline.ParameterAttribute):
    key = 'period'
    string_value = '1 Day'


class DynamoDBInputS3OutputHivePipelineObject4(datapipeline.Pipeline.PipelineObject):
    id = 'DefaultSchedule'
    name = 'RunOnce'
    fields = [DynamoDBInputS3OutputHiveParameterAttribute13, DynamoDBInputS3OutputHiveParameterAttribute14, DynamoDBInputS3OutputHiveParameterAttribute15, DynamoDBInputS3OutputHiveParameterAttribute16]


class DynamoDBInputS3OutputHiveParameterAttribute17(datapipeline.Pipeline.ParameterAttribute):
    key = 'resourceRole'
    string_value = 'DataPipelineDefaultResourceRole'


class DynamoDBInputS3OutputHiveParameterAttribute18(datapipeline.Pipeline.ParameterAttribute):
    key = 'role'
    string_value = 'DataPipelineDefaultRole'


class DynamoDBInputS3OutputHiveParameterAttribute19(datapipeline.Pipeline.ParameterAttribute):
    key = 'scheduleType'
    string_value = 'cron'


class DynamoDBInputS3OutputHiveParameterAttribute20(datapipeline.Pipeline.ParameterAttribute):
    key = 'type'
    string_value = 'Default'


class DynamoDBInputS3OutputHiveField3(datapipeline.Pipeline.Field):
    key = 'schedule'
    ref_value = 'DefaultSchedule'


class DynamoDBInputS3OutputHivePipelineObject5(datapipeline.Pipeline.PipelineObject):
    id = 'Default'
    name = 'Default'
    fields = [DynamoDBInputS3OutputHiveParameterAttribute17, DynamoDBInputS3OutputHiveParameterAttribute18, DynamoDBInputS3OutputHiveParameterAttribute19, DynamoDBInputS3OutputHiveParameterAttribute20, DynamoDBInputS3OutputHiveField3]


class DynamoDBInputS3OutputHive(datapipeline.Pipeline):
    name = 'DynamoDBInputS3OutputHive'
    description = 'Pipeline to backup DynamoDB data to S3'
    activate = 'true'
    pipeline_objects = [DynamoDBInputS3OutputHivePipelineObject, DynamoDBInputS3OutputHivePipelineObject1, DynamoDBInputS3OutputHivePipelineObject2, DynamoDBInputS3OutputHivePipelineObject3, DynamoDBInputS3OutputHivePipelineObject4, DynamoDBInputS3OutputHivePipelineObject5]
