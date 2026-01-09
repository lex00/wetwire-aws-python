"""Stack resources."""

from . import *  # noqa: F403


class SfnToStockCheckerFunctionConnectorConnectorDestination(serverless.Connector.ConnectorDestination):
    id = 'StockTradingStateMachine'


class SfnToStockCheckerFunctionConnectorConnectorDestination1(serverless.Connector.ConnectorDestination):
    id = 'StockCheckerFunction'


class SfnToStockCheckerFunctionConnector(serverless.Connector):
    source = SfnToStockCheckerFunctionConnectorConnectorDestination
    destination = SfnToStockCheckerFunctionConnectorConnectorDestination1
    permissions = ['Write']


class SfnToTransactionTableConnectorConnectorDestination(serverless.Connector.ConnectorDestination):
    id = 'StockTradingStateMachine'


class SfnToTransactionTableConnectorConnectorDestination1(serverless.Connector.ConnectorDestination):
    id = 'TransactionTable'


class SfnToTransactionTableConnector(serverless.Connector):
    source = SfnToTransactionTableConnectorConnectorDestination
    destination = SfnToTransactionTableConnectorConnectorDestination1
    permissions = ['Write']


class SfnToStockBuyerFunctionConnectorConnectorDestination(serverless.Connector.ConnectorDestination):
    id = 'StockTradingStateMachine'


class SfnToStockBuyerFunctionConnectorConnectorDestination1(serverless.Connector.ConnectorDestination):
    id = 'StockBuyerFunction'


class SfnToStockBuyerFunctionConnector(serverless.Connector):
    source = SfnToStockBuyerFunctionConnectorConnectorDestination
    destination = SfnToStockBuyerFunctionConnectorConnectorDestination1
    permissions = ['Write']


class SfnToStockSellerFunctionConnectorConnectorDestination(serverless.Connector.ConnectorDestination):
    id = 'StockTradingStateMachine'


class SfnToStockSellerFunctionConnectorConnectorDestination1(serverless.Connector.ConnectorDestination):
    id = 'StockSellerFunction'


class SfnToStockSellerFunctionConnector(serverless.Connector):
    source = SfnToStockSellerFunctionConnectorConnectorDestination
    destination = SfnToStockSellerFunctionConnectorConnectorDestination1
    permissions = ['Write']


class StockBuyerFunction(serverless.Function):
    code_uri = 'functions/stock_buyer/'
    handler = 'app.lambda_handler'
    runtime = lambda_.Runtime.PYTHON3_9


class StockSellerFunction(serverless.Function):
    code_uri = 'functions/stock_seller/'
    handler = 'app.lambda_handler'
    runtime = lambda_.Runtime.PYTHON3_9


class StockCheckerFunction(serverless.Function):
    code_uri = 'functions/stock_checker/'
    handler = 'app.lambda_handler'
    runtime = lambda_.Runtime.PYTHON3_9


class TransactionTablePrimaryKey(serverless.SimpleTable.PrimaryKey):
    name = 'Id'
    type_ = 'String'


class TransactionTableProvisionedThroughput(serverless.SimpleTable.ProvisionedThroughput):
    read_capacity_units = 1
    write_capacity_units = 1


class TransactionTable(serverless.SimpleTable):
    primary_key = TransactionTablePrimaryKey
    provisioned_throughput = TransactionTableProvisionedThroughput


class StockTradingStateMachine(serverless.StateMachine):
    definition_uri = 'statemachine/stock_trader.asl.json'
    definition_substitutions = {
        'StockCheckerFunctionArn': StockCheckerFunction.Arn,
        'StockSellerFunctionArn': StockSellerFunction.Arn,
        'StockBuyerFunctionArn': StockBuyerFunction.Arn,
        'DDBPutItem': Sub('arn:${AWS::Partition}:states:::dynamodb:putItem'),
        'DDBTable': TransactionTable,
    }
    events = {
        'HourlyTradingSchedule': {
            'Type': 'Schedule',
            'Properties': {
                'Description': 'Schedule to run the stock trading state machine every hour',
                'Enabled': False,
                'Schedule': 'rate(1 hour)',
            },
        },
    }
    policies = [{
        'CloudWatchPutMetricPolicy': {},
    }]
