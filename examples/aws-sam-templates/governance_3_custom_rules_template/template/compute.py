"""Compute resources: GeneralLambdaAccessPermission."""

from . import *  # noqa: F403


class GeneralLambdaAccessPermission(lambda_.Permission):
    action = 'lambda:InvokeFunction'
    function_name = GenericRuleLambda
    principal = 'config.amazonaws.com'
    source_account = AWS_ACCOUNT_ID
