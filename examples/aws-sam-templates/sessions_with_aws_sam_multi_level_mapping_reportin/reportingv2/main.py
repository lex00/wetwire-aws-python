"""Stack resources."""

from . import *  # noqa: F403


class ReportingAPIV2(serverless.HttpApi):
    description = 'Reporting API V2'
    disable_execute_api_endpoint = True


class GlobalReportingV2(serverless.Function):
    code_uri = 'src/global-reportingv2'
    events = {
        'GlobalReportingV2': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': ReportingAPIV2,
                'Method': 'GET',
                'Path': '/global',
            },
        },
    }
