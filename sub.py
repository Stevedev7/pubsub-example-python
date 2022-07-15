
import os
from google.cloud import pubsub_v1

TIMEOUT = 120
SUB_ID = os.getenv('SUB_ID')
PROJECT_ID = os.getenv('PROJECT_ID')

subscriber = pubsub_v1.SubscriberClient()

subscription_path = f"projects/{PROJECT_ID}/subscriptions/{SUB_ID}"

def callback(message):
    print('Received message:', message)
    print('data: ',message.data)
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

print("Listening for messages on ", subscription_path)

with subscriber:
    try:
        streaming_pull_future.result(timeout = TIMEOUT)

    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()
    finally :
        exit(0)