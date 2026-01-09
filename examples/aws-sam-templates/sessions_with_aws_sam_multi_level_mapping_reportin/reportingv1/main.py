"""Stack resources."""

from . import *  # noqa: F403


class ReportingAPIV1(serverless.HttpApi):
    description = 'Reporting API V1'
    disable_execute_api_endpoint = True


class GlobalReportingV1(serverless.Function):
    code_uri = 'src/global-reportingv1'
    events = {
        'GlobalReportingV1': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': ReportingAPIV1,
                'Method': 'GET',
                'Path': '/global',
            },
        },
    }


class RegionalReporting(serverless.Function):
    code_uri = 'src/regional-reporting'
    events = {
        'RegionalReporting': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': ReportingAPIV1,
                'Method': 'GET',
                'Path': '/regional',
            },
        },
    }
