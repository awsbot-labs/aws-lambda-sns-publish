import boto3
import os


def lambda_handler(event, context):
    """
    :param event:
    :param context:
    :return:
    """
    print event
    sns = boto3.client('sns')
    try:
        response = sns.publish(
            TargetArn=os.environ['TARGET_ARN'],
            Message=event['Records'][0]['dynamodb']['NewImage']['title']['S'],
            Subject='What\'s New'
        )
        print response
    except Exception as e:
        print e.message


if __name__ == "__main__":
    with open('event.json') as json_file:
        event = json.loads(json_file.read())
    lambda_handler(event, '')
