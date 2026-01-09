"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class AppName(Parameter):
    """Name of the application"""

    type = STRING
    description = 'Name of the application'
    default = 'AppConfigLambda'


class AppConfigLayerMapping(Mapping):
    map_data = {
        'us-east-1': {
            'ARN': 'arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:1',
        },
        'us-east-2': {
            'ARN': 'arn:aws:lambda:us-east-2:728743619870:layer:AWS-AppConfig-Extension:1',
        },
        'us-west-1': {
            'ARN': 'arn:aws:lambda:us-west-1:958113053741:layer:AWS-AppConfig-Extension:1',
        },
        'us-west-2': {
            'ARN': 'arn:aws:lambda:us-west-2:359756378197:layer:AWS-AppConfig-Extension:1',
        },
        'ca-central-1': {
            'ARN': 'arn:aws:lambda:ca-central-1:039592058896:layer:AWS-AppConfig-Extension:1',
        },
        'eu-central-1': {
            'ARN': 'arn:aws:lambda:eu-central-1:066940009817:layer:AWS-AppConfig-Extension:1',
        },
        'eu-west-1': {
            'ARN': 'arn:aws:lambda:eu-west-1:434848589818:layer:AWS-AppConfig-Extension:1',
        },
        'eu-west-2': {
            'ARN': 'arn:aws:lambda:eu-west-2:282860088358:layer:AWS-AppConfig-Extension:1',
        },
        'eu-west-3': {
            'ARN': 'arn:aws:lambda:eu-west-3:493207061005:layer:AWS-AppConfig-Extension:1',
        },
        'eu-north-1': {
            'ARN': 'arn:aws:lambda:eu-north-1:646970417810:layer:AWS-AppConfig-Extension:1',
        },
        'eu-south-1': {
            'ARN': 'arn:aws:lambda:eu-south-1:203683718741:layer:AWS-AppConfig-Extension:1',
        },
        'ap-east-1': {
            'ARN': 'arn:aws:lambda:ap-east-1:630222743974:layer:AWS-AppConfig-Extension:1',
        },
        'ap-northeast-1': {
            'ARN': 'arn:aws:lambda:ap-northeast-1:980059726660:layer:AWS-AppConfig-Extension:1',
        },
        'ap-northeast-2': {
            'ARN': 'arn:aws:lambda:ap-northeast-2:826293736237:layer:AWS-AppConfig-Extension:1',
        },
        'ap-southeast-1': {
            'ARN': 'arn:aws:lambda:ap-southeast-1:421114256042:layer:AWS-AppConfig-Extension:1',
        },
        'ap-southeast-2': {
            'ARN': 'arn:aws:lambda:ap-southeast-2:080788657173:layer:AWS-AppConfig-Extension:1',
        },
        'ap-south-1': {
            'ARN': 'arn:aws:lambda:ap-south-1:554480029851:layer:AWS-AppConfig-Extension:1',
        },
        'sa-east-1': {
            'ARN': 'arn:aws:lambda:sa-east-1:000010852771:layer:AWS-AppConfig-Extension:1',
        },
        'af-south-1': {
            'ARN': 'arn:aws:lambda:af-south-1:574348263942:layer:AWS-AppConfig-Extension:1',
        },
        'me-south-1': {
            'ARN': 'arn:aws:lambda:me-south-1:559955524753:layer:AWS-AppConfig-Extension:1',
        },
    }
