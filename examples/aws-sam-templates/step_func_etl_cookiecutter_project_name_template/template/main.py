"""Stack resources."""

from . import *  # noqa: F403


class FnCheck(serverless.Function):
    code_uri = 'functions/etl_check/'
    handler = 'app.lambda_handler'
    role = LambdaRole.Arn
    runtime = lambda_.Runtime.PYTHON3_9


class FnSuccess(serverless.Function):
    code_uri = 'functions/etl_success/'
    handler = 'app.lambda_handler'
    runtime = lambda_.Runtime.PYTHON3_9


class FnFailure(serverless.Function):
    code_uri = 'functions/etl_failure/'
    handler = 'app.lambda_handler'
    runtime = lambda_.Runtime.PYTHON3_9


class StateMachine(serverless.StateMachine):
    definition_uri = 'statemachine/asl.json'
    definition_substitutions = {
        'GlueJobName': pGlueJobName,
        'FnCheck': FnCheck.Arn,
        'FnSuccess': FnSuccess.Arn,
        'FnFailure': FnFailure.Arn,
    }
    role = StateMachineRole.Arn
