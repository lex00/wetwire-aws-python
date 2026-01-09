"""Stack resources."""

from . import *  # noqa: F403


class S3JsonLoggerFunction(serverless.Function):
    code_uri = './src/S3EventSource/'
    handler = 'S3EventSource::S3EventSource.Function::FunctionHandler'
    runtime = 'dotnet10'
    memory_size = 512
    policies = {
        'S3ReadPolicy': {
            'BucketName': AppBucketName,
        },
    }
    events = {
        'S3NewObjectEvent': {
            'Type': 'S3',
            'Properties': {
                'Bucket': AppBucket,
                'Events': 's3:ObjectCreated:*',
                'Filter': {
                    'S3Key': {
                        'Rules': [{
                            'Name': 'suffix',
                            'Value': '.json',
                        }],
                    },
                },
            },
        },
    }
