import boto3
import pymongo
import uuid


def establish_ddb_connection():
    return boto3.resource('dynamodb', region_name='us-west-2')


def connect_to_dynamodb(dynamodb, predictions):
    discord_predictions = dynamodb.Table('discord-predictions')
    with discord_predictions.batch_writer() as batch:
        for p in predictions:
            batch.put_item(p)


def connect_to_mongodb():
    client = pymongo.MongoClient(
        "mongodb://bgraver:LlBnVBAfw6pbAcZI@lol-prediction-shard-00-00.5wr2n.mongodb.net:27017,lol-prediction-shard-00-01.5wr2n.mongodb.net:27017,lol-prediction-shard-00-02.5wr2n.mongodb.net:27017/lol-prediction?ssl=true&replicaSet=atlas-uoxvsb-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client['lol-prediction']
    discord_prediction = db['discord-predictions']
    prediction_list = []
    for p in discord_prediction.find():
        p.pop('_id')
        p['UUID'] = str(uuid.uuid1())
        prediction_list.append(p)
    return prediction_list


def run_migration():
    dynamodb = establish_ddb_connection()

    predictions = connect_to_mongodb()
    connect_to_dynamodb(dynamodb, predictions)

# run_migration()

