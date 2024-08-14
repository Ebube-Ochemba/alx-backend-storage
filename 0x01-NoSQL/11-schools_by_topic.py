#!/usr/bin/env python3
'''Task 11's module.
'''


def schools_by_topic(mongo_collection, topic):
    '''
    return: the list of school having a specific topic
    '''
    filtr = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return list(mongo_collection.find(filtr))
