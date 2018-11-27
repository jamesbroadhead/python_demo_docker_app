#!/usr/bin/env python

import datetime
import pymongo
import time

print("Starting up the app!")

client = pymongo.MongoClient(
    'my-replica-set-0.my-replica-set-svc.jbo.svc.cluster.local:27017',
    serverSelectionTimeoutMS=500,
    connectTimeoutMS=500,
    socketTimeoutMS=500)
db = client.test_database

while True:
    time.sleep(0.1)
    dt = datetime.datetime.utcnow()
    try:
        post = {
            "author": "James",
            "text": "I wrote to a database on kubernetes",
            "date": dt
        }

        result = db.posts.insert_one(post)
        print('Posted successfully - {} at {}'.format(result.inserted_id, dt))
    except Exception as e:
        print('Failed to post - {} - at {}'.format(e, dt))

print("Exiting")
