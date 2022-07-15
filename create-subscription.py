import os
from google.cloud import pubsub_v1
PROJECT_ID = os.getenv('PROJECT_ID')
TOPIC_ID = "new-topic"
SUB_ID = "new-topic-sub-2"

topic_name = f'projects/{PROJECT_ID}/topics/{TOPIC_ID}'

subscription_name = f'projects/{PROJECT_ID}/subscriptions/{SUB_ID}'

def callback(message):
    print(message.data)
    message.ack()

with pubsub_v1.SubscriberClient() as subscriber:
    subscriber.create_subscription(
        name=subscription_name, topic=topic_name)
    future = subscriber.subscribe(subscription_name, callback)