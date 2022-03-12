import uuid

import boto3

from credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


def create_table():
    dynamodb = boto3.client('dynamodb', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)
    table = dynamodb.create_table(
        TableName='itc_entities',
        KeySchema=[
            {
                'AttributeName': 'entity_id',
                'KeyType': 'HASH'  # partition key
            }
        ],
        AttributeDefinitions=[
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


# create_table()

domain_not_allowed_list = [
    'gmail.com',
    'email.com'
]


def insert_users(name, user_email, password):
    dynamodb = boto3.client('dynamodb', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)

    # 1. Get email domain
    domain_name = user_email.split("@")[1]

    # Check is domain is not allowed
    if domain_name in domain_not_allowed_list:
        print(f"Domain {domain_name} not allowed")
        return

    # Check entity already exists or not
    item = dynamodb.get_item(TableName='itc_entities', Key={'admin_email': {'S': user_email}})
    for res in item:
        print(res)

    # dynamodb.put_item(TableName='itc_entities',
    #                   Item={'entity_id': {'S': str(uuid.uuid4())}, 'admin_email': {'S': user_email}, 'admin_name': {'S': name}})


insert_users('Ishwar Bhat', 'ishwar@email.com', 'MySecretKey')
insert_users('Rahul Dravid', 'rahul@bcci.com', 'MySecretKey')
insert_users('Virat Kohli', 'virat@rcb.com', 'MySecretKey')
insert_users('AB Devilliers', 'abd@rcb.com', 'MySecretKey')
insert_users('Lewis Hamilton', 'lewis@mercedes.com', 'MySecretKey')
