"""Compute resources: ASCPrivateLinkLambdaFunction."""

from . import *  # noqa: F403


class ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.CapacityProvider.CapacityProviderVpcConfig
    subnet_ids = Subnets
    security_group_ids = SecurityGroups


class ASCPrivateLinkLambdaFunctionCode:
    resource: lambda_.Function.Code
    zip_file = Sub("""import boto3
import cfnresponse
import logging
def handler(event, context):
  print('Receive event: {} and context: {}'.format(str(event), str(context)))
  responseData = {}
  eventType = event['RequestType'].strip()
  props = event['ResourceProperties']
  try:
    if eventType in ('Create'):
      match props['Action']:
        case 'EnablePrivateDNS':
          dnsClient = boto3.client('route53')
          ec2Client = boto3.client('ec2')
          serviceId = props['ServiceId']
          domainName = props['DomainName']
          hostedZoneId = props['HostedZoneId']
          ec2Client.modify_vpc_endpoint_service_configuration(ServiceId=serviceId, PrivateDnsName=domainName)
          validationRecord = ec2Client.describe_vpc_endpoint_service_configurations(ServiceIds=[serviceId])['ServiceConfigurations'][0]['PrivateDnsNameConfiguration']
          dnsClient.change_resource_record_sets(
            HostedZoneId=hostedZoneId,
            ChangeBatch={
              'Changes': [
                {
                  'Action': 'UPSERT',
                  'ResourceRecordSet': {
                    'Type': validationRecord['Type'],
                    'Name': '{}.{}'.format(validationRecord['Name'], domainName[2:] if domainName.startswith('*') else domainName),
                    'ResourceRecords': [{'Value': '"{}"'.format(validationRecord['Value'])}],
                    'TTL': 300
                  }
                }
              ]
            }
          )
        case _:
          raise Exception('Unsupported action')
    else:
      print('Skip on resource UPDATE and DELETE')
    cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
  except Exception as e:
    logging.exception(e)
    cfnresponse.send(event, context, cfnresponse.FAILED, responseData)
""", {
    'Region': AWS_REGION,
})


class ASCPrivateLinkLambdaFunction(lambda_.Function):
    description = 'Lambda function to help with private link infrastructure setup'
    handler = 'index.handler'
    role = ASCPrivateLinkLambdaRole.Arn
    timeout = 900
    runtime = lambda_.Runtime.PYTHON3_12
    vpc_config = ASCPrivateLinkLambdaFunctionCapacityProviderVpcConfig
    code = ASCPrivateLinkLambdaFunctionCode
