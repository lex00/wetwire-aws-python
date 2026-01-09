"""Stack resources."""

from . import *  # noqa: F403


class SampleTablePrimaryKey(serverless.SimpleTable.PrimaryKey):
    name = 'id'
    type_ = 'String'


class SampleTableProvisionedThroughput(serverless.SimpleTable.ProvisionedThroughput):
    read_capacity_units = 2
    write_capacity_units = 2


class SampleTable(serverless.SimpleTable):
    primary_key = SampleTablePrimaryKey
    provisioned_throughput = SampleTableProvisionedThroughput


class getByIdFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'SAMPLE_TABLE': SampleTable,
    }


class getByIdFunction(serverless.Function):
    handler = 'src/handlers/get_by_id.getByIdHandler'
    runtime = lambda_.Runtime.PYTHON3_10
    memory_size = 128
    timeout = 100
    description = 'A simple example includes a HTTP get method to get one item by id from a DynamoDB table.'
    environment = getByIdFunctionEnvironment
    events = {
        'Api': {
            'Type': 'Api',
            'Properties': {
                'Path': '/{id}',
                'Method': 'GET',
            },
        },
    }


class putItemFunctionToTableConnectorConnectorDestination(serverless.Connector.ConnectorDestination):
    id = 'putItemFunction'


class putItemFunctionToTableConnectorConnectorDestination1(serverless.Connector.ConnectorDestination):
    id = 'SampleTable'


class putItemFunctionToTableConnector(serverless.Connector):
    source = putItemFunctionToTableConnectorConnectorDestination
    destination = putItemFunctionToTableConnectorConnectorDestination1
    permissions = ['Write']


class getAllItemsFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'SAMPLE_TABLE': SampleTable,
    }


class getAllItemsFunction(serverless.Function):
    handler = 'src/handlers/get_all_items.getAllItemsHandler'
    runtime = lambda_.Runtime.PYTHON3_10
    memory_size = 128
    timeout = 100
    description = 'A simple example includes a HTTP get method to get all items from a DynamoDB table.'
    environment = getAllItemsFunctionEnvironment
    events = {
        'Api': {
            'Type': 'Api',
            'Properties': {
                'Path': '/',
                'Method': 'GET',
            },
        },
    }


class getAllItemsFunctionToTableConnectorConnectorDestination(serverless.Connector.ConnectorDestination):
    id = 'getAllItemsFunction'


class getAllItemsFunctionToTableConnectorConnectorDestination1(serverless.Connector.ConnectorDestination):
    id = 'SampleTable'


class getAllItemsFunctionToTableConnector(serverless.Connector):
    source = getAllItemsFunctionToTableConnectorConnectorDestination
    destination = getAllItemsFunctionToTableConnectorConnectorDestination1
    permissions = ['Read']


class putItemFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'SAMPLE_TABLE': SampleTable,
    }


class putItemFunction(serverless.Function):
    handler = 'src/handlers/put_item.putItemHandler'
    runtime = lambda_.Runtime.PYTHON3_10
    memory_size = 128
    timeout = 100
    description = 'A simple example includes a HTTP post method to add one item to a DynamoDB table.'
    environment = putItemFunctionEnvironment
    events = {
        'Api': {
            'Type': 'Api',
            'Properties': {
                'Path': '/',
                'Method': 'POST',
            },
        },
    }


class getByIdFunctionToTableConnectorConnectorDestination(serverless.Connector.ConnectorDestination):
    id = 'getByIdFunction'


class getByIdFunctionToTableConnectorConnectorDestination1(serverless.Connector.ConnectorDestination):
    id = 'SampleTable'


class getByIdFunctionToTableConnector(serverless.Connector):
    source = getByIdFunctionToTableConnectorConnectorDestination
    destination = getByIdFunctionToTableConnectorConnectorDestination1
    permissions = ['Read']
