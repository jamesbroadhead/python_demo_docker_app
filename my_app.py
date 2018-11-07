#!/usr/bin/env python

import datetime
import pymongo
import time
while True:

    try:

        client = pymongo.MongoClient('my-replica-set3-0.my-replica-set3-svc.jbo.svc.cluster.local:27017')
        db = client.test_database
        dt = datetime.datetime.utcnow()
        post = {"author": "James",
                "text": "I wrote to a database on kubernetes",
                "date": dt}

        result = db.posts.insert_one(post)
        print('Posted successfully - {} at {}'.format(result.inserted_id, dt))
    except:
        raise # TODO rm
        print('Failed to post')
        time.sleep(0.5)
