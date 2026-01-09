"""Stack resources."""

from . import *  # noqa: F403


class uploadSignerLambda(serverless.Function):
    code_uri = 'lambda/uploadSigner/'
    policies = [{
        'S3WritePolicy': {
            'BucketName': storageBucket,
        },
    }]


class downloadSignerLambda(serverless.Function):
    code_uri = 'lambda/downloadSigner/'
    policies = [{
        'S3ReadPolicy': {
            'BucketName': storageBucket,
        },
    }]


class urlStateMachineTracingConfiguration(serverless.StateMachine.TracingConfiguration):
    enabled = True


class urlStateMachine(serverless.StateMachine):
    type_ = 'EXPRESS'
    tracing = urlStateMachineTracingConfiguration
    definition = {
        'StartAt': 'Generate Signed URLs',
        'States': {
            'Generate Signed URLs': {
                'Type': 'Parallel',
                'Comment': 'Fetches a signed upload and download URL for the given Key',
                'Next': 'formatResults',
                'Branches': [
                    {
                        'StartAt': 'GetUploadSignedUrl',
                        'States': {
                            'GetUploadSignedUrl': {
                                'End': True,
                                'Retry': [{
                                    'ErrorEquals': [
                                        'Lambda.ServiceException',
                                        'Lambda.AWSLambdaException',
                                        'Lambda.SdkClientException',
                                    ],
                                    'IntervalSeconds': 2,
                                    'MaxAttempts': 6,
                                    'BackoffRate': 2,
                                }],
                                'Type': 'Task',
                                'ResultPath': '$.UploadSignResults',
                                'Resource': 'arn:aws:states:::lambda:invoke',
                                'Parameters': {
                                    'FunctionName': '${GetUploadSignerFunction}',
                                    'Payload.$': '$',
                                },
                            },
                        },
                    },
                    {
                        'StartAt': 'GetDownloadSignedUrl',
                        'States': {
                            'GetDownloadSignedUrl': {
                                'Next': 'WriteToDynamoDB',
                                'Retry': [{
                                    'ErrorEquals': [
                                        'Lambda.ServiceException',
                                        'Lambda.AWSLambdaException',
                                        'Lambda.SdkClientException',
                                    ],
                                    'IntervalSeconds': 2,
                                    'MaxAttempts': 6,
                                    'BackoffRate': 2,
                                }],
                                'Type': 'Task',
                                'OutputPath': '$',
                                'ResultPath': '$.DownloadSignResults',
                                'Resource': 'arn:aws:states:::lambda:invoke',
                                'Parameters': {
                                    'FunctionName': '${GetDownloadSignerFunction}',
                                    'Payload.$': '$',
                                },
                            },
                            'WriteToDynamoDB': {
                                'End': True,
                                'Type': 'Task',
                                'OutputPath': '$',
                                'ResultPath': '$.DynamoResults',
                                'Resource': '${DDBPutItem}',
                                'Parameters': {
                                    'Item': {
                                        'id': {
                                            'S.$': '$.DownloadSignResults.Payload.id',
                                        },
                                        'signedUrl': {
                                            'S.$': '$.DownloadSignResults.Payload.signedUrl',
                                        },
                                        'TTL': {
                                            'N.$': '$.DownloadSignResults.Payload.ttl',
                                        },
                                    },
                                    'TableName': '${DDBTable}',
                                },
                            },
                        },
                    },
                ],
            },
            'formatResults': {
                'Type': 'Pass',
                'Parameters': {
                    'UploadUrl.$': '$[0].UploadSignResults.Payload.signedUrl',
                    'DownloadUrl.$': '$[1].DownloadSignResults.Payload.signedUrl',
                    'DownloadShortId.$': '$[1].DownloadSignResults.Payload.id',
                },
                'End': True,
            },
        },
        'TimeoutSeconds': 30,
    }
    policies = [{
        'DynamoDBWritePolicy': {
            'TableName': urlTable,
        },
    }, {
        'LambdaInvokePolicy': {
            'FunctionName': uploadSignerLambda,
        },
    }, {
        'LambdaInvokePolicy': {
            'FunctionName': downloadSignerLambda,
        },
    }]
    definition_substitutions = {
        'DDBPutItem': Sub('arn:${AWS::Partition}:states:::dynamodb:putItem'),
        'DDBTable': urlTable,
        'GetUploadSignerFunction': uploadSignerLambda.Arn,
        'GetDownloadSignerFunction': downloadSignerLambda.Arn,
    }


class httpApi(serverless.HttpApi):
    definition_body = {
        'openapi': '3.0.1',
        'info': {
            'title': 'Signed URL Generator - Built with AWS SAM',
        },
        'paths': {
            '/': {
                'post': {
                    'responses': {
                        'default': {
                            'description': 'Step Function Response',
                        },
                    },
                    'x-amazon-apigateway-integration': {
                        'integrationSubtype': 'StepFunctions-StartSyncExecution',
                        'credentials': httpApiRole.Arn,
                        'requestParameters': {
                            'Input': '$request.body',
                            'StateMachineArn': urlStateMachine.Arn,
                        },
                        'payloadFormatVersion': '1.0',
                        'type': 'aws_proxy',
                        'connectionType': 'INTERNET',
                    },
                },
            },
        },
    }


class fetchedShortUrlLambda(serverless.Function):
    code_uri = 'lambda/fetchShortUrl/'
    policies = {
        'DynamoDBReadPolicy': {
            'TableName': urlTable,
        },
    }
    events = {
        'ApiEvent': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': httpApi,
                'Path': '/{id}',
                'Method': 'GET',
            },
        },
    }
