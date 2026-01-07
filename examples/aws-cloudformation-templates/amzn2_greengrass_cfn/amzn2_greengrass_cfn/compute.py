"""Compute resources: GroupDeploymentResetFunction, InstanceAZFunction, CreateThingFunction, GGSampleFunction, GGSampleFunctionVersion."""

from . import *  # noqa: F403


class GroupDeploymentResetFunctionEnvironment(lambda_.Function.Environment):
    variables = {
        'STACK_NAME': AWS_STACK_NAME,
    }


class GroupDeploymentResetFunctionCode(lambda_.Function.Code):
    zip_file = {
        'Rain::Embed': 'reset_function.py',
    }


class GroupDeploymentResetFunction(lambda_.Function):
    description = 'Resets any deployments during stack delete and manages Greengrass service role needs'
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_12
    role = LambdaExecutionRole.Arn
    timeout = 60
    environment = GroupDeploymentResetFunctionEnvironment
    code = GroupDeploymentResetFunctionCode


class InstanceAZFunctionCode(lambda_.Function.Code):
    zip_file = """import sys
import cfnresponse
import boto3
from botocore.exceptions import ClientError
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

c = boto3.client('ec2')


def handler(event, context):
    responseData = {}
    try:
        logger.info('Received event: {}'.format(json.dumps(event)))
        result = cfnresponse.FAILED
        if event['RequestType'] == 'Create':
            r = c.describe_reserved_instances_offerings(
                Filters=[
                    {
                        'Name': 'scope',
                        'Values': [
                            'Availability Zone',
                        ]
                    },
                ],
                IncludeMarketplace=False,
                InstanceType='t3.micro',
            )
            x = r['ReservedInstancesOfferings']
            while 'NextToken' in r:
                r = c.describe_reserved_instances_offerings(
                    Filters=[
                        {
                            'Name': 'scope',
                            'Values': [
                                'Availability Zone',
                            ]
                        },
                    ],
                    IncludeMarketplace=False,
                    InstanceType='t3.micro',
                    NextToken=r['NextToken']
                )
                x.extend(r['ReservedInstancesOfferings'])
            responseData['AvailabilityZone'] = set(d['AvailabilityZone'] for d in x).pop()
            result = cfnresponse.SUCCESS
        else:
            result = cfnresponse.SUCCESS
    except ClientError as e:
        logger.error('Error: {}'.format(e))
        result = cfnresponse.FAILED
    logger.info('Returning response of: %s, with result of: %s' % (result, responseData))
    sys.stdout.flush()
    cfnresponse.send(event, context, result, responseData)
"""


class InstanceAZFunction(lambda_.Function):
    description = 'Queries account and region for supported AZ'
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_12
    role = LambdaExecutionRole.Arn
    timeout = 60
    code = InstanceAZFunctionCode


class CreateThingFunctionCode(lambda_.Function.Code):
    zip_file = """import sys
import cfnresponse
import boto3
from botocore.exceptions import ClientError
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

policyDocument = {
    'Version': '2012-10-17',
    'Statement': [
        {
            'Effect': 'Allow',
            'Action': 'iot:*',
            'Resource': '*'
        },
        {
            'Effect': 'Allow',
            'Action': 'greengrass:*',
            'Resource': '*'
        }
    ]
}


def handler(event, context):
    responseData = {}
    try:
        logger.info('Received event: {}'.format(json.dumps(event)))
        result = cfnresponse.FAILED
        client = boto3.client('iot')
        thingName=event['ResourceProperties']['ThingName']
        if event['RequestType'] == 'Create':
            thing = client.create_thing(
                thingName=thingName
            )
            response = client.create_keys_and_certificate(
                setAsActive=True
            )
            certId = response['certificateId']
            certArn = response['certificateArn']
            certPem = response['certificatePem']
            privateKey = response['keyPair']['PrivateKey']
            client.create_policy(
                policyName='{}-full-access'.format(thingName),
                policyDocument=json.dumps(policyDocument)
            )
            response = client.attach_policy(
                policyName='{}-full-access'.format(thingName),
                target=certArn
            )
            response = client.attach_thing_principal(
                thingName=thingName,
                principal=certArn,
            )
            logger.info('Created thing: %s, cert: %s and policy: %s' % 
                (thingName, certId, '{}-full-access'.format(thingName)))
            result = cfnresponse.SUCCESS
            responseData['certificateId'] = certId
            responseData['certificatePem'] = certPem
            responseData['privateKey'] = privateKey
            responseData['iotEndpoint'] = client.describe_endpoint(endpointType='iot:Data-ATS')['endpointAddress']
        elif event['RequestType'] == 'Update':
            logger.info('Updating thing: %s' % thingName)
            result = cfnresponse.SUCCESS
        elif event['RequestType'] == 'Delete':
            logger.info('Deleting thing: %s and cert/policy' % thingName)
            response = client.list_thing_principals(
                thingName=thingName
            )
            for i in response['principals']:
                response = client.detach_thing_principal(
                    thingName=thingName,
                    principal=i
                )
                response = client.detach_policy(
                    policyName='{}-full-access'.format(thingName),
                    target=i
                )
                response = client.update_certificate(
                    certificateId=i.split('/')[-1],
                    newStatus='INACTIVE'
                )
                response = client.delete_certificate(
                    certificateId=i.split('/')[-1],
                    forceDelete=True
                )
                response = client.delete_policy(
                    policyName='{}-full-access'.format(thingName),
                )
                response = client.delete_thing(
                    thingName=thingName
                )
            result = cfnresponse.SUCCESS
    except ClientError as e:
        logger.error('Error: {}'.format(e))
        result = cfnresponse.FAILED
    logger.info('Returning response of: {}, with result of: {}'.format(result, responseData))
    sys.stdout.flush()
    cfnresponse.send(event, context, result, responseData)
"""


class CreateThingFunction(lambda_.Function):
    description = 'Create thing, certificate, and policy, return cert and private key'
    handler = 'index.handler'
    runtime = lambda_.Runtime.PYTHON3_12
    role = LambdaExecutionRole.Arn
    timeout = 60
    code = CreateThingFunctionCode


class GGSampleFunctionCode(lambda_.Function.Code):
    zip_file = """import os
from threading import Timer
import greengrasssdk


counter = 0
client = greengrasssdk.client('iot-data')


def telemetry():
    '''Publish incrementing value to telemetry topic every 2 seconds'''
    global counter
    counter += 1
    client.publish(
        topic='{}/telem'.format(os.environ['CORE_NAME']),
        payload='Example telemetry counter, value: {}'.format(counter)
    )
    Timer(5, telemetry).start()
# Call telemetry() to start telemetry publish
telemetry()


def function_handler(event, context):
    '''Echo message on /in topic to /out topic'''
    client.publish(
        topic='{}/out'.format(os.environ['CORE_NAME']),
        payload=event
    )
"""


class GGSampleFunction(lambda_.Function):
    function_name = Join('_', [
    CoreName,
    'sample',
])
    description = 'Long running lambda that provides telemetry and pub/sub echo'
    handler = 'index.function_handler'
    runtime = lambda_.Runtime.PYTHON3_12
    role = LambdaExecutionRole.Arn
    timeout = 60
    code = GGSampleFunctionCode


class GGSampleFunctionVersion(lambda_.Version):
    function_name = GGSampleFunction.Arn
