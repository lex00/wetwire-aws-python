"""Stack resources."""

from . import *  # noqa: F403


class ReportingV2App(serverless.Application):
    location = './reportingv2.yaml'
    parameters = {
        'DomainName': CustomDomainName,
    }


class ReportingV1App(serverless.Application):
    location = './reportingv1.yaml'
    parameters = {
        'DomainName': CustomDomainName,
    }


class AdminApp(serverless.Application):
    location = './admin.yaml'
    parameters = {
        'DomainName': CustomDomainName,
    }
