import boto3
from boto3.dynamodb.conditions import Key


def create_user_table():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id="DUMMYIDEXAMPLE", aws_secret_access_key="DUMMYEXAMPLEKEY",
                              region_name="us-west-2", endpoint_url='http://localhost:8800')

    # aws_access_key_id = "DUMMYIDEXAMPLE", aws_secret_access_key = "DUMMYEXAMPLEKEY",
    # #                    region_name="us-west-2", endpoint_url='http://localhost:8800'

    table = dynamodb.create_table(
        TableName='itc_users',
        KeySchema=[
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'  # partition key
            },
            {
                'AttributeName': 'entity_id',
                'KeyType': 'RANGE'  # sort key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'entity_id',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )

    print("Table status:", table.table_status)


create_user_table()
