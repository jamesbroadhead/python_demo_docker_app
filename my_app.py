#!/usr/bin/env python

import datetime
import pymongo
import time

print("Starting up the app!")

while True:
    try:
        client = pymongo.MongoClient('my-replica-set-0.my-replica-set-svc.jbo.svc.cluster.local:27017', serverSelectionTimeoutMS=500)
        db = client.test_database
        break
    except Exception as e:
        print('Failed to initially connect to mongo - waiting - {}'.format(e))



while True:
    time.sleep(100)
    try:
        dt = datetime.datetime.utcnow()
        post = {"author": "James",
                "text": "I wrote to a database on kubernetes",
                "date": dt}

        result = db.posts.insert_one(post)
        print('Posted successfully - {} at {}'.format(result.inserted_id, dt))
    except Exception as e:
        print('Failed to post - {}'.format(e))

print("Exiting")
