"""Stack resources."""

from . import *  # noqa: F403


class SampleTable(serverless.SimpleTable):
    pass


class putItemFunction(serverless.Function):
    handler = 'src/put-item.putItemHandler'
    description = 'put item in ddb table'
    policies = [{
        'DynamoDBCrudPolicy': {
            'TableName': SampleTable,
        },
    }]
    events = {
        'Api': {
            'Type': 'HttpApi',
            'Properties': {
                'Path': '/',
                'Method': 'POST',
            },
        },
    }


class getByIdFunction(serverless.Function):
    handler = 'src/get-by-id.getByIdHandler'
    description = 'get item by id'
    policies = [{
        'DynamoDBReadPolicy': {
            'TableName': SampleTable,
        },
    }]
    events = {
        'Api': {
            'Type': 'HttpApi',
            'Properties': {
                'Path': '/{id}',
                'Method': 'GET',
            },
        },
    }


class getAllItemsFunction(serverless.Function):
    handler = 'src/get-all-items.getAllItemsHandler'
    description = 'get all items'
    policies = [{
        'DynamoDBReadPolicy': {
            'TableName': SampleTable,
        },
    }]
    events = {
        'Api': {
            'Type': 'HttpApi',
            'Properties': {
                'Path': '/',
                'Method': 'GET',
            },
        },
    }
