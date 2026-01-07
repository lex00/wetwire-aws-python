"""Stack resources."""

from . import *  # noqa: F403


class TransformFunction(serverless.Function):
    resource: serverless.Function
    runtime = lambda_.Runtime.PYTHON3_11
    handler = 'index.handler'
    memory_size = 128
    timeout = 3
    inline_code = """import datetime
def handler(event, context):
    response = {
        'requestId': event['requestId'],
        'status': 'success'
    }
    try:
        format = event['params']['format']
        response['fragment'] = datetime.datetime.now().strftime(format)
    except Exception as e:
        response['status'] = 'failure'
        response['errorMessage'] = str(e)
    return response
"""
