import json
import os
from google.cloud import pubsub_v1

PROJECT_ID = os.getenv('PROJECT_ID')
TOPIC_ID = os.getenv('TOPIC_ID')

publisher = pubsub_v1.PublisherClient(
    publisher_options = pubsub_v1.types.PublisherOptions(
        enable_message_ordering=True,
    )
)

topic_path = f"projects/{PROJECT_ID}/topics/{TOPIC_ID}"


# payload = {
#     "_id": "1",
#     "name": "Steve",
#     "email": "brian.pinto@niveussolutions.com"
# }

# json_payload = json.dumps(payload).encode('utf-8')


for _ in range(1, 11):
    data = f"Message number {_}".encode('utf-8')
    future = publisher.publish(topic_path, data, user_id=f"{_}", order_number=f"{_}", price=f"{_}")
    print("published message id", future.result())


