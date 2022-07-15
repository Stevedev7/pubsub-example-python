import os
from google.cloud import pubsub_v1

TOPIC_ID = "new-topic"
PROJECT_ID = os.getenv('PROJECT_ID')

publisher = pubsub_v1.PublisherClient()
topic_name = f'projects/{PROJECT_ID}/topics/{TOPIC_ID}'

publisher.create_topic(name=topic_name)